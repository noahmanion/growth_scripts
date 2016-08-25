import requests
import csv
import time

# set filename with date + time
timestr = time.strftime("%m-%d-%Y-%H-%M-%S")
filename = str("redirect-output\\redirect-test-"+timestr+".csv")

with open('urls-in1.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        urls = row[0]
        #print urls
        r = requests.get(urls)

f = open(filename, 'a+')
response = requests.get(r)
if response.history:
    print "Request was redirected:"
    reqredirected = "Request was redirected:"
    f.write(reqredirected)
    f.write("\n")
    for resp in response.history:
        print resp.status_code
        status = str(resp.status_code)
        f.write(status)
        f.write("\n")
        print resp.url
        url = str(resp.url)
        f.write(url)
        f.write("\n")
    print "Final destination:"
    final = "Final destination:"
    f.write(final)
    f.write("\n")
    print response.status_code
    destinationstatus = str(response.status_code)
    f.write(destinationstatus)
    f.write("\n")
    print response.url
    destinationurl = str(response.url)
    f.write(destinationurl)
    print "\n"
    f.write("\n")
else:
    print "Request was not redirected"
    noredirect = "Request was not redirected"
    f.write(noredirect)
    f.write("\n")
    responseurl = response.url
    print responseurl
    f.write(responseurl)
    f.write("\n")