'''
Created on May 18, 2017

@author: Mukadam
'''
import requests,sys

#for attendess
# url = "https://finovatespring2017.zerista.com/user"
# file_attendees_details = open('file_attendees_details.txt','w')
# querystring = {"user_order":"updated_asc","user_page":"1"}


url = "http://finovatespring2017.zerista.com/exhibitor"
file_attendees_details = open('file_exhibitors_details.txt','w')
querystring = {"exhibitor_order":"updated_asc","exhibitor_page":"1"}



headers = {
    'x-zerista-auth-token': "FfVUXxopHQrVpZXEsClg3qZ75QslntCi",
    'accept-language': "en",
    'user-agent': "Zerista (Android 6.0) com.zerista.finovateeurope2017/1200 (12.00)",
    'accept': "application/json;version=8",
    'host': "finovatespring2017.zerista.com",
    'connection': "Keep-Alive",
    'accept-encoding': "gzip",
    'cache-control': "no-cache"
    }
i=1
while True:
    response = requests.request("GET", 'https://finovatespring2017.zerista.com/user?user_order=updated_asc&user_page='+str(i), headers=headers)
    print i
    i+=1
    if response.json():
        #print response.text.encode('ascii','ignore')
        #sys.exit()
        for profile in response.json():
            details = ''
            details+= str(profile['id'])+'\t'
            
            #resp_profile = requests.get('https://finovatespring2017.zerista.com/user/member/'+str(profile['id'])).json()
            
            
            
            
            
            
            try:
                details+= profile['first_name']
            except Exception,e:
                pass
            details+='\t'   
            try:
                details+= profile['last_name']
            except Exception,e:
                pass
            details+='\t'
            try:
                details+= profile['employee']['position']
            except Exception,e:
                pass
            details+='\t'
            try:
                details+= profile['employee']['organization']
            except Exception,e:
                pass
            details+='\t'
            try:
                details+= profile['web_links']['linkedin']
            except Exception,e:
                pass
            details+='\t'
            try:
                details+= profile['content'].encode('ascii','ignore').replace('\n','').replace('\r','')
            except Exception,e:
                pass
            file_attendees_details.write(details.encode('ascii','ignore')+'\n')
            file_attendees_details.flush()
    else:
        break