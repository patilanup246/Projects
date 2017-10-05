from threading import Thread
from Queue import Queue
import requests
import csv
import datetime
import sys

reload(sys)
import time
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()
sys.setdefaultencoding('utf-8')  # set utf-8 encoding
# Check if pyquery is installed
try:
    from pyquery import PyQuery
except Exception, e:
    print 'Install package using pip - <pip install pyquery>'

# file for storing the results in csv format
file_export = open('university_of_illinois_urbana-champaign_professors_' + str(
    datetime.datetime.today().strftime('%Y-%m-%d')) + '.csv', 'wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name', 'Department', 'School', 'Email']  # csv headers
wr.writerow(headers)

primary_url = "http://illinois.edu/ds/facultyListing"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'University of Illinois Urbana-Champaign'

all_urls = []


def build_urls():
    resp = requests.get('http://illinois.edu/ds/facultyListing')
    pq = PyQuery(resp.text)
    for people in pq('[href^="http://illinois.edu/ds/search?search_type=userid&search="]'):
        all_urls.append(people.attrib['href'])
    return all_urls


def worker(q):
    while not q.empty():
        print 'Remaining - ' + str(q.qsize())
        try:
            url_link = q.get()
            time.sleep(5)
            resp = requests.get(url_link)

            csv_row = []
            pq_r = PyQuery(resp.text)
            print pq_r('#mobile-content h4').text()
            csv_row.append(pq_r('#mobile-content h4').text())
            csv_row.append(pq_r('.role-and-dept a').text())
            csv_row.append(school)
            print url_link.replace('http://illinois.edu/ds/search?search_type=userid&search=', '')
            csv_row.append(url_link.replace('http://illinois.edu/ds/search?search_type=userid&search=', ''))
            wr.writerow(csv_row)
        except Exception, e:
            print e


q = Queue()
map(q.put, build_urls())
# Will create 10 threads

print 'Total urls - ' + str(len(all_urls))

for i in range(1):
    t = Thread(target=worker, args=(q,))
    t.start()


