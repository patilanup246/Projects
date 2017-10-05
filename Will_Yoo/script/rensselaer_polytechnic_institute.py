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
file_export = open('rensselaer_polytechnic_institute_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = "http://faculty.rpi.edu/data/peoplesearch"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Rensselaer Polytechnic Institute'


resp = requests.get(primary_url).json()['nodes']

for people in resp:
    csv_row = []
    print people['node']['title']
    csv_row.append(people['node']['title'])
    resp_p = requests.get('http://faculty.rpi.edu'+people['node']['Path'])
    pq = PyQuery(resp_p.text)

    csv_row.append( pq('.field-content h4').text())
    csv_row.append( school)
    csv_row.append( pq('a[href^="mailto:"]').text())
    wr.writerow(csv_row)