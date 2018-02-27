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
    response = requests.request("GET", 'https://finovatespring2017.zerista.com/post?post_order=updated_asc&post_page='+str(i), headers=headers)
    print i
    i+=1
    if response.json():
        
            file_attendees_details.write(response.text.encode('ascii','ignore')+'\n')
            file_attendees_details.flush()
    else:
        break