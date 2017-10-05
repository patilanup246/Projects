import urllib
import json, time
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from pyquery import PyQuery
from requests_futures.sessions import FuturesSession
session = FuturesSession()
headers = {
    'accept-encoding': "gzip, deflate",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'content-length': "216",
    'content-type': "application/x-www-form-urlencoded",
    'cookie': "__utmli=new_user",
    'host': "developer.modelmydiet.com",
    'origin': "http://developer.modelmydiet.com",
    'referer': "http://developer.modelmydiet.com/signup",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    }
headers2 = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "en-US,en;q=0.8",
    'connection': "keep-alive",
    'host': "sandbox.modelmydiet.com",
    'if-none-match': "W/\"1e1-sQF1BfC0pltfT2n4oM4eL2BIKFk\"",
    'origin': "http://www.modelmydiet.com",
    'referer': "http://www.modelmydiet.com/men.html",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    'cache-control': "no-cache",
    'content-type': "application/x-www-form-urlencoded"
    }
weights = ['80','100','120','140','160','180','200','220','240','260','280','300','320','340','360','380','400']
heights = ['59','64','68','74']
hair_colors = ['HC01','HC02','HC03','HC04','HC05','HC06']
races = ['CA01','LA01','AS01','BL01']
angles = ['front','back','right','left']
hair_styles = ['HS31','HS32','HS33','HS34','HS35','HS36','HS37','HS38','HS39','HS40','HS41','HS42']
shapes = ['muscular','regular']
belly = 'flat'
i=1
api_key = ''
from datetime import datetime
datetime.now().strftime('%H:%M:%S')
f_mmd = open('mmd.txt','w')
for weight in weights:
    for height in heights:
        for hair_color in hair_colors:
            for race in races:
                for angle in angles:
                    for hair_style in hair_styles:
                        for shape in shapes:
    
    
                            print i
                            i+=1
                            try:
                                quoted = urllib.quote(
                                    '{"api_key": "' + api_key + '","units":"imperial","height":"' + height + '","belly":"' + belly + '","ethnicity":"' + race + '","age":"AG40","eyes":"EYR","nose":"NOS","lips":"LPB","beard_style":"BS04","beard_color":"BC06","hair_color":"' + hair_color + '","hair_style":"' + hair_style + '","background":"blank","view":"' + angle + '","delta":{"current":{"weight":"' + weight + '","shape":"' + shape + '","outfit":"undergarment"},"goal":{"weight":"190","shape":"muscular","outfit":"undergarment"}}}')
                                future = session.get('http://sandbox.modelmydiet.com/men?json=' + quoted,headers=headers2)
                                resp = future.result()
                                #resp = requests.request('GET', 'http://sandbox.modelmydiet.com/men?json=' + quoted)
                                print resp.text
                                json.loads(resp.text)['current']
                                j = json.loads(urllib.unquote(resp.url.replace('http://sandbox.modelmydiet.com/men?json=', '')))
    
                                f_mmd.write(
                                    'after_' + j['hair_color'] + '_' + j['hair_style'] + '_' + j['ethnicity'] + '_' + j[
                                        'height'] + '_' + j['delta']['current']['weight'] + '_' + j['view'] + '_' +
                                    j['delta']['current']['shape'] + '\t\t' + json.loads(resp.text)['current'] + '\n')
                                f_mmd.flush()
                                resp.close()
                            except Exception,e:
                                print e
    
    
