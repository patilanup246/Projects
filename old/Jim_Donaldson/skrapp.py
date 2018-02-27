import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#1864200848IDmEGwL2cSTRwd8BawUZ7qfMRelI0GOI
ema = [
'firstName=Eric&lastName=Windeknecht&domain=nidec.com',
'firstName=William&lastName=Walls&domain=zurn.com',
'firstName=Rick&lastName=Anderson&domain=zurn.com',
'firstName=Joy&lastName=Dascalakis&domain=zurn.com',
'firstName=Roy&lastName=Horton&domain=zurn.com',
'firstName=Andy&lastName=Turnbull&domain=zurn.com',

]

url = "https://skrappapi-hello123541.rhcloud.com/api/v2/find"

querystring = {"firstName":"Ali","lastName":"Masoudi","domain":"usbcsd.org","context":"profile","liv":"nli"}

headers = {
    'host': "skrappapi-hello123541.rhcloud.com",
    'connection': "keep-alive",
    'accept': "*/*",
    'origin': "chrome-extension://gklkbifnmojjpmbkojffeamiblineife",
    'x-access-key': "555990200SMUSVx5pRjP2rU34Lyzif6zhIQvJBIqde",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36",
    'referer': "https://www.linkedin.com/in/alimasoudi83/",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache"
    }
for u in ema:
    url = 'https://skrappapi-hello123541.rhcloud.com/api/v2/find?'+u+'&context=profile&liv=nli'
    response = requests.request("GET", url, headers=headers,verify=False)

    try:
        print(response.json()['email'])
    except:
        print (response.json())