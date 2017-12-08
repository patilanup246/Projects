'''
Created on 02-Dec-2017

@author: Administrator
'''
#!/usr/bin/python

import sqlite3
import csv
reddit_id = []
import sys




conn = sqlite3.connect('reddit_crawl.db')
cursor = conn.execute("select distinct reddit_id from details")
for row in cursor:
    reddit_id.append(row[0])
conn.close()
 


max_fetch_num = 0
conn = sqlite3.connect('reddit_crawl.db')
cursor = conn.execute("select max(fetch_num) from details")
for row in cursor:
    max_fetch_num = int(row[0])
conn.close()
print (max_fetch_num)

def get_score(reddit_id,fetch_id):
    conn = sqlite3.connect('reddit_crawl.db')
    cursor = conn.execute("select {} from details where reddit_id = '{}' and fetch_num = {}".format(sys.argv[1], reddit_id,fetch_id))
    score_val = ''
    for row in cursor:
        score_val = row[0]
    conn.close()
    
    return score_val

output_f = open('reddit_formatted_output_{}.csv'.format(sys.argv[1]),'a',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)

output = []
for ri in reddit_id:
    ri_o = []
    ri_o.append(ri)
    for i in range(1,max_fetch_num+1):
        ri_o.append(get_score(ri, i))
    wr.writerow(ri_o)
    
