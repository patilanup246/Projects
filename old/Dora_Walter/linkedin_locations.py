import requests

url = "https://www.linkedin.com/sales/search/results/companies"



headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache",
    'cookie': "bcookie=\"v=2&c08f52ef-f4e2-4fce-89e5-9c43955f8071\"; bscookie=\"v=1&20170521043018b70a9bbe-8b2e-4691-826c-0d2768393ec9AQH6y-5f0Y9YsV8Tg5WaIGMkiiCwC34O\"; visit=\"v=1&M\"; sl=\"v=1&sP6UJ\"; liap=true; li_at=AQEDAQXQY1AERRdZAAABX7s-P1cAAAFf30rDV1EAdEG2gdwDA5CRplnNd5RPvlvPVSf5h3VbwV_i7OwivKI6y5Ks0Qp2YOyoSFT21rBK8IJ6zOtWCHeY7ZjKReHc9yM9bkZdssBVEwLZGJfz1Vp3yC5f; JSESSIONID=\"ajax:2345760577114445451\"; _lipt=CwEAAAFf2eCHPSud_DVUX6VNyXVixAZ_aACrZtuhvRg3P0rcPmiMQsZSeBC-3cIguVfzvqeKgPvq_D0F5rBoD9nftQOdiZz_YMDcRoRwr35rCWMLfx47zsDJBB18UeyAc8FQbafXzKIgHqu2GlxizdoYQovumumsgOIKKoz5XXlvQTqXT6BbRYliPOcmPEO37RQ4sYhstcYVSCYuF892d_CnOkjZvY5JkEzL7S_kgS7qkymI2dLMDdlzZQ1g5KZy4vB0p1ZvRP9veG5BLgU_rn95td3st4cHf_UR0_jIPZt1J-xZO28L18FUhCijyEb70Jmo1DK827w-vs2MsCXbLQARZx0M2pZZOprNLtqKtIqEiaVpp02rJIQGXUTsKEeMoN2QVsuEjW_Jg7tCbuknYcb8GvXqSTOVya73-vxsZdB48j_ABLTUeU8PeOoLpfyBmwKzMOCdAl5oL7mwQ_yGmGwV7u2IP2mqHBfrzGAPhIijtUoGV7_mNLFqoQjkcxOx7A6TZ_1dag5k6agKY9q_OCwP-Mw-vv0; ELOQUA=GUID=71FCF295D13B445AAEE24EDB9E32E4B2; lidc=\"b=SB92:g=54:u=284:i=1511190703:t=1511244739:s=AQHVVIyp3iX1xQbLZGOGU2QFYSWr7_F-\"; _ga=GA1.2.690901640.1495374784; li_a=AQJ2PTEmc2FsZXNfY2lkPTI4ODM2OTAwMiUzQSUzQTk0MDg0NTAy5s1lzYtPz7irFcT5eYY87LJIr48; lang=\"v=2&lang=en-us\"; sdsc=22%3A1%2C1511191639596%7ECAOR%2C0L94qFDjexfHW29Hi3eSQNzlS5Ks%3D",
    'pragma': "no-cache",
    'referer': "https://www.linkedin.com/sales/search/companies?geoScope=BY_REGION&facet=CCR&facet=I&facet=CS&facet.I=80&facet.CS=D&REV=USD&count=25&start=0&trackingInfoJson.contextId=3F5B86740AD5F81440EB94509C2B0000",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    'x-li-identity': "dXJuOmxpOm1lbWJlcjo5NzU0Mjk5Mg",
    'x-requested-with': "XMLHttpRequest"
    }


output_f =  open('output_f','w')
#print(response.text)
#for i in ['al','ak','az','ar','ca','co','ct','de','fl','ga','hi','id','il','in','ia','ks','ky','la','me','md','ma','mi','mn','ms','mo','mt','ne','nv','nh','nj','nm','ny','nc','nd','oh','ok','or','pa','ri','sc','sd','tn','tx','ut','vt','va','wa','wv','wi','wy']:
for i in ['tx','ny','il','fl','ca']:
#     for j in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
#     
    querystring = {"geoScope":"BY_REGION","facet":["CCR","I","CS"],"facet.CCR":"us:{}".format(i),"facet.I":"80","facet.CS":"C","REV":"USD","count":"1000","start":"0"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print (str(i) + '-- '+ str(len(response.json()['searchResults'])))
    for j in response.json()['searchResults']:
        location = ''
        try:
            location = j['location']
        except Exception as e:
            #print e
            pass
        try:
            output_f.write (str(j['companyId'])+'\t'+
                        str(j['name'])+'\t'+
                        str(location)+'\t'+
                        str(j['size'])+ '\t'+str(i)+'\n')
            output_f.flush()
        except Exception as e:
            #print e
            pass