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
file_export = open('wustl_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)


primary_url = 'https://directory.uchicago.edu/individuals/results'

departments_links = [
    'http://bulletin.wustl.edu/undergrad/artsci/philosophy/#facultylink',
    'http://bulletin.wustl.edu/undergrad/artsci/politicalscience/#facultylink',
    'http://bulletin.wustl.edu/undergrad/artsci/history/#facultylink',
    'http://bulletin.wustl.edu/undergrad/artsci/english/#facultylink',
    'http://bulletin.wustl.edu/undergrad/artsci/biology/#faculty',
    'http://bulletin.wustl.edu/undergrad/artsci/biology/#faculty'] #Available department list

name_keys = 'abcdefghijklmnopqrstuvwxyz'                                                    #Name keys to be used for name filter
school = 'Washington University in St. Louis'

all_urls = []  #will hold all the urls that will then be passed to threads


def step1():
    for dep in departments_links:
        resp = requests.get(dep)
        pq = PyQuery(resp.text)

        for people_link in pq('.keeptogether a'):
            print people_link.attrib['href']
            all_urls.append(people_link.attrib['href'])
    return all_urls


def step2():
    for url in step1():
        resp = requests.get(url)
        print url
        pq = PyQuery(resp.text)
        csv_row = []
        csv_row.append( pq('.pane-content .pane-title').text())
        csv_row.append( pq('#site-name span').text())
        csv_row.append( school)
        csv_row.append( pq('a.mailto').attr('href'))
        wr.writerow(csv_row)
step2()