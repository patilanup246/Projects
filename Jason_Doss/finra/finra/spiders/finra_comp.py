# -*- coding: utf-8 -*-
from finra.items import Website
import scrapy
import json
import requests
import psycopg2
class finra(scrapy.Spider):
    name="finra_firms"
    all_urls = []
    scraped_country = ''
    
    DB_ADDRESS = "brokercheck.c3l9vpoajvgp.us-east-2.rds.amazonaws.com"
    DB_USER = "jasondoss"
    DB_PASS = "jasondoss1!"
    DB_NAME = "brokercheck"
    scrape_id = 1

    
    def __init__(self, country = '', *args,**kwargs):
        
        db = psycopg2.connect(host=self.DB_ADDRESS,user=self.DB_USER,password=self.DB_PASS,database=self.DB_NAME )
        print ('started')
        cursor = db.cursor()
        cur1 = cursor.execute("SELECT scrape_id from firm_scrape_id ORDER BY scrape_id DESC LIMIT 1")
        data = cursor.fetchall()
        
         
        if len(data) == 0 :
            exists = False
        else:
            self.scrape_id = int(data[0][0]) + 1
         
        cursor.execute('INSERT INTO firm_scrape_id (scrape_id) VALUES ({})'.format(self.scrape_id))
        db.commit()
        db.close()
        
        
        
        
        
        states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
        #states = []
        for s in states:
            start = 0
            while True:
                r = requests.get('http://doppler.finra.org/doppler-lookup/api/v1/search/firms?hl=true&nrows=24&r=25&sort=score+desc&start={}&state={}&wt=json'.format(str(start),s)).json()
                 
                if not r['results']['BROKER_CHECK_FIRM']['results']:
                    break
                else:
                    for p in r['results']['BROKER_CHECK_FIRM']['results']:
                        self.all_urls.append (p['fields']['bc_source_id'])
                 
                start+=24
                 
                print(s+' -- \t -- '+str(start))
        
        

    def start_requests(self):
        for url in self.all_urls:
            yield scrapy.Request(url='http://doppler.finra.org/doppler-lookup/api/v1/search/firms/{}/?wt=json'.format(str(url)), callback=self.parse)
    

    
    
    def parse(self, response):
        item = Website()
        
        resp = json.loads(json.loads(response.body_as_unicode())['results']['BROKER_CHECK_FIRM']['results'][0]['fields']['content_json'][0])
        
        item['firmId'] = resp.get('basicInformation',{}).get('firmId','')
        item['firmName'] = resp.get('basicInformation',{}).get('firmName','')
        item['secNumber'] = resp.get('basicInformation',{}).get('secNumber','')
        item['isLegacy'] = resp.get('basicInformation',{}).get('isLegacy','')
        item['otherNames'] = '$SEP$'.join(resp.get('basicInformation',{}).get('otherNames',''))
        item['bcScope'] = resp.get('basicInformation',{}).get('bcScope','')
        
        item['finraRegistered'] = resp.get('basicInformation',{}).get('finraRegistered','')
        item['districtName'] = resp.get('basicInformation',{}).get('districtName','')
        item['firmType'] = resp.get('basicInformation',{}).get('firmType','')
        item['formedState'] = resp.get('basicInformation',{}).get('formedState','')
        
        
        
        item['firmSize'] = resp.get('basicInformation',{}).get('firmSize','')
        item['formedDate'] = resp.get('basicInformation',{}).get('formedDate','')
        item['fiscalMonthEndCode'] = resp.get('basicInformation',{}).get('fiscalMonthEndCode','')
        item['legacyReportStatus'] = resp.get('basicInformation',{}).get('legacyReportStatus','')
        
        
        if resp.get('branchOfficeLocations',[]):
            bolarray = []
            for bol in resp.get('branchOfficeLocations'):
                bolarray.append(bol.get('street1','')+', '+bol.get('street2','')+', '+bol.get('city','')+', '+bol.get('state','')+', '+bol.get('zipCode',''))
            
            item['branchOfficeLocations'] = json.dumps('$SEP$'.join(bolarray))
        

        
        
        
        if resp.get('firmAddressDetails'):
            if resp.get('officeAddress'):
                oa = resp.get('officeAddress')
                
                item['officeAddress_street1'] = oa.get('street1','')
                item['officeAddress_city'] = oa.get('city','')
                item['officeAddress_state'] = oa.get('state','')
                item['officeAddress_country'] = oa.get('country','')
                item['officeAddress_postalCode'] = oa.get('postalCode','')
                
                
            if resp.get('mailingAddress'):
                ma = resp.get('mailingAddress')
                
                item['mailingAddress_street1'] = ma.get('street1','')
                item['mailingAddress_city'] = ma.get('city','')
                item['mailingAddress_state'] = ma.get('state','')
                item['mailingAddress_country'] = ma.get('country','')
                item['mailingAddress_postalCode'] = ma.get('postalCode','')
                
            item['businessPhoneNumber'] = resp.get('firmAddressDetails').get('businessPhoneNumber','')
        
        item['bdDisclosureFlag']    = resp.get('bdDisclosureFlag','')
        
        item['disclosures']         = json.dumps(resp.get('disclosures',[]))
        
        
        if resp.get('registrations'):
            item['approvedFinraRegistrationCount'] = resp.get('registrations').get('approvedFinraRegistrationCount')
            item['approvedSECRegistrationCount'] = resp.get('registrations').get('approvedSECRegistrationCount')
            item['approvedSRORegistrationCount'] = resp.get('registrations').get('approvedSRORegistrationCount')
            item['approvedStateRegistrationCount'] = resp.get('registrations').get('approvedStateRegistrationCount')
            item['businessTypeCount'] = resp.get('registrations').get('businessTypeCount')
            item['hasAffliation'] = resp.get('registrations').get('hasAffliation')
            item['referOtherBd'] = resp.get('registrations').get('referOtherBd')
            
            sts = []
            for s in resp.get('registrations').get('stateList'):
                sts.append(s.get('state'))
            
            item['registrations_states'] = '$SEP$'.join(sts)
        
        
        item['directOwners']        = json.dumps(resp.get('directOwners',[]))
        print ()
        sql_statement = '''INSERT INTO finra_firms ("firmId", "firmName", "secNumber", "isLegacy", "otherNames", "bcScope", "finraRegistered", "districtName", "firmType", "formedState", "firmSize", "formedDate", "fiscalMonthEndCode", "legacyReportStatus", "branchOfficeLocations", "firmAddressDetails", "bdDisclosureFlag", "disclosures", "registrations", "directOwners", "scrapeID") VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{})'''.format(
            str( resp.get('basicInformation',{}).get('firmId','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( resp.get('basicInformation',{}).get('firmName','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( resp.get('basicInformation',{}).get('secNumber','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( resp.get('basicInformation',{}).get('isLegacy','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            
            str( '$SEP$'.join([x.encode('ascii', 'ignore').decode('ascii') for x in resp.get('basicInformation',{}).get('otherNames','')])).replace("'","''"),
            str( resp.get('basicInformation',{}).get('bcScope','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( resp.get('basicInformation',{}).get('finraRegistered','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( resp.get('basicInformation',{}).get('districtName','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( resp.get('basicInformation',{}).get('firmType','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( resp.get('basicInformation',{}).get('formedState','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( resp.get('basicInformation',{}).get('firmSize','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( resp.get('basicInformation',{}).get('formedDate','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( resp.get('basicInformation',{}).get('fiscalMonthEndCode','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( resp.get('basicInformation',{}).get('legacyReportStatus','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str(json.dumps(resp.get('branchOfficeLocations',[])[:10])).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str(json.dumps(resp.get('firmAddressDetails'))).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( resp.get('bdDisclosureFlag','')).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( json.dumps(resp.get('disclosures',[]))).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str(json.dumps(resp.get('registrations'))).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            str( json.dumps(resp.get('directOwners',[]))).encode('ascii', 'ignore').decode('ascii').replace("'","''"),
            self.scrape_id
            
            )
        print (sql_statement)
        db = psycopg2.connect(host=self.DB_ADDRESS,user=self.DB_USER,password=self.DB_PASS,database=self.DB_NAME )
        cursor = db.cursor()
        cursor.execute(sql_statement)
        db.commit()
        db.close()
        
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
        
        
        yield item
        

    