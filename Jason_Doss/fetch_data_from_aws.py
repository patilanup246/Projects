'''
Created on Jul 24, 2018

@author: talib
'''
import json
import psycopg2
DB_ADDRESS = "178.128.148.219"
DB_USER = "jasondoss"
DB_PASS = "jasondoss1!2@"
DB_NAME = "postgres"
scrape_id = 1

o = open('jason_data2.txt','w')
    
db = psycopg2.connect(host=DB_ADDRESS,user=DB_USER,password=DB_PASS,database=DB_NAME )
print ('started')
cursor = db.cursor()
cur1 = cursor.execute('select "id" from individuals where scrape_id = \'3\'')

data = cursor.fetchall()

for d in data:

    
    
    o.write (d[0]+'\n')
    o.flush()
db.close()