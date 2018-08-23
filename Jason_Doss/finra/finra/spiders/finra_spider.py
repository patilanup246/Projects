# -*- coding: utf-8 -*-
from finra.items import Website
import scrapy
import json
import requests
class finra(scrapy.Spider):
    name="finra_individual"
    all_urls = []
    scraped_country = ''
    
    o = open('output.txt','w')
    DB_ADDRESS = "localhost"
    DB_USER = "jasondoss"
    DB_PASS = "jasondoss1!2@"
    DB_NAME = "postgres"
    scrape_id = 1
    
    #db1 = psycopg2.connect(host=DB_ADDRESS,user=DB_USER,password=DB_PASS,database=DB_NAME )
    #cursor1 = db1.cursor()
    
    def __init__(self, country = '', *args,**kwargs):
        
#         db = psycopg2.connect(host=self.DB_ADDRESS,user=self.DB_USER,password=self.DB_PASS,database=self.DB_NAME )
#         print ('started')
#         cursor = db.cursor()
#         cur1 = cursor.execute("SELECT scrape_id from individual_scrape_id ORDER BY scrape_id DESC LIMIT 1")
#         data = cursor.fetchall()
#         
#          
#         if len(data) == 0 :
#             exists = False
#         else:
#             self.scrape_id = int(data[0][0]) + 1
#          
#         cursor.execute("INSERT INTO individual_scrape_id (scrape_id) VALUES ('{}')".format(str(self.scrape_id)))
#         db.commit()
#         db.close()
        
        
        states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
        #states = []
        for s in states:
            start = 0
            while True:
                r = requests.get('http://doppler.finra.org/doppler-lookup/api/v1/search/individuals?hl=true&nrows=24&r=25&sort=score+desc&start={}&state={}&wt=json'.format(str(start),s)).json()
                 
                if not r['results']['BROKER_CHECK_REP']['results']:
                    break
                else:
                    for p in r['results']['BROKER_CHECK_REP']['results']:
                        self.all_urls.append (p['fields']['bc_source_id'])
                 
                start+=24
                 
                print(s+' -- \t -- '+str(start))
        
        

    def start_requests(self):
        for url in self.all_urls:
            #print (url)
            yield scrapy.Request(url='http://doppler.finra.org/doppler-lookup/api/v1/search/individuals/{}/?wt=json'.format(str(url)), callback=self.parse)
    
    
    
    def parse(self, response):
        item = Website()
        
        resp = json.loads(json.loads(response.body_as_unicode())['results']['BROKER_CHECK_REP']['results'][0]['fields']['content_json'][0])
        
        item['individualId'] = resp.get('basicInformation',{}).get('individualId','')
        item['firstName'] = resp.get('basicInformation',{}).get('firstName','')
        item['lastName'] = resp.get('basicInformation',{}).get('lastName','')
        item['nameSuffix'] = resp.get('basicInformation',{}).get('nameSuffix','')
        item['otherNames'] = json.dumps(resp.get('basicInformation',{}).get('otherNames',''))
        item['bcScope'] = resp.get('basicInformation',{}).get('bcScope','')
         
        item['iaScope'] = resp.get('basicInformation',{}).get('iaScope','')
        item['daysInIndustryCalculatedDate'] = resp.get('basicInformation',{}).get('daysInIndustryCalculatedDate','')
        item['daysInIndustry'] = resp.get('basicInformation',{}).get('daysInIndustry','')
        item['disclosureFlag'] = resp.get('basicInformation',{}).get('disclosureFlag','')
        item['iaDisclosureFlag'] = resp.get('basicInformation',{}).get('iaDisclosureFlag','')
        item['examsCount_stateExamCount'] = resp.get('examsCount',{}).get('stateExamCount','')
        item['examsCount_principalExamCount'] = resp.get('examsCount',{}).get('principalExamCount','')
        item['examsCount_productExamCount'] = resp.get('examsCount',{}).get('productExamCount','')
        item['registrationCount_approvedSRORegistrationCount'] = resp.get('registrationCount',{}).get('approvedSRORegistrationCount','')
        item['registrationCount_approvedFinraRegistrationCount'] = resp.get('registrationCount',{}).get('approvedFinraRegistrationCount','')
        item['registrationCount_approvedStateRegistrationCount'] = resp.get('registrationCount',{}).get('approvedStateRegistrationCount','')
        item['brokerDetails_hasBCComments'] = resp.get('brokerDetails',{}).get('hasBCComments','')
        item['brokerDetails_hasIAComments'] = resp.get('brokerDetails',{}).get('hasIAComments','')
        item['brokerDetails_legacyReportStatusDescription'] = resp.get('brokerDetails',{}).get('legacyReportStatusDescription','')
 
         
        item['currentEmployments']  = json.dumps( resp.get('currentEmployments'))
        item['previousEmployments'] = json.dumps( resp.get('previousEmployments'))
        item['disclosures']         = json.dumps( resp.get('disclosures'))
        #item['disclosures_length']  = len(resp.get('disclosures'))
        
        
