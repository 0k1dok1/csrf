require 'uri'
require 'net/http'

url = URI("<put your url here>")
cookies = {}

Net::HTTP.start(url.host, url.port) do |http|
  response = http.get(url.path)
  response.get_fields('set-cookie').each do |cookie|
    cookies.merge!(Hash[cookie.split(';').map {|val| val.split('=') }])
  end
end

data = URI.encode_www_form('<put your POST data here>').concat('&csrf_token=fake_token')

options = {
  :body => data,
  :headers => {
    "Content-Type" => "application/x-www-form-urlencoded",
    "Cookie" => cookies.map{|k, v| "#{k}=#{v}" }.join(';')
  },
  :max_redirects => 0,
  :read_timeout => 20
}
response = Net::HTTP.post(url, options)

if response.code.to_i == 403
  puts "The URL #{url} has CSRF protection enabled."
elsif response.code.to_i == 200
  puts "The URL #{url} does not have CSRF protection enabled."
else
  puts "An error occurred."
end
