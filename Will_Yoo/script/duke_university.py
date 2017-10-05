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
file_export = open('duke_university_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = "https://trinity.duke.edu/directory/people/b"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Duke University'


for i in xrange(26):
    resp = requests.get('https://trinity.duke.edu/directory/people/'+name_keys[i])
    pq = PyQuery(resp.text)
    print name_keys[i]
    for people in pq('.person'):
        csv_row = []
        csv_row.append( pq(people)('h4').text())
        csv_row.append( pq(people)('.person-info a').text())
        csv_row.append( school)
        csv_row.append( pq(people)('.person-title [href^="mailto:"]').text())
        wr.writerow(csv_row)

