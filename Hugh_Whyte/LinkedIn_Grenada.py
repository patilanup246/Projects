'''
Created on May 1, 2017

@author: Mukadam
'''
import requests
import urlparse, json, requests.packages.urllib3, urllib


requests.packages.urllib3.disable_warnings()
f= open('results.txt','w')
f2= open('parameters.txt','r').read()

cookie_value = f2.split('\n')[0].strip()
csrf_value = f2.split('\n')[1]
print cookie_value
print csrf_value

details = ''
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'host': "www.linkedin.com",
    'connection': "Keep-Alive",
    'x-udid': "b9ddf84b-8735-426c-bf9a-acda7b764726",
    'x-restli-protocol-version': "2.0.0",
    'accept-language': "en-US",
    'csrf-token': csrf_value,
    'x-li-page-instance': "urn:li:page:p_flagship3_search_srp_loading;dti5pBsmQoGpR5icx2evLw==",
    'x-li-track': "{\"osName\":\"Android OS\",\"osVersion\":\"6.0.1\",\"clientVersion\":\"4.1.9\",\"clientMinorVersion\":91700,\"model\":\"asus_ASUS_Z010D\",\"dpi\":\"xhdpi\",\"deviceType\":\"android\",\"appId\":\"com.linkedin.android\",\"deviceId\":\"b9ddf84b-8735-426c-bf9a-acda7b764726\",\"storeId\":\"us_googleplay\",\"isAdTrackingLimited\":false,\"mpName\":\"voyager-android\",\"mpVersion\":\"0.82.41\",\"timezoneOffset\":\"5\",\"clientTimestamp\":1487230373453}",
    'x-li-lang': "en_US",
    'cookie': cookie_value,
    'user-agent': "com.linkedin.android/91700 (Linux; U; Android 6.0.1; en_US; ASUS_Z010D; Build/MMB29P; Cronet/53.0.2782.3)",
    'accept-encoding': "gzip, deflate"
    }
    
url = "http://www.linkedin.com/voyager/api/search/hits"
urls_file = open('urls2.txt','r').read()
urls_to_scrap = urls_file.split('\n')
#print len(urls_to_scrap)
for url_to_scrap in urls_to_scrap:
#for h in xrange(1):
    print 'Scraping - '+url_to_scrap
    
    
    
    parsed = urlparse.urlparse(urllib.unquote(url_to_scrap).decode('utf8') )