#         sql_statement = '''INSERT INTO finra_individuals ("individualId", "firstName", "lastName", "nameSuffix", "otherNames", "bcScope", "iaScope", "daysInIndustryCalculatedDate", "daysInIndustry", "disclosureFlag", "iaDisclosureFlag", "examsCount_stateExamCount", "examsCount_principalExamCount", "examsCount_productExamCount", "registrationCount_approvedSRORegistrationCount", "registrationCount_approvedFinraRegistrationCount", "registrationCount_approvedStateRegistrationCount", "brokerDetails_hasBCComments", "brokerDetails_hasIAComments", "brokerDetails_legacyReportStatusDescription", "currentEmployments", "previousEmployments", "disclosures", "scrapeID" ) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(
#             str(resp.get('basicInformation',{}).get('individualId','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             resp.get('basicInformation',{}).get('firstName','').encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             
#             resp.get('basicInformation',{}).get('lastName','').encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('basicInformation',{}).get('nameSuffix','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('basicInformation',{}).get('otherNames','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('basicInformation',{}).get('bcScope','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('basicInformation',{}).get('iaScope','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('basicInformation',{}).get('daysInIndustryCalculatedDate','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('basicInformation',{}).get('daysInIndustry','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('basicInformation',{}).get('disclosureFlag','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('basicInformation',{}).get('iaDisclosureFlag','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('examsCount',{}).get('stateExamCount','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('examsCount',{}).get('principalExamCount','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('examsCount',{}).get('productExamCount','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('registrationCount',{}).get('approvedSRORegistrationCount','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('registrationCount',{}).get('approvedFinraRegistrationCount','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('registrationCount',{}).get('approvedStateRegistrationCount','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('brokerDetails',{}).get('hasBCComments','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('brokerDetails',{}).get('hasIAComments','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(resp.get('brokerDetails',{}).get('legacyReportStatusDescription','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(json.dumps( resp.get('currentEmployments'))).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(json.dumps( resp.get('previousEmployments'))).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             str(json.dumps( resp.get('disclosures'))).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
#             self.scrape_id
# 
#             )
#         
#         self.o.write(sql_statement+';\n')
#         self.o.flush()
        #print (sql_statement)

        #self.cursor1.execute(sql_statement)
        #self.db1.commit()
        #db.close()
        
#         ce_num = 1
#         for ce in resp['currentEmployments']:
#             item['currentEmployments_{}_firmId'.format(str(ce_num))] = ce.get('firmId','')
#             item['currentEmployments_{}_firmName'.format(str(ce_num))] = ce.get('firmName','')
#             item['currentEmployments_{}_iaOnly'.format(str(ce_num))] = ce.get('iaOnly','')
#             item['currentEmployments_{}_registrationBeginDate'.format(str(ce_num))] = ce.get('registrationBeginDate','')
#             item['currentEmployments_{}_firmBCScope'.format(str(ce_num))] = ce.get('firmBCScope','')
#             item['currentEmployments_{}_firmIAScope'.format(str(ce_num))] = ce.get('firmIAScope','')
#              
#             if ce.get('branchOfficeLocations'):
#                 branch_loc = ce['branchOfficeLocations'][0]
#                 item['currentEmployments_{}_street1'.format(str(ce_num))] = branch_loc.get('street1','')
#                 item['currentEmployments_{}_city'.format(str(ce_num))] = branch_loc.get('city','')
#                 item['currentEmployments_{}_cityAlias'.format(str(ce_num))] = ', '.join(branch_loc.get('cityAlias',''))
#                 item['currentEmployments_{}_state'.format(str(ce_num))] = branch_loc.get('state','')
#                 item['currentEmployments_{}_country'.format(str(ce_num))] = branch_loc.get('country','')
#                 item['currentEmployments_{}_zipCode'.format(str(ce_num))] = branch_loc.get('zipCode','')
#                 item['currentEmployments_{}_latitude'.format(str(ce_num))] = branch_loc.get('latitude','')
#                 item['currentEmployments_{}_longitude'.format(str(ce_num))] = branch_loc.get('longitude','')
#             ce_num+=1
             
             
#         pe_num = 1
#         for pe in resp['previousEmployments']:
#             item['previousEmployments_{}_firmId'.format(str(pe_num))] = pe.get('firmId','')
#             item['previousEmployments_{}_firmName'.format(str(pe_num))] = pe.get('firmName','')
#             item['previousEmployments_{}_street1'.format(str(pe_num))] = pe.get('street1','')
#             item['previousEmployments_{}_city'.format(str(pe_num))] = pe.get('city','')
#             item['previousEmployments_{}_state'.format(str(pe_num))] = pe.get('state','')
#             item['previousEmployments_{}_zipCode'.format(str(pe_num))] = pe.get('zipCode','')
#             item['previousEmployments_{}_registrationBeginDate'.format(str(pe_num))] = pe.get('registrationBeginDate','')
#             item['previousEmployments_{}_registrationEndDate'.format(str(pe_num))] = pe.get('registrationEndDate','')
#             item['previousEmployments_{}_firmBCScope'.format(str(pe_num))] = pe.get('firmBCScope','')
#             item['previousEmployments_{}_firmIAScope'.format(str(pe_num))] = pe.get('firmIAScope','')
#             pe_num+=1
         
         
        
