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
file_export = open('UOC_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = 'https://directory.uchicago.edu/individuals/results'

departments = ['Philosophy','Political Science','History','English','Biology','Psychology'] #Available department list

name_keys = 'abcdefghijklmnopqrstuvwxyz'                                                    #Name keys to be used for name filter
school = 'University of Chicago'

all_urls = []  #will hold all the urls that will then be passed to threads

#Method for building Urls for queue
def build_urls():
    for department in departments:
        for i in xrange(26):
            all_urls.append(primary_url+'?name={}*&organization={}'.format(name_keys[i],department.replace(' ','+')))
    return all_urls


#worker method
def worker(q):
    while not q.empty():
        print 'Remaining - '+str(q.qsize())
        try:
            url = q.get()
            resp = requests.get(url)
            pq = PyQuery(resp.text)
            department_name = pq('caption a').text()[1:].replace('" departments','')

            for person in pq('tbody tr'):
                csv_row = []
                csv_row.append(pq(person)('td:nth-child(1) a').text())
                csv_row.append(department_name)
                csv_row.append(school)
                csv_row.append(pq(person)('td:nth-child(3) a').text())
                wr.writerow(csv_row)
        except Exception,e:
            print e

q = Queue()
map(q.put, build_urls())
#Will create 10 threads

print 'Total urls - '+str(len(all_urls))

for i in range(10):
    t = Thread(target=worker, args=(q, ))
    t.start()
