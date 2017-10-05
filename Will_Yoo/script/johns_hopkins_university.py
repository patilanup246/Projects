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

file_export = open('johns_hopkins_university_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email','Phone'] # csv headers
wr.writerow(headers)

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'host': "krieger.jhu.edu",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"
    }

primary_url = 'http://krieger.jhu.edu/about/faculty/'

resp = requests.get(primary_url,headers=headers)

pq = PyQuery(resp.text)
#print resp.text

for people in pq('table tr'):
    print pq(people)('.column-1').text()
    if pq(people)('.column-5').text():
        csv_row = []
        csv_row.append(pq(people)('.column-1').text())
        csv_row.append(pq(people)('.column-5').text())
        csv_row.append('Johns Hopkins University')
        csv_row.append(pq(people)('.column-2 a').text())
        csv_row.append(pq(people)('.column-3').text())
        wr.writerow(csv_row)
        print csv_row
