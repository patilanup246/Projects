from threading import Thread
from Queue import Queue
import requests
import csv
import datetime
import sys
reload(sys)
import re
import time
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
sys.setdefaultencoding('utf-8') #set utf-8 encoding
#Check if pyquery is installed
try:
    from pyquery import PyQuery
except Exception,e:
    print 'Install package using pip - <pip install pyquery>'

#file for storing the results in csv format
file_export = open('massachusetts_institute_of_technology_professors_'+str(datetime.datetime.today().strftime('%Y-%m-%d'))+'.csv','wb')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['Name','Department','School','Email'] # csv headers
wr.writerow(headers)




primary_url = "http://web.mit.edu/bin/cgicso"
name_keys = 'abcdefghijklmnopqrstuvwxyz'
school = 'Massachusetts Institute of Technology'

#
resp = requests.get('http://web.mit.edu/philosophy/faculty.html')
pq = PyQuery(resp.text)
for people in pq('.faculty a'):
    print people.text
    print people.attrib['href']
    try:
        resp_p = requests.get('http://web.mit.edu/philosophy/'+people.attrib['href'])
        pq_p = PyQuery(resp_p.text)
        csv_row = []
        csv_row.append(people.text)
        csv_row.append('philosophy')
        csv_row.append(school)
        csv_row.append(pq_p('a[href^="mailto"]').text())
        wr.writerow(csv_row)
    except Exception,e:
        print e

resp = requests.get('http://web.mit.edu/polisci/people/faculty/index.html')
pq = PyQuery(resp.text)
for people in pq('#listings tr'):
    print pq(people)('.name').text()
    #print people.attrib['href']

    csv_row = []
    csv_row.append(pq(people)('.name').text())
    csv_row.append('polisci')
    csv_row.append(school)
    csv_row.append(pq(people)('.email .email').text())
    wr.writerow(csv_row)

resp = requests.get('http://history.mit.edu/people')
pq = PyQuery(resp.text)
for people in pq('.field-content a'):
    if people.text:
        print people.text
        print people.attrib['href']
        try:
            resp_p = requests.get('http://history.mit.edu'+people.attrib['href'])
            pq_p = PyQuery(resp_p.text)
            csv_row = []
            csv_row.append(people.text)
            csv_row.append('history')
            csv_row.append(school)
            csv_row.append(pq_p('.field-items a[href^="mailto"]').text())
            wr.writerow(csv_row)
        except Exception,e:
            print e

resp = requests.get('https://lit.mit.edu/people/')
pq = PyQuery(resp.text)
for people in pq('.row-hover tr'):
    if pq(people)('td:nth-child(2) a').text():
        print pq(people)('td:nth-child(2) a').text()
        #print people.attrib['href']

        csv_row = []
        csv_row.append(pq(people)('td:nth-child(2) a').text())
        csv_row.append('English')
        csv_row.append(school)
        csv_row.append(pq(people)('td:nth-child(5) a').text())
        wr.writerow(csv_row)


resp = requests.get('https://biology.mit.edu/research/faculty')
pq = PyQuery(resp.text)
for people in pq('tbody tr'):
    if pq(people)('.views-field.views-field-value-7 a').text():
        print pq(people)('.views-field.views-field-value-7 a').text()
        # print people.attrib['href']

        csv_row = []
        csv_row.append(pq(people)('.views-field.views-field-value-7 a').text())
        csv_row.append('Biology')
        csv_row.append(school)
        print pq(people)('.views-field.views-field-mail a:nth-child(2)').text()
        csv_row.append(pq(people)('.views-field.views-field-mail a:nth-child(2)').text())
        wr.writerow(csv_row)


resp = requests.get('https://bcs.mit.edu/our-faculty')
pq = PyQuery(resp.text)
for people in pq('a[href^="/users/"]'):
    if people.text:
        print people.text
        print people.attrib['href']
        try:
            resp_p = requests.get('https://bcs.mit.edu'+people.attrib['href'])
            pq_p = PyQuery(resp_p.text)
            csv_row = []
            csv_row.append(people.text)
            csv_row.append('psychology')
            csv_row.append(school)
            print pq_p('.field.user-email a[href^="mailto"]').text()
            csv_row.append(pq_p('.field.user-email a[href^="mailto"]').text())
            wr.writerow(csv_row)
        except Exception,e:
            print e




# for i in xrange(26):
#     for j in xrange(26):
#         time.sleep(2)
#         resp = requests.get('http://web.mit.edu/bin/cgicso?options=lastnamesx&query={}*'.format(name_keys[i]+name_keys[j]))
#         pq = PyQuery(resp.text)
#         print i,j
#         print resp.status_code
#         for people in pq('pre a'):
#             resp_2 = requests.get('http://web.mit.edu'+people.attrib['href'])
#             time.sleep(2)
#             pq2 = PyQuery(resp_2.text)
#             csv_row = []
#             try:
#                 print re.search('name: (.*?)\n',pq2('pre').text()).group(1)
#                 csv_row.append( re.search('name: (.*?)\n', pq2('pre').text()).group(1))
#                 csv_row.append( re.search('department: (.*?)\n', pq2('pre').text()).group(1))
#                 csv_row.append( school)
#                 csv_row.append( re.search('email: (.*?)\s', pq2('pre').text()).group(1))
#             #print csv_row
#                 wr.writerow(csv_row)
#             except:
#                 pass