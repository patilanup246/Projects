'''
Created on Jun 27, 2018

@author: talib
'''
import json
import requests
import psycopg2
from operator import sub
DB_ADDRESS = "brokercheck.c3l9vpoajvgp.us-east-2.rds.amazonaws.com"
DB_USER = "jasondoss"
DB_PASS = "jasondoss1!"
DB_NAME = "brokercheck"
scrape_id = 1




def get_scrape_id():
    db = psycopg2.connect(host=DB_ADDRESS,user=DB_USER,password=DB_PASS,database=DB_NAME )
    print ('started')
    cursor = db.cursor()
    cursor.execute("SELECT scrape_id from individual_scrape_id ORDER BY scrape_id DESC LIMIT 1")
    data = cursor.fetchall()
    db.close()
    return int(data[0][0])
    
    
def get_disclosures_count(disclosures):
    curr_cust_dispute = 0
    curr_regulatory = 0
    curr_employment_separation_after_allegations = 0
    curr_investigation = 0
    curr_financial = 0 
    curr_civil = 0
    curr_criminal = 0

    for cd in json.loads(disclosures):
        if 'Customer Dispute' in cd['disclosureType']:
            curr_cust_dispute+=1
            
        if 'Regulatory' in cd['disclosureType']:
            curr_regulatory+=1
            
        if 'Employment Separation After Allegations' in cd['disclosureType']:
            curr_employment_separation_after_allegations+=1
            
        if 'Investigation' in cd['disclosureType']:
            curr_investigation+=1
            
        if 'Financial' in cd['disclosureType']:
            curr_financial+=1
            
        if 'Civil' in cd['disclosureType']:
            curr_civil+=1
            
        if 'Criminal' in cd['disclosureType']:
            curr_criminal+=1
            
            
    return (curr_cust_dispute,curr_regulatory,curr_employment_separation_after_allegations,curr_investigation,curr_financial,curr_civil,curr_criminal)

current_scrape_id = get_scrape_id()
last_scrape_id = current_scrape_id - 1






db = psycopg2.connect(host=DB_ADDRESS,user=DB_USER,password=DB_PASS,database=DB_NAME )
cursor = db.cursor()


# delete_broker = '''DELETE FROM finra_individuals where cast("scrapeID" as bigint) <= {}'''.format(current_scrape_id-5)
# cursor.execute(delete_broker)
# db.commit()

cursor.execute('''SELECT "individualId","currentEmployments", "previousEmployments", "disclosures","registrationCount_approvedStateRegistrationCount" from finra_individuals where "scrapeID" = \'{}\' '''.format(current_scrape_id))
current_data = cursor.fetchall()


# cursor.execute('''SELECT "individualId","currentEmployments", "previousEmployments", "disclosures","registrationCount_approvedStateRegistrationCount" from finra_individuals where "scrapeID" = \'{}\''''.format(last_scrape_id))
# last_data = cursor.fetchall()


# for cd in current_data:
#     is_firm_changed = 0
#     is_active = 0
#     
#     try:
#         curr_dis_count = get_disclosures_count(cd[3])
#         last_dis_count = (0,0,0,0,0,0,0)
#         
#         last_state_count = 0
#         curr_state_count = int(cd[4])
#         
#         curr_firm = cd[1]
#         
#         if curr_firm:
#             is_active = 1
#         
#         for ld in last_data:
#             if cd[0] == ld[0]:
#                 last_dis_count = get_disclosures_count(ld[3])
#                 last_firm = ld[1]
#                 last_state_count = int(ld[4])
#                 if not last_firm == curr_firm:
#                     is_firm_changed = 1
#                 print 
#         
#             
#                 break
#         disclosure_diff = [a - b for a, b in zip(curr_dis_count, last_dis_count)]
#         state_count_diff = curr_state_count-last_state_count
#         print (is_firm_changed)
#         print (is_active)
#         print (curr_dis_count)
#         print (last_dis_count)
#         print (disclosure_diff)
#         print (state_count_diff)
#         
# 
#     
#     except Exception as e:
#         print (e)
#         print (cd[0])

    
    

#    finally:


for cd in current_data:
    print (cd[1])
db.close()
