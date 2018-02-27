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
file_export = open('pomona_college_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = "https://www.pomona.edu/directory/people"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Pomona College'

all_urls=[]
def build_urls():
    for i in xrange(26):
        for j in xrange(26):
            for k in xrange(26):
                all_urls.append(name_keys[i]+name_keys[j]+name_keys[k])
    return all_urls
headers2 = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'connection': "keep-alive",
    'host': "jicsweb.pomona.edu",
    'referer': "https://www.pomona.edu/directory/people",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    'cache-control': "no-cache"
    }

def worker(q):
    while not q.empty():
        print 'Remaining - '+str(q.qsize())
        try:

            querystring = {"first": q.get(), "last": ""}
            resp = requests.get("https://jicsweb.pomona.edu/api/employees", headers=headers2, params=querystring).json()


            for person in resp:
                #print person
                csv_row = []
                csv_row.append(person['FullName'])
                csv_row.append(person['Office'])
                csv_row.append(school)
                csv_row.append(person['Email'])
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
