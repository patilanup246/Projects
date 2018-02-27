# -*- coding: utf-8 -*-
'''
Created on 20-Oct-2017

@author: Administrator
'''
'''
Created on 23-Sep-2017

@author: Administrator
'''
import requests
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
url = "https://api.yelp.com/v3/businesses/search"


input_file  = open('lat_lon.txt').read()
output_file = open('yelp_output.txt','w',encoding='utf-8')


for ll in input_file.split('\n'):

    #lat =   str(ll.split(',')[0])
    #long =  str(ll.split(',')[1])
    print ('\n'+ll)
    offset = 0
    while True:
        #querystring = {"location":10029,"offset":str(offset),"limit":"50"}
        #querystring = {"latitude":lat,"longitude":long,"offset":str(offset),"limit":"50","categories":"gyms"}
        querystring = {"radius":"3218","location":ll,"offset":str(offset),"limit":"50","categories":"fitness"}
        #TALIB_ACCESS_TOKEN = Pg3GkiiyQHRGyx9VaDjJ1zdLqo-gZDbDKvjGcFYrN-FEM0-x_j_w-rE1v1JqheL85OQW43aDQ63pkdWii2AI7Dweb1cS68Y8_Pa8Bz2X4VQnvk_zCDB_bV5xLMXEWXYx
        #TASNEEM _ACCESS_TOKEN = WEGE2Pfl6iFGAmdk-vYRzjwJARD_jVnY6AJ2puozjjYL767W6_ilh7fy9aNLORKRuxzHD2Yw72lSCzjTTJ-KWqsRS3OuLEfcgzFHPmpZo9gqLqeyDQEqOrXi6fPqWXYx
        headers = {'authorization': 'Bearer WEGE2Pfl6iFGAmdk-vYRzjwJARD_jVnY6AJ2puozjjYL767W6_ilh7fy9aNLORKRuxzHD2Yw72lSCzjTTJ-KWqsRS3OuLEfcgzFHPmpZo9gqLqeyDQEqOrXi6fPqWXYx'}
    
        response = requests.request("GET", url, headers=headers, params=querystring)
        r = (response.json())
        #print ('\n'+ll)
        try:
            businesses = r['businesses']
            print (len(businesses))
            if businesses:
                for business in businesses:
                    output_file.write(
                                str(business['id'])+'\t'+
                                str(business['name'])+'\t'+
                                str(business['url'])+'\t'+
                                str(business['review_count'])+'\t'+
                                str(business['rating'])+'\t'+
                                str(business['location']['address1'])+'\t'+
                                str(business['location']['address2'])+'\t'+
                                str(business['location']['address3'])+'\t'+
                                str(business['location']['city'])+'\t'+
                                str(business['location']['zip_code'])+'\t'+
                                str(business['location']['country'])+'\t'+
                                str(business['location']['state'])+'\t'+
                                str(business['phone'])+'\t'+
                                str(business['display_phone'])+'\t'+
                                str(ll)+'\n'
                                )
                    output_file.flush()
                
            else:
                break
        except Exception as e:
            print (e)
            break
        offset += 50
