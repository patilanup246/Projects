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
file_export = open('northeastern_university_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = "https://prod-web.neu.edu/wasapp/employeelookup/public/searchEmployees.action"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Northeastern University'



url = "https://prod-web.neu.edu/wasapp/employeelookup/public/searchEmployees.action"


headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'content-length': "104",
    'content-type': "application/x-www-form-urlencoded",
    'cookie': "JSESSIONID=0000b6PgZFdRMSwlpTWpTS20Edu:188q12kdr",
    'host': "prod-web.neu.edu",
    'origin': "https://prod-web.neu.edu",
    'referer': "https://prod-web.neu.edu/wasapp/employeelookup/public/searchEmployees.action",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    }
for i in xrange(26):
    for j in xrange(26):
        payload = "searchBy=First%20Name&queryType=begins%20with&searchText={}&deptText=&addrText=&numText=&divText=&facStaff=2".format(name_keys[i]+name_keys[j])
        response = requests.request("POST", url, data=payload, headers=headers)
        print name_keys[i]+name_keys[j]
        pq = PyQuery(response.text)
        #print(response.text)
        for people in pq('#result tr'):
            if pq(people)('td a').text():
                csv_row = []
                csv_row.append( pq(people)('td a').text())
                csv_row.append( pq(people)('td:nth-child(9)').text())
                csv_row.append( school)
                csv_row.append( pq(people)('td:nth-child(5)').text())
                wr.writerow(csv_row)
