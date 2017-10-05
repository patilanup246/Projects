from threading import Thread
from Queue import Queue
import requests
import csv
import datetime
import sys
reload(sys)

sys.setdefaultencoding('utf-8') #set utf-8 encoding
#Check if pyquery is installed
try:
    from pyquery import PyQuery
except Exception,e:
    print 'Install package using pip - <pip install pyquery>'

#file for storing the results in csv format
file_export = open('bowdoin_college_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = "https://www.directory.gatech.edu/directory/results/a/a"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Bowdoin College'

departments =[
'philosophy',
'psychology',
'history',
'english',
'biology',
'psychology'
]

for dep in departments:
    resp = requests.get('https://www.bowdoin.edu/'+dep+'/faculty/index.shtml')

    pq = PyQuery(resp.text)

    for people in pq('.content a[href*="faculty"]'):
        try:
            csv_row = []
            print people.attrib['href']
            if 'http' in people.attrib['href']:
                resp_p = requests.get(people.attrib['href'])
            else:
                resp_p = requests.get('https://www.bowdoin.edu'+people.attrib['href'])

            pq_p = PyQuery(resp_p.text)

            if pq_p('.pagetitle').text():
                csv_row.append( pq_p('.pagetitle').text())
            else:
                csv_row.append( pq_p('.facname').text())
            csv_row.append(dep)
            csv_row.append( school)
            if pq_p('#content-wrapper [href^="mailto:"]').text():
                csv_row.append( pq_p('#content-wrapper [href^="mailto:"]').text())
            else:
                csv_row.append( pq_p('.email [href^="mailto:"]').text())
            wr.writerow(csv_row)
        except Exception,e:
            print e