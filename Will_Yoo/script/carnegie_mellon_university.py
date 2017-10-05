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
file_export = open('carnegie_mellon_university_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)

primary_url = 'https://directory.andrew.cmu.edu/index.cgi/'

name_keys = 'abcdefghijklmnopqrstuvwxyz'                                                    #Name keys to be used for name filter
school = 'Carnegie Mellon University'

def get_details():
    for i in xrange(26):
        for j in xrange(26):
            print name_keys[i]+name_keys[j]
            payload = "first_name={}*&last_name=&andrew_id=&email=&action=Search&searchtype=advanced&activetab=advanced".format(name_keys[i]+name_keys[j])
            resp = requests.request("POST", primary_url, data=payload)

            pq = PyQuery(resp.text)

            for people in pq('table tr'):
                if pq(people)('td:nth-child(4)').text().lower() == 'faculty':
                    csv_row = []
                    csv_row.append(pq(people)('td:nth-child(2)').text()+' '+pq(people)('td:nth-child(1)').text())
                    csv_row.append(pq(people)('td:nth-child(5)').text())
                    csv_row.append(school)

                    resp_people = requests.get('https://directory.andrew.cmu.edu/'+pq(people)('td:nth-child(1) a').attr('href'))

                    pq_people = PyQuery(resp_people.text)
                    csv_row.append(re.search('Email: (.*?) ',pq_people('#content > div > p').text()).group(1))
                    wr.writerow(csv_row)


get_details()