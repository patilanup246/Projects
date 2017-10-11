import requests
from time import gmtime, strftime
import os
site_name = 'coopisrael'+'_'+strftime("%Y-%m-%d%H-%M-%S", gmtime())

try:
    os.makedirs(site_name)
except:
    pass

url = "http://coopisrael.coop/home/get_prices"


headers = {
    'origin': "http://coopisrael.coop",
    'upgrade-insecure-requests': "1",
    'content-type': "application/x-www-form-urlencoded",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.45 Safari/537.36",
    'x-devtools-emulate-network-conditions-client-id': "041c1a04-32bc-44b4-9c97-27e9b778b349",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "http://coopisrael.coop/home/prices",
    'accept-encoding': "gzip, deflate",
    'accept-language': "en-US,en;q=0.9",
    }

for i in range(1,100):
    print (i)
    payload = "agree=1&branch="+str(i)+"&product=0&type=0"
    response = requests.request("POST", url, data=payload, headers=headers)
    
    with open(site_name+'/'+'coopisrael'+str(i)+'.xls', 'wb') as f:
        f.write(response.content)


