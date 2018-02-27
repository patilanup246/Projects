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
file_export = open('cornwell_university_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = "https://www.engineering.cornell.edu/research/faculty/directory.cfm?letter=all&sort=alpha"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Cornwell University'


resp = requests.get('https://www.engineering.cornell.edu/research/faculty/directory.cfm?letter=all&sort=alpha')

pq = PyQuery(resp.text)

for people in pq('table tr'):
    if pq(people)('td:nth-child(2) a').text():
        csv_row = []
        csv_row.append( pq(people)('td:nth-child(2) a').text())
        csv_row.append( pq(people)('td:nth-child(3)').text())
        csv_row.append( school)
        csv_row.append( pq(people)('td:nth-child(2) a').attr('href').replace('profile.cfm?netid=','')+'@cornell.edu')
        wr.writerow(csv_row)
