import requests
from queue import Queue
from threading import Thread
from pyquery import PyQuery
t = 1
f_out = open('f_out.txt','w')
q = Queue()
[q.put(i) for i in open('input.txt','r').read().split('\n')]

def worker(q):
    while not q.empty():
        try:
            url = q.get()
            print (url)
            r = requests.get('http://www.zawya.com' + url).text
            pq = PyQuery(r)

            numbers = []
            for p in pq('.info-box li strong'):
                numbers.append(p.text)

            details = []

            for p in pq('.info-box li a'):
                details.append(p.text)

            f_out.write(str('http://www.zawya.com' + url) + '\t\t' + str(','.join(numbers)) +'\t\t'+ str(pq('address').text())+ '\t\t' + str(','.join(details)) + '\n')
            f_out.flush()

        except Exception as e:
             print(e)
        finally:
            q.task_done()

# for i in open('input.txt','r').read().split('\n'):
#     r = requests.get('http://www.zawya.com'+i).text
#     pq = PyQuery(r)
#
#     numbers = []
#     for p in pq('.info-box li strong'):
#         numbers.append(p.text)
#
#     details = []
#
#     for p in pq('.info-box li a'):
#         details.append(p.text)
#
#     f_out.write(str(t)+'-->'+str(','.join(numbers))+'-->'+str(','.join(details))+'\n')
#     f_out.flush()
#     print (t)
#     t+=1

for i in range(10):
    #print (i)
    t = Thread(target=worker, args=(q, ))
    t.start()
q.join()