'''
Created on Apr 21, 2018

@author: talib
'''
import requests
import csv

output_f = open('Scott_2018.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)

wr.writerow(['First Name','Last Name','Job Title','Organisation Name', 'Address', 'Address 2', 'City', 'State', 'Country', 'Zipcode','bio','email','facebook_url','linkedin_url','phone_mobile','phone_work','phone_other','phone_other_type','twitter_url','website','website 2'])
id1 = 'dL2PMIzA75'
min1 = 1

while True:

    r = requests.get('https://attendeedirectory.crowdcompass.com/attendee_directory/{}/sync?min={}&max={}'.format(id1,str(min1),str(min1+499)),verify=False).json()

    
    if not r['attendees']:
        break
    
    for p in r['attendees']:
        details = []
        if p.get('profile').get('first_name',''):
            details.append (p.get('profile').get('first_name',''))
            details.append (p.get('profile').get('last_name',''))
            details.append (p.get('profile').get('job_title',''))
            details.append (p.get('profile').get('organization_name',''))
            address1 = p.get('profile').get('address')
            if address1:
                details.append (address1.get('address'))
                details.append (address1.get('address_2'))
                details.append (address1.get('city'))
                details.append (address1.get('state'))
                details.append (address1.get('country'))
                details.append (address1.get('zipcode'))
            else:
                details.append ('')
                details.append ('')
                details.append ('')
                details.append ('')
                details.append ('')
                details.append ('')
            details.append (p.get('profile').get('bio',''))
            details.append (p.get('profile').get('email',''))
            details.append (p.get('profile').get('facebook_url',''))
            details.append (p.get('profile').get('linkedin_url',''))
            details.append (p.get('profile').get('phone_mobile',''))
            details.append (p.get('profile').get('phone_work',''))
            details.append (p.get('profile').get('phone_other',''))
            details.append (p.get('profile').get('phone_other_type',''))
            details.append (p.get('profile').get('twitter_url',''))
            details.append (p.get('profile').get('website',''))
            details.append (p.get('profile').get('website_2',''))
    
            wr.writerow(details)
            try:
                print (details)
            except:
                pass
    min1+=500
    
    print (min1)