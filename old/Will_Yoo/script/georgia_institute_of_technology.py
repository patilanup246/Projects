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
file_export = open('georgia_institute_of_technology_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = "https://www.directory.gatech.edu/directory/results/a/a"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Georgia Institute of Technology'


headers2 = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'cookie': "has_js=1; _ga=GA1.2.810673548.1498669397; _gid=GA1.2.1974401806.1498669397",
    'host': "www.directory.gatech.edu",
    'referer': "https://www.directory.gatech.edu/directory/results/a/a",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }

all_urls = []
def build_urls():
    for i in xrange(26):
        for j in xrange(26):
            response = requests.request("GET","https://www.directory.gatech.edu/directory/results/{}/{}".format(name_keys[i],name_keys[j]),headers=headers2)
            pq = PyQuery(response.text)
            print name_keys[i],name_keys[j]
            for people in pq('p a'):
                all_urls.append(people.attrib['href'])
    return all_urls



def worker(q):
    while not q.empty():
        print 'Remaining - '+str(q.qsize())
        try:
            resp = requests.get('https://www.directory.gatech.edu'+q.get(), headers=headers2)
            csv_row = []
            pq_r = PyQuery(resp.text)
            csv_row.append(pq_r('.content.block-body.clearfix h2').text())
            csv_row.append(pq_r('.content.block-body.clearfix p:nth-child(3)').text())
            csv_row.append(school)
            csv_row.append(pq_r('a[href^="mailto"]').text())
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