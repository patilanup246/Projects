'''
Created on 30-Nov-2017

@author: Administrator
'''
import requests
from pyquery import PyQuery
import time
import csv
import sqlite3
from datetime import datetime
#start_url = 'https://www.reddit.com/r/askreddit/top/?sort=top&t=day&count='
start_url = 'https://www.reddit.com/r/askreddit/top/?sort=top&t=day&count='
threshold_score = 20
pause_time = 1
auto_inc_id = 1
fetch_id = 1

def create_database():
    try:
        conn = sqlite3.connect('reddit_crawl.db')
        print ("Opened database successfully");
    
        conn.execute('''CREATE TABLE details
             (ID INTEGER  PRIMARY KEY AUTOINCREMENT,
             reddit_id                TEXT,
             title                    TEXT,
             suburl                   TEXT,
             timestamp                TEXT,
             score                    TEXT,
             comment                  TEXT,
             rank                     TEXT,
             fetch_time                TEXT,
             fetch_num                INTEGER,
             age                        TEXT
             );''')
        print ("Table created successfully");
    except Exception as e:
        print (e)
    finally:
        conn.close()

def get_field(p, css_selector, attribute):
    try:
        if attribute:
            return str(p(css_selector).attr(attribute))
        else:
            return str(p(css_selector).text())
    except Exception as e:
        return ''



def crawl_reddit(fetch_num,fetch_id):
    headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache",
    'pragma': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.70 Safari/537.36"
    }
    global auto_inc_id
    page_num = 0
    output_f = open('reddit_crawl.csv','a',encoding='utf-8', newline='')
    wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
    stop_crawling = 0
    last_id =''
    conn = sqlite3.connect('reddit_crawl.db')
    while page_num <= 250:
        print (start_url+str(page_num)+'&after='+last_id)
        resp = requests.get(start_url+str(page_num)+'&after='+last_id, headers=headers)
        time.sleep(3)
        pq = PyQuery(resp.text)
        #print (resp.text)
        page_num+=25
        global threshold_score
        
        for l in pq('[data-type="link"]'): 

            title = str(pq(l)('.title a').text())
            reddit_id = str(l.attrib['id'])
            sub_url = 'https://www.reddit.com'+str(pq(l)('.first a').attr('data-href-url'))
            timestamp = str(pq(l)('time').attr('datetime')).replace('T',' ').split('+')[0]+'.000000'
            
            try:
                score = str(int(pq(l)('.score.unvoted').attr('title')))
            except Exception as e:
                score = '-999'
            #score = str(l.attrib['data-score'])

            comments = pq(l)('.comments').text().replace(' comments','')
            #comments = str(l.attrib['data-comments-count'])

            rank = str(l.attrib['data-rank'])
            updated_reddit_id = reddit_id.replace('thing_t3_','')
            conn.execute("INSERT INTO details values (NULL,?,?,?,?,?,?,?,?,?,NULL)", [updated_reddit_id,title,sub_url,timestamp,score,comments,rank,fetch_num,fetch_id])
            conn.commit()
            conn.execute("Update details set age = (julianday(fetch_time) - julianday(timestamp))*24 where reddit_id = '{}' and fetch_num = {}".format(updated_reddit_id,fetch_id))
            conn.commit()
            details = []
            details.append(auto_inc_id)
            details.append(reddit_id.split('_')[2])
            details.append(title)
            details.append('https://www.reddit.com'+sub_url)
            details.append(timestamp)
            details.append(score)
            details.append(comments)
            details.append(rank)

            auto_inc_id+=1
            wr.writerow(details)
            
#             if not int(score) <= threshold_score:
#                 #print (score)
#                 auto_inc_id+=1
#                 wr.writerow(details)
#             else:
#                 stop_crawling = 1
            last_id = reddit_id.replace('thing_','')

#         if stop_crawling == 1:
#             break
        
    output_f.close()
    conn.close()
while True:
    try:
        create_database()
        crawl_reddit(str(datetime .utcnow()),str(fetch_id))
        fetch_id+=1
    except Exception as e:
        print (e)
    time.sleep(60*pause_time)
    
    