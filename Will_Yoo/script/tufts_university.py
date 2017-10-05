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
file_export = open('tufts_university_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = "https://whitepages.tufts.edu/searchresults.cgi"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Tufts University'



all_urls = []
def build_urls():
    for i in xrange(26):
        for j in xrange(26):
            print name_keys[i] + name_keys[j]
            payload = "type=Faculty%2FStaff&search={}".format(name_keys[i] + name_keys[j])
            response = requests.request("POST", "https://whitepages.tufts.edu/searchresults.cgi", data=payload)

            pq = PyQuery(response.text)
            for people in pq('.responsive-table tr a'):
                all_urls.append(people.attrib['href'])
    return all_urls


def worker(q):
    while not q.empty():
        print 'Remaining - '+str(q.qsize())
        try:
            resp_p = requests.get('https://whitepages.tufts.edu/' +q.get())

            pq_p = PyQuery(resp_p.text)
            csv_row = []
            csv_row.append(pq_p('[onmouseover^="ddrivetip(\'<b>Name"]').parent().parent()('td:nth-child(2)').text())
            csv_row.append(
                pq_p('[onmouseover^="ddrivetip(\'<b>Department"]').parent().parent()('td:nth-child(2)').text())
            csv_row.append(pq_p('[onmouseover^="ddrivetip(\'<b>Primary Tufts Affiliation"]').parent().parent()(
                'td:nth-child(2)').text())
            csv_row.append(
                pq_p('[onmouseover^="ddrivetip(\'<b>Email Address"]').parent().parent()('td:nth-child(2)').text())
            wr.writerow(csv_row)
        except Exception,e:
            print e

q = Queue()
map(q.put, build_urls())
#Will create 10 threads

print 'Total urls - '+str(len(all_urls))

for i in range(50):
    t = Thread(target=worker, args=(q, ))
    t.start()