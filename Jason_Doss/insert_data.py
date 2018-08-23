'''
Created on Jul 21, 2018

@author: talib
'''

import psycopg2
import json


DB_ADDRESS = "localhost"
DB_USER = "jasondoss"
DB_PASS = "jasondoss1!2@"
DB_NAME = "postgres"

scrape_id = 1


db1 = psycopg2.connect(host=DB_ADDRESS,user=DB_USER,password=DB_PASS,database=DB_NAME )
cursor1 = db1.cursor()
    

def update_scrape_id():
    global scrape_id
    db = psycopg2.connect(host=DB_ADDRESS,user=DB_USER,password=DB_PASS,database=DB_NAME )
    cursor = db.cursor()
    cursor.execute("SELECT scrape_id from individual_scrape_id ORDER BY scrape_id DESC LIMIT 1")
    data = cursor.fetchall()
     
      
    if len(data) == 0 :
        exists = False
    else:
        scrape_id = int(data[0][0]) + 1
      
    cursor.execute("INSERT INTO individual_scrape_id (scrape_id) VALUES ('{}')".format(str(scrape_id)))
    db.commit()
    db.close()




#def insert_data(id,firstname,lastname, p_employments, c_employments, disclosures, pemp_count, cemp_count, disclosure_count, id, scrape_id):
    


def read_line(linedata):
    
    #print (linedata)
    j = json.loads(linedata)
    print (j.get('individualId',''))
    id1 = j.get('individualId','')
    
    if j.get('firstName',''):
        firstname = j.get('firstName','').encode('ascii', 'ignore').decode('ascii').replace("'","''")
    else:
        firstname = ''
        
    if j.get('lastName',''):
        lastname = j.get('lastName','').encode('ascii', 'ignore').decode('ascii').replace("'","''")
    else:
        lastname = ''
        
    pe = []
    ce = []
    dis = []

    dis_temp = json.loads(j.get('disclosures',[]))
    pemp_temp = json.loads(j.get('previousEmployments',[]))
    cemp_temp = json.loads(j.get('currentEmployments',[]))

    
    if dis_temp:
        for d in dis_temp:
    
            dobj = {}
            dobj["disclosureType"] = d.get('disclosureType','')
            dobj["eventDate"] = d.get('eventDate','')
            dis.append(dobj)
        disclosure_count = str(len(dis_temp))
    else:
        disclosure_count = '0'
    if pemp_temp:
        for pemp in pemp_temp:
            if pemp.get('firmName',''):
                pe.append(pemp.get('firmName','').encode('ascii', 'ignore').decode('ascii')) 
        pemp_count  = str(len(pemp_temp))
    else:
        pemp_count  = '0'
            
    if cemp_temp:
        for cemp in cemp_temp:
            if cemp.get('firmName',''):
                ce.append(cemp.get('firmName','').encode('ascii', 'ignore').decode('ascii')) 
        cemp_count = str(len(cemp_temp))
    else:
        cemp_count = '0'
            

    p_employments = '; '.join(pe).replace("'","''")
    c_employments = '; '.join(ce).replace("'","''")
    disclosures = json.dumps(dis).replace("'","''")

    
    
   
    
    
    
    
    
    sql_statement = '''INSERT INTO individuals ("id", "firstname", "lastname", "p_employments", "c_employments", "disclosures", "pemp_count", "cemp_count", "disclosure_count", "scrape_id") VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(id1,firstname,lastname, p_employments, c_employments, disclosures, pemp_count, cemp_count, disclosure_count, scrape_id)
    #print (sql_statement)
    cursor1.execute(sql_statement)
    db1.commit()

    #print (j['_type'])

update_scrape_id()

try:
    with open("james_data.jl") as myfile:
        for line in myfile:
            read_line(line)
except Exception as e:
    print (e)
finally:
    db1.close()


    

