import urllib,time

import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()
import uuid
requests.packages.urllib3.disable_warnings()

from threading import Thread
from Queue import Queue

requests.packages.urllib3.disable_warnings()
from stem import Signal
from stem.control import Controller

def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        #print 'a'
        controller.authenticate(password="muidsa1!2@")
        controller.signal(Signal.NEWNYM)


requests.packages.urllib3.disable_warnings()
headers = {
    'accept': "application/json, text/javascript, */*; q=0.01",
    'accept-encoding': "gzip, deflate, sdch, br",
    'accept-language': "en-US,en;q=0.8",
    'connection': "keep-alive",
    'host': "model.modelmydiet.com",
    'if-none-match': "W/\"1b3-5ZNHI5rmspEEOawKK64QDIyXUtw\"",
    'origin': "http://www.modelmydiet.com",
    'referer': "http://www.modelmydiet.com/men.html",
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
    'cache-control': "no-cache",
    'X-Ratelimit-Limit': '50',
    }

weights = ['80','100','120','140','160','180','200','220','240','260','280','300','320','340','360','380','400']
heights = ['59','64','68','74']
hair_colors = ['HC01','HC02','HC03','HC04','HC05','HC06']
races = ['CA01','LA01','AS01','BL01','CA02','BL02']
angles = ['front','back','right','left']
hair_styles = ['HS21','HS14','HS03','bald']
shapes = ['pear','hourglass']
busts = ['small','large']
i=1
api_key = ''
from datetime import datetime
datetime.now().strftime('%H:%M:%S')




# file_quotes = open('file_quotes_after.txt','w')
# for weight in weights:
#     for bust in busts:
#         for height in heights:
#             for hair_color in hair_colors:
#                 for race in races:
#                     for angle in angles:
#                         for hair_style in hair_styles:
#                             for shape in shapes:
#                                 
#                                 
#                                 print i
#                                 i+=1
#                                 try:
#                                     #quoted = urllib.quote('{"units":"imperial","height":"'+height+'","shape":'+shapes+',"bust":'+bust+',"visual_adjustment":"1","ethnicity":'+race+',"age":"AG20","eyes":"EYR","nose":"NOS","lips":"LPB","hair_color":'+hair_color+',"hair_style":'+hair_style+',"background":"blank","view":"front","delta":{"current":{"weight":'+weight+',"outfit":"undergarment"},"goal":{"weight":"120","outfit":"undergarment"}},"face":"disabled","id":"ea6341c4-15d9-4dff-8a8c-469281add122","":"1"}')
#                                     #resp = requests.get('https://model.modelmydiet.com/women?json=' + quoted,headers=headers)
#                                     file_quotes.write(str('before_'+hair_color+'_'+hair_style+'_'+race+'_'+height+'_'+weight+'_'+angle+'_'+shape+'_'+bust+'\t'))
#                                     file_quotes.write(str('{"units":"imperial","height":"'+height+'","shape":"'+shape+'","bust":"'+bust+'","visual_adjustment":"1","ethnicity":"'+race+'","age":"AG20","eyes":"EYR","nose":"NOS","lips":"LPB","hair_color":"'+hair_color+'","hair_style":"'+hair_style+'","background":"blank","view":"'+angle+'","delta":{"current":{"weight":"'+weight+'","outfit":"undergarment"},"goal":{"weight":"120","outfit":"undergarment"}},"face":"disabled","id":"ea6341c4-15d9-4dff-8a8c-469281add122","":"1"}'+'\n'))
#                                     
#                                     
# #                                     j= ''
# #                                     f_mmd.write(
# #                                         'before_' + j['hair_color'] + '_' + j['hair_style'] + '_' + j['ethnicity'] + '_' + j[
# #                                             'height'] + '_' + j['delta']['current']['weight'] + '_' + j['view'] + '_' +
# #                                         j['delta']['current']['shape'] + '\t\t' + json.loads(resp.text)['current'] + '\n')
#                                     file_quotes.flush()
#                                     #resp.close()
#                                 except Exception,e:
#                                     print e

urls = open('file_quotes_after.txt','r').read().split('\n')
file_after_women = open('file_after_women.txt','w')



def worker(q):
    while not q.empty():    
        try: 
            item = q.get()

            #print item.split('\t')[1]
            quoted_st = urllib.quote(item.split('\t')[1])
            resp = requests.get('https://model.modelmydiet.com/women?json=' + quoted_st,headers=headers,verify=False
                                    ,proxies=dict(http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050')
                                    )
            print resp.text
            #print 'X-Ratelimit-Remaining - '+str(resp.headers)
            
            #print quoted_st
            
            #print resp.json()
            file_after_women.write(str(item.split('\t')[0])+'\t'+str(resp.json()['current'])+'\n')
            file_after_women.flush()
        except Exception,e:
            #print resp.text
            print e
            pass

q = Queue()
map(q.put, urls)
 
startime = time.time()
#renew_connection()
for i in range(4):
    #print i
    t = Thread(target=worker, args=(q, ))
    t.start()
    
while True:
    renew_connection()
    print 'resetting '
    time.sleep(10)
#q.join()
endtime = time.time()
print endtime-startime

