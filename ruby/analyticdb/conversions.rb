require 'sinatra'
require 'json'
require 'mysql2'
require 'rest-client'


get '/analytics/:account/organic-campaigns/conversions' do
  startDate = params['beginDate']
  endDate = params['endDate']
  account = params['account']

  headers = { 'X-CAPTORA-TOKEN' => 'APIKEY-ac6d68f24c46ea8cdcff4bbe8e330091', 'Content-Type' => "application/json;charset=UTF-8"}
  response=RestClient.get "http://qa5-analytics.captora.com/analytics/attribution-type/#{account}" , headers
  type=JSON.parse(response.body)['Value']

  column = case type
           when 'FIRSTORLASTTOUCH_CONVERSION' then 'all_first_lasttouch_conversions'
           when 'ANYTOUCH_CONVERSION' then 'all_anytouch_conversions'
           when 'FIRSTTOUCH_CONVERSION' then 'all_firsttouch_conversions'
           when 'LASTTOUCH_CONVERSION' then 'all_lasttouch_conversions'
           else
             'all_anytouch_conversions'
           end

  sql = %Q/
        SELECT cp_page_name, url, sum(all_total_visits) total_visits,sum(#{column}) total_conversions
        FROM urlstats
        WHERE client = '#{account}' AND is_ppc = 0
        AND date BETWEEN #{startDate} AND #{endDate}
        GROUP BY url
        /

  puts sql

  client = Mysql2::Client.new(:host => 'qa5-analytics-db.captora.com',
                              :username => 'captora_war',
                              :password => 'BOOST4CAPTORA',
                              :database => 'analytics')

  results = client.query(sql)
  output=[]
  results.each { |row|
    output << { 'pageName' => row['cp_page_name'], 'pageUrl' => row['url'],
                'visits' => row['total_visits'] , 'conversions' => row['total_conversions']}
  }

  content_type :json
  output.to_json
end