#     facetGeoRegion = ''
#     facetIndustry = ''
#     keywords= 'Director'
#     facetCurrentCompany = '3830175|6322485|7980237|2846825|5493846|419520|1040655|10094778|1183735|6952657|1133104|8701055|4771665|7611621|2846233|6198582|1460797|6116579|1927914|6088185|7700103|8362193|8551468|6549071|319800|1433473|6053372|6325189|863168|4481838|2523406|15082215|10342484|1181224|714099|3048801|10861444|5477139|2995347|9047985'
#     facetNetwork = ''
    facetGeoRegion = ''
    facetIndustry = ''
    keywords= ''
    facetCurrentCompany = ''
    facetNetwork = ''
    try:
        a = eval(urlparse.parse_qs(parsed.query)['facetGeoRegion'][0])
        for t in a:
            facetGeoRegion+=t+'|'
         
        facetGeoRegion = facetGeoRegion[:-1]
        print 'facet geo '+facetGeoRegion
    except Exception,e:
        print 'facetGeoRegion error - '+str(e)
        pass
    #print facetGeoRegion
     
    try:
        a = eval(urlparse.parse_qs(parsed.query)['facetIndustry'][0])
        for t in a:
            facetIndustry+=t+','
         
        facetIndustry = facetIndustry[:-1]
        print facetIndustry
    except Exception,e:
        print 'facetIndustry error - '+str(e)
        pass
    print facetIndustry
     
    facetCurrentCompany = ''
    try:
        a = eval(urlparse.parse_qs(parsed.query)['facetCurrentCompany'][0])
        for t in a:
            facetCurrentCompany+=t+','
         
        facetCurrentCompany = facetCurrentCompany[:-1]
        print facetCurrentCompany
    except Exception,e:
        print 'facetCurrentCompany error - '+str(e)
        pass
     
     
    facetNetwork = ''
    try:
        a = eval(urlparse.parse_qs(parsed.query)['facetNetwork'][0])
        for t in a:
            facetNetwork+=t+'|'
         
        facetNetwork = facetNetwork[:-1]
        print 'facetNetwork '+facetNetwork
    except Exception,e:
        print 'facetNetwork error - '+str(e)
        pass
    #print facetGeoRegion
     
     
    try:
        keywords = urlparse.parse_qs(parsed.query)['keywords'][0]
    except Exception, e:
        #print e
        pass
    keywords = urllib.quote_plus(keywords)
    print keywords
    keywords = 'Title%3A%28Assistant%20Manager%29'
    #url_to_scrap = ('http://www.linkedin.com/voyager/api/search/hits?q=guided&searchId=975429921487170962447&origin=FACETED_SEARCH&timestamp=1487170962447&guides=List('+urllib.quote_plus('v->PEOPLE,facetNetwork->'+facetNetwork+',facetGeoRegion->'+facetGeoRegion+',facetCurrentCompany->'+facetCurrentCompany+',facetIndustry->'+facetIndustry)+')&keywords='+keywords+'&count=20&nc=1487170962448').replace('%2C', ',')
    url_to_scrap = ('http://www.linkedin.com/voyager/api/search/hits?q=guided&searchId=975429921487170962447&origin=FACETED_SEARCH&timestamp=1487170962447&guides=List('+urllib.quote_plus('v->PEOPLE,facetGeoRegion->'+facetGeoRegion)+')&keywords='+keywords+'&count=20&nc=1487170962448').replace('%2C', ',')
    print url_to_scrap
    #url_to_scrap = ('http://www.linkedin.com/voyager/api/search/hits?q=guided&origin=FACETED_SEARCH&guides=List('+urllib.quote_plus('v->PEOPLE,facetGeoRegion->'+facetGeoRegion)+')&count=20').replace('%2C', ',')
    #url_to_scrap = ('http://www.linkedin.com/voyager/api/search/hits?q=guided&searchId=975429921487170962447&origin=FACETED_SEARCH&timestamp=1487170962447&guides=List('+urllib.quote_plus('v->PEOPLE,facetNetwork->'+facetNetwork+',facetGeoRegion->'+facetGeoRegion)+')&keywords='+'AA'+'&count=20&nc=1487170962448').replace('%2C', ',')
    
    #print url_to_scrap
    
    #print url_to_scrap
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    try:
        
        i=0
        while True:
            #querystring = {"q":"guided","searchId":"1","origin":"FACETED_SEARCH","timestamp":"1","guides":"List(v->PEOPLE,facetNetwork->F,facetCurrentCompany->1009,facetGeoRegion->"+facetGeoRegion+",facetIndustry->"+facetIndustry+")","keywords":keywords,"start":str(i*20),"count":"20","nc":"1"}
            response = requests.request("GET", url_to_scrap+'&start='+str(i*20), headers=headers)
            #print url_to_scrap+'&start='+str(i*20)
            #print url_to_scrap+'&start='+str(i*20)
            #print str(json.loads(response.text)['total'])
            #print response.text
            try:
                print response.text
                whole_json = json.loads(response.text)
                j = whole_json['elements']
                
            except Exception,e:
                print 'breaking from loop (just for debugging)'
                break
            #print len(j)
            if (i*20) > whole_json['paging']['total']:
                #print 'breaking'
                break
            else:
                print ('Total is - '+str(whole_json['paging']['total']) + '  |  Currently running - '+str(i*20))
            
            for people in j:
                try:
                    try:
                        response_profile = requests.request("GET", 'https://www.linkedin.com/voyager/api/identity/profiles/'+people['hitInfo']['com.linkedin.voyager.search.SearchProfile']['miniProfile']['publicIdentifier']+'/positions', headers=headers)
                        #print response_profile.text
                        profile_details =  json.loads(response_profile.text)['elements'][0]
                    except Exception,e:
                        pass
                    try:
                        f.write(people['hitInfo']['com.linkedin.voyager.search.SearchProfile']['miniProfile']['firstName'].encode('utf-8').strip() + '\t')
                    except Exception,e:
                        f.write('\t')
                    try:
                        f.write(people['hitInfo']['com.linkedin.voyager.search.SearchProfile']['miniProfile']['lastName'].encode('utf-8').strip()+ '\t')
                    except Exception,e:
                        f.write('\t')
                    try:
                        f.write(people['hitInfo']['com.linkedin.voyager.search.SearchProfile']['industry'].encode('utf-8').strip()+  '\t')
                    except Exception,e:
                        f.write('\t')
                    try:
                        f.write(people['hitInfo']['com.linkedin.voyager.search.SearchProfile']['location'].encode('utf-8').strip()+ '\t')
                    except Exception,e:
                        f.write('\t')
                    try:
                        f.write('https://www.linkedin.com/in/'+people['hitInfo']['com.linkedin.voyager.search.SearchProfile']['miniProfile']['publicIdentifier'].encode('utf-8').strip()+'\t')
                    except Exception,e:
                        f.write('\t')
                    
                    try:
                        f.write(profile_details['companyName'].encode('utf-8').strip() +'\t'+profile_details['title'].encode('utf-8').strip()+'\t')
                    except Exception,e:
                        f.write('\t')
                        
                    try:
                        j = json.loads(requests.request("GET", 'https://www.linkedin.com/voyager/api/organization/companies/'+profile_details['companyUrn'].encode('utf-8').strip().replace('urn:li:fs_miniCompany:',''), headers=headers).text.encode('utf-8').strip())
                        #print j['companyPageUrl']
                        f.write(j['companyPageUrl']+'\n')
                    except Exception,e:
                        f.write('\n')
                    f.flush()
                    
                    
                except Exception,e:
                    #print e
                    pass
            i+=1
            
    
    except Exception,e:
        print response.text
        print 'total - '+str(e)
        pass



#file.write(details)
f.close()