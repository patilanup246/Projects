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
file_export = open('rice_university_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = 'https://search.rice.edu/html/people/p/0/0/'

departments = ['Philosophy','Political Science','History','English','Biology','Psychology'] #Available department list

name_keys = 'abcdefghijklmnopqrstuvwxyz'                                                    #Name keys to be used for name filter
school = 'Rice University'

all_urls = []  #will hold all the urls that will then be passed to threads

for i in xrange(26):
    resp = requests.get(primary_url+'?firstname={}*'.format(name_keys[i]))
    print name_keys[i]
    pq = PyQuery(resp.text)
    print resp.text
    for people in pq('.results'):
        if 'faculty' in pq(people)('.affiliation').text().lower():
            print pq(people)('.name').text()
            csv_row = []
            csv_row.append(pq(people)('.name').text())
            csv_row.append(pq(people)('.department').text())
            csv_row.append(school)
            csv_row.append(pq(people)('.email').text())