from threading import Thread
from Queue import Queue
import requests
import csv
import datetime
import sys
reload(sys)
import re

sys.setdefaultencoding('utf-8') #set utf-8 encoding
#Check if pyquery is installed
try:
    from pyquery import PyQuery
except Exception,e:
    print 'Install package using pip - <pip install pyquery>'

#file for storing the results in csv format
file_export = open('harvard_university_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email','Phone'] # csv headers
wr.writerow(headers)

primary_url = 'https://directory.andrew.cmu.edu/index.cgi/'

name_keys = 'abcdefghijklmnopqrstuvwxyz'                                                    #Name keys to be used for name filter
school = 'Harvard University'




for i in xrange(26):
    num=0
    while True:
        print 'http://facultyfinder.harvard.edu/search?name={}&offset={}'.format(name_keys[i],str(num*100))
        resp = requests.get('http://facultyfinder.harvard.edu/search?name={}&offset={}'.format(name_keys[i],str(num*100)))

        pq = PyQuery(resp.text)
        #print resp.text
        print name_keys[i]+str(num*100)
        if not len(pq('tr td a')):
            break

        for people in pq('tr'):
            csv_row = []
            if pq(people)('td:nth-child(1)').text():
                csv_row.append(pq(people)('td:nth-child(1)').text())
                csv_row.append(pq(people)('td:nth-child(3)').text())
                csv_row.append(pq(people)('td:nth-child(2)').text())
                csv_row.append('')
                print pq(people)('td:nth-child(1)').text()
                wr.writerow(csv_row)
        num+=1

