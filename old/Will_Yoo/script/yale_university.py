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
file_export = open('yale_university_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = 'https://directory.uchicago.edu/individuals/results'

departments = ['http://philosophy.yale.edu/people/faculty',
               'http://politicalscience.yale.edu/people/faculty',
               'http://history.yale.edu/people/faculty',
               'http://english.yale.edu/faculty-staff',
               'http://mcdb.yale.edu/people/faculty',
               'http://psychology.yale.edu/people/faculty'] #Available department list

name_keys = 'abcdefghijklmnopqrstuvwxyz'                                                    #Name keys to be used for name filter
school = 'Yale University'

all_urls = []  #will hold all the urls that will then be passed to threads

for dep in departments:
    resp = requests.get(dep)
    pq = PyQuery(resp.text)
    print dep
    for people in pq('.views-field.views-field-name'):
        csv_row = []
        print pq(people)('.username').text()
        csv_row.append( pq(people)('.username').text())
        csv_row.append( pq('.site-name a').text())
        csv_row.append( school)
        if not pq('.views-field.views-field-mail a'):
            try:
                csv_row.append( pq(people)('.views-field.views-field-name a:nth-child(5)').attr('href').replace('mailto:',''))
            except AttributeError,e:
                pass
        else:
            try:
                csv_row.append(pq(people).parent()('.views-field.views-field-mail a').attr('href').replace('mailto:',''))
            except AttributeError,e:
                pass
        wr.writerow(csv_row)