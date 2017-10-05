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
file_export = open('brown_university_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = "https://www.directory.gatech.edu/directory/results/a/a"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Brown University'

all_urls = []
def build_urls():
    for i in xrange(26):
        for j in xrange(26):
            for k in xrange(26):
                all_urls.append(name_keys[i]+name_keys[j]+name_keys[k])
    return all_urls


def worker(q):
    while not q.empty():
        print 'Remaining - '+str(q.qsize())
        try:
            resp = requests.get('http://directory.brown.edu/?search_string='+q.get())

            pq_r = PyQuery(resp.text)

            for people in pq_r('.vcard.faculty.badged'):

                csv_row = []
                csv_row.append(pq_r(people)('.fn').text())
                csv_row.append(pq_r(people)('.org').text())
                csv_row.append(school)
                csv_row.append(pq_r(people)('.email').text())
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
