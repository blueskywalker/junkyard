#!/usr/bin/env ruby
#
require 'rest-client'
require 'json'
require 'time'
require 'easy_logging'
require 'set'
require 'psych'
require 'tempfile'

BASE_DIR = File.expand_path("#{File.dirname($0)}")
RESTART_SCRIPT="#{BASE_DIR}/scripts/spark-restart.sh"


class PrevJob
  attr_reader :job_id, :tz

  def initialize(job_id, tz)
    @job_id = job_id
    @tz = tz
  end

  def to_s
    "PrevJob(#{@job_id},#{@tz})"
  end

end


EasyLogging.log_destination = "#{BASE_DIR}/log/monitoring.log"

def get_spark_job(pod_name)
  content_yaml = `helm template spark-main-signals  lucid-data/#{pod_name}`
  config = Psych.load_stream(content_yaml)
  job = config.select { |item| item['metadata']['name'] == pod_name }
  if job.size > 0
    return Psych.dump(job[0])
  end
  return nil 
end

def kick_off_job(pod_name)
   spark_job = get_spark_job(pod_name)
   if not spark_job.nil?
       file = Tempfile.new('spark')
       file.write(spark_job)
       file.close
       cmd = "kubectl apply -f #{file.path}"
       system(cmd)
       file.unlink
   end
end

class SparkMonitor
  include EasyLogging
  attr_reader :pod_name, :job_name 

  def initialize(pod_name, job_name )
    @pod_name = pod_name
    @job_name = job_name
    @prev = nil
    @status = 'init'
  end

  def get_id
    begin
      response = RestClient.get "http://localhost:4040/api/v1/applications"
      if response.code == 200
        JSON.parse(response.body).each { |r|
          if r['name'] == @job_name
            return r['id']
          end
        }
      end
    rescue
      return nil
    end
    nil
  end

  def get_running_jobs(job_id)
    begin
      # job_id = get_id
      return nil if job_id.nil?
      response = RestClient.get "http://localhost:4040/api/v1/applications/#{job_id}/jobs?status=running"
      if response.code == 200
        return JSON.parse(response.body, object_class: OpenStruct)
      end
    rescue
      return nil
    end
    nil
  end

  def get_success_jobs(job_id)
    begin
      return nil if job_id.nil?
      response = RestClient.get "http://localhost:4040/api/v1/applications/#{job_id}/jobs?status=succeeded"
      if response.code == 200
        return JSON.parse(response.body, object_class: OpenStruct)
      end
    rescue
      return nil
    end
  end

  def idle_for(n)
    duration = Time.now - @prev.tz
    logger.info("#{@pod_name} duration - #{duration}  #{duration > n}")
    return true if duration > n
    false
  end

  def restart
    logger.info( "#{@pod_name} restarting" )
    cmd = "kubectl delete pod  #{@pod_name}"
    puts cmd
    `#{cmd}`
    cmd = "kubectl delete job/#{@pod_name}"
    puts cmd
    `#{cmd}`

    kick_off_job(@pod_name)
    @status = 'restart'
  end

  def checking_running_pod
    cmd = "kubectl get pod #@pod_name"
    running = system(cmd)
    if running
      return false if `#{cmd} | sed '1d'| awk '{print $3}'` == "Error"
      return true
    else
      return false
    end
  end

  def checking_job
    logger.info( "#{@pod_name} checking job" )
    unless self.checking_running_pod
      self.restart
      logger.info("#{@pod_name} sleep for waiting for spawning job")
      sleep 20
      return
    end
    pid = fork do
      logger.info( "#{@pod_name} port forwarding #{Process.pid}")
      cmd = "kubectl port-forward #{@pod_name} 4040:4040"
      exec cmd
      logger.info( "#{@pod_name} port-forwarding is done")
    end
    logger.info( "#{@pod_name} sleep 20 seconds for waiting for port-forwarding")
    sleep(20)
    logger.info( "#{@pod_name} wake up after sleeping" )
    job_id = self.get_id
    running_jobs = self.get_running_jobs(job_id)
    logger.info(running_jobs)
    if running_jobs.nil? or running_jobs.size == 0
      success_jobs = self.get_success_jobs job_id
      if !success_jobs.nil? and success_jobs.size > 0
        @prev = PrevJob.new(success_jobs[0]['jobId'], Time.parse(success_jobs[0]["completionTime"]))
        logger.info( "#{@pod_name} update previous job #{@prev}")
      end
      if @prev.nil? or self.idle_for(300)
        self.restart if @status != 'restart' and @status != 'init'
      else
        logger.info("#{@pod_name} skip...")
      end
    else
      @prev = PrevJob.new(running_jobs[0].jobId, Time.now)
      @status = 'running'
      logger.info( "#{@pod_name} update previous job #{@prev}")
    end
    logger.info( "#{@pod_name} kill #{pid}" )
    Process.kill('SIGINT', pid)
    logger.info( "#{@pod_name} wait #{pid}")
    Process.wait2 pid
  end
end

class HelmApp
  attr_reader :release, :chart
  def initialize(src)
    elem = src.split(" ")
    @release = elem[0] 
    @chart = elem[1].split('-')[0..-2].join('-')
  end
  
  def to_s
    "HelmApp(#{@release},#{@chart})"
  end
end

def helm_repo_update
  cmd="helm repo update"
  system(cmd)
end

def get_running_apps
  helm_repo_update
  cmd="helm list | sed '1d' | awk '{print $1,$9}'"
  list_app = `#{cmd}`
  output=Hash.new
  list_app.split("\n").map {|item| HelmApp.new(item) }.each {|item|
    output[item.chart] = item
  }
  output
end

def watching
  main_pipeline = SparkMonitor.new("spark-main-pipeline","Message Process")
  hot_pipeline = SparkMonitor.new("spark-hot-pipeline","Stream Sinker")
  signal_decoder = SparkMonitor.new("spark-signal-decoder","Message Decoding")
  jobs = [ main_pipeline, hot_pipeline, signal_decoder ]

  while true
    apps = get_running_apps 
    jobs.each { |job|
      if apps.include?(job.pod_name)
        job.checking_job
      end
      puts "#{job.pod_name} sleep 30 seconds"
      sleep 30
    }
  end
end

def main
  watching
end

main
