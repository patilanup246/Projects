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
file_export = open('case_western_reserve_university_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = "https://webapps.case.edu/directory/lookup?search_text=&surname=&givenname=aa*&department=&location=&category=faculty&search_method=regular"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Case Western Reserve University'

for i in xrange(26):
    for j in xrange(26):
        try:
            resp = requests.get('https://webapps.case.edu/directory/lookup?search_text=&surname=&givenname={}*&department=&location=&category=faculty&search_method=regular'.format(name_keys[i]+name_keys[j]))
            pq = PyQuery(resp.text)
            email = ''
            name = ''
            dept = ''
            for people in pq('.dirresults tr'):

                if pq('.dirresults tr').index(people) % 2 == 0:
                    email =  pq(people)('td:nth-child(1)').text()
                    dept  =  pq(people)('td:nth-child(2)').text()
                else:
                    csv_row = []
                    csv_row.append( name)
                    csv_row.append( email)
                    csv_row.append(school)
                    csv_row.append( dept )
                    wr.writerow(csv_row)
                    name = pq(people)('td:nth-child(1)').text()
                    print name.encode('ascii','ignore')

        except Exception,e:
            print 'exception'