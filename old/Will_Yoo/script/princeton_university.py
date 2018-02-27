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
file_export = open('princeton_university_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = "https://www.princeton.edu/search/people-advanced"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Princeton University'


for i in xrange(26):
    p =0
    while True:
        resp = requests.get(primary_url+'?f={}&ff=b&t=Professor&tf=c&page={}'.format(name_keys[i],str(p)))
        print name_keys[i],str(p)
        p+=1
        pq = PyQuery(resp.text)

        if len(pq('.people-search-result-name h3')) == 0:
            break

        for people in pq('.row'):
            if pq(people)('.people-search-result-name h3').text():
                csv_row = []
                csv_row.append( pq(people)('.people-search-result-name h3').text() )
                csv_row.append( pq(people)('.expanded-details-value.title').text() )
                csv_row.append( school )
                csv_row.append( pq(people)('.people-search-email').text() )
                wr.writerow(csv_row)
