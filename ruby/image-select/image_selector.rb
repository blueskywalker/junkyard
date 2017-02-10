
require 'sinatra'
require 'mongo'
require 'json'
require 'koala'

mongo_host=['brandflask.com']
mongo_opts= {
  database: 'brandflask',
  user: 'olympus',
  password: 'oft7,harrows'
}
client = Mongo::Client.new(mongo_host,mongo_opts)

get '/' do
  send_file  File.join(settings.public_folder, 'index.html')
end

get '/graph' do
  page = params['page'].to_i
  size = params['size'].to_i

  page = 1 if page == 0
  size = 1 if size == 0

  brandimages = client['brandimages']
  total = brandimages.count
  found = brandimages.find.skip((page - 1) * size).limit(size)

  data = []
  found.each { |r|  data << r }
  output = {total: total, size: size, page: page, data: data }
  output.to_json
end

get '/facebook' do
  fbid=params['fbid']
  return {} unless fbid
  access_token="1380374468852725%7Cd5zZcwcUyaF7i1VMUa31kD1Pz6k"
  graph = Koala::Facebook::API.new(access_token)
  Koala.config.api_version = "v2.8"
  graph.get_object("#{fbid}?field=id,name").to_json
end
