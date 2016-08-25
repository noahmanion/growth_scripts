import csv
import requests

schools = {}
writer = csv.writer(open('urls-out.csv', 'wb'))

reader = csv.reader(open('urls-in1.csv'))
for row in reader:
	schools[row[0]]=row[1:]


print schools

for s in schools:
	var = requests.get(s)
	print var.url
	writer.writerow([var.url])
