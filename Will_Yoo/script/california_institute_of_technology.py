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
file_export = open('california_institute_of_technology_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email','Phone'] # csv headers
wr.writerow(headers)

primary_url = 'https://directory.caltech.edu/search/advanced_search'

name_keys = 'abcdefghijklmnopqrstuvwxyz'                                                    #Name keys to be used for name filter
school = 'California Institute of Technology'

for i in xrange(26):
    request_url = primary_url+'?personType=faculty&givenName='+name_keys[i]
    print request_url
    resp = requests.get(request_url)

    pq = PyQuery(resp.text)

    #print resp.text

    for people in pq('table tr'):
        csv_row = []
        #print pq(people)('td:nth-child(1)').text()
        csv_row.append(pq(people)('td:nth-child(1)').text())
        csv_row.append(pq(people)('td:nth-child(3)').text())
        csv_row.append(school)
        csv_row.append(pq(people)('td:nth-child(5)').text())
        csv_row.append(pq(people)('td:nth-child(4)').text())
        wr.writerow(csv_row)