#         dis_num = 1
#         if resp.get('disclosures'):
#             for dis in resp['disclosures']:
#                 item['disclosures_{}_eventDate'.format(str(dis_num))] = dis.get('eventDate','')
#                 item['disclosures_{}_disclosureType'.format(str(dis_num))] = dis.get('disclosureType','')
#                 item['disclosures_{}_disclosureResolution'.format(str(dis_num))] = dis.get('disclosureResolution','')
#                 item['disclosures_{}_disclosureDetail_Firm_Name'.format(str(dis_num))] = dis.get('disclosureDetail',{}).get('Firm Name','')
#                 item['disclosures_{}_disclosureDetail_Termination_Type'.format(str(dis_num))] = dis.get('disclosureDetail',{}).get('Termination Type','')
#                 item['disclosures_{}_disclosureDetail_DocketNumberFDA'.format(str(dis_num))] = dis.get('disclosureDetail',{}).get('DocketNumberFDA','')
#                 item['disclosures_{}_disclosureDetail_DocketNumberAAO'.format(str(dis_num))] = dis.get('disclosureDetail',{}).get('DocketNumberAAO','')
#                 item['disclosures_{}_disclosureDetail_Initiated_By'.format(str(dis_num))] = dis.get('disclosureDetail',{}).get('Initiated By','')
#                 item['disclosures_{}_disclosureDetail_Allegations'.format(str(dis_num))] = dis.get('disclosureDetail',{}).get('Allegations','')
#                 item['disclosures_{}_disclosureDetail_Resolution'.format(str(dis_num))] = dis.get('disclosureDetail',{}).get('Resolution','')
#                 item['disclosures_{}_disclosureDetail_Damage_Amount_Requested'.format(str(dis_num))] = dis.get('disclosureDetail',{}).get('Damage Amount Requested','')
#                 item['disclosures_{}_disclosureDetail_Settlement_Amount'.format(str(dis_num))] = dis.get('disclosureDetail',{}).get('Settlement Amount','')
#                 item['disclosures_{}_disclosureDetail_DisplayAAOLinkIfExists'.format(str(dis_num))] = dis.get('disclosureDetail',{}).get('DisplayAAOLinkIfExists','')
#                 item['disclosures_{}_disclosureDetail_arbitrationClaimFiledDetail'.format(str(dis_num))] = dis.get('disclosureDetail',{}).get('arbitrationClaimFiledDetail','')
#                 item['disclosures_{}_disclosureDetail_arbitrationDocketNumber'.format(str(dis_num))] = dis.get('disclosureDetail',{}).get('arbitrationDocketNumber','')
#                 item['disclosures_{}_disclosureDetail_Broker_Comment'.format(str(dis_num))] = dis.get('disclosureDetail',{}).get('Broker Comment','')
#                 
#                 sanc_num = 1
#                 if dis.get('disclosureDetail',{}).get('SanctionDetails'):
#                     for sanc in dis.get('disclosureDetail',{}).get('SanctionDetails'):
#                         item['disclosures_{}_disclosureDetail_SanctionDetails_{}_Sanctions'.format(str(dis_num), str(sanc_num))] = sanc.get('Sanctions','')
#                         item['disclosures_{}_disclosureDetail_SanctionDetails_{}_Registration_Capacities_Affected'.format(str(dis_num), str(sanc_num))] = sanc.get('SanctionDetails',[{}])[0].get('Registration Capacities Affected','')
#                         item['disclosures_{}_disclosureDetail_SanctionDetails_{}_Duration'.format(str(dis_num), str(sanc_num))] = sanc.get('SanctionDetails',[{}])[0].get('Duration','')
#                         item['disclosures_{}_disclosureDetail_SanctionDetails_{}_Start_Date'.format(str(dis_num), str(sanc_num))] = sanc.get('SanctionDetails',[{}])[0].get('Start Date','')
#                         item['disclosures_{}_disclosureDetail_SanctionDetails_{}_End_Date'.format(str(dis_num), str(sanc_num))] = sanc.get('SanctionDetails',[{}])[0].get('End Date','')
#                         item['disclosures_{}_disclosureDetail_SanctionDetails_{}_Amount'.format(str(dis_num), str(sanc_num))] = sanc.get('SanctionDetails',[{}])[0].get('Amount','')
#                 
#                         sanc_num+=1
#                 dis_num+=1
        
        #print (item)
        yield item
        
    