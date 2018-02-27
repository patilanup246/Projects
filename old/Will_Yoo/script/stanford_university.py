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
file_export = open('stanford_university_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = "https://stanfordwho.stanford.edu/SWApp/Search.do"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Stanford University'

departments = ['philosophy','politicalscience','history','english','biology','psychology']

for dep in departments:
    resp = requests.get('https://{}.stanford.edu/people/faculty'.format(dep))

    pq = PyQuery(resp.text)

    for people in pq('.postcard-col2'):
        csv_row = []
        csv_row.append( pq(people)('h3 a').text())
        csv_row.append( dep)
        csv_row.append( school)
        csv_row.append( pq(people)('[href^="mailto:"]').text())
        wr.writerow(csv_row)