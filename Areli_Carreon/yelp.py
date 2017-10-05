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
output_file = open('yelp_output.txt','w')


for ll in input_file.split('\n'):

    lat =   str(ll.split(',')[0])
    long =  str(ll.split(',')[1])
    print (ll)
    offset = 0
    while True:
        querystring = {"term":"moving service companies","latitude":lat,"longitude":long,"offset":str(offset),"limit":"50"}
    
        headers = {'authorization': 'Bearer Pg3GkiiyQHRGyx9VaDjJ1zdLqo-gZDbDKvjGcFYrN-FEM0-x_j_w-rE1v1JqheL85OQW43aDQ63pkdWii2AI7Dweb1cS68Y8_Pa8Bz2X4VQnvk_zCDB_bV5xLMXEWXYx'}
    
        response = requests.request("GET", url, headers=headers, params=querystring)
        r = (response.json())
        print (r)
        try:
            businesses = r['businesses']
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
                                str(business['display_phone'])+'\n'
                                    )
                    output_file.flush()
                
            else:
                break
        except Exception as e:
            print (e)
            break
        offset += 50
            
            