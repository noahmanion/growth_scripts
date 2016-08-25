require 'csv'
require 'net/http'
require 'uri'

CSV.foreach('urls-in.csv') do |row|
	res = Net::HTTP.get_response(URI(row))
	res['location']
end