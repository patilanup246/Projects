import requests
from pygame import mixer # Load the required library
from datetime import datetime
import time

url = "https://www.upwork.com/api/mc/v2/trays/rangwala_tasneem/notifications/contents.json"
url_unread_count = 'https://www.upwork.com/api/v3/notification-feed/notifications/unreadCount'
headers = {
    'accept': "application/json, text/plain, */*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'authorization': "Bearer oauth2v1_1dfa51c65e3af1316163d894dcbe5538",
    #'cookie': "__cfduid=d8badb8d1a25b80a50fe7cebb6915f58f1499616192; device_view=full; console_user=rangwala_tasneem; recognized=1; master_access_token=01471091.oauth2v1_ec8c5729b192a210f5276356f913f3dd; oauth2_global_js_token=oauth2v1_1dfa51c65e3af1316163d894dcbe5538; dash_company_last_accessed=705290620522987521; optimizelySegments=%7B%222772971468%22%3A%22false%22%2C%222800491501%22%3A%22gc%22%2C%222801081125%22%3A%22direct%22%2C%222806681009%22%3A%22none%22%2C%222877800604%22%3A%22true%22%7D; optimizelyEndUserId=oeu1499616631565r0.2750212543708188; optimizelyBuckets=%7B%7D; last_accessed_app=dash; _ga=GA1.2.2104878895.1499616206; _gid=GA1.2.467494506.1499616206; XSRF-TOKEN=0b66b4cd91ade53a2e6a97cdd5b88719; visitor_id=103.207.10.146.1499616192364034; current_organization_uid=705290620522987521; qt_visitor_id=49.202.56.431456989363959580; mc_unread.rangwala_tasneem=%7B%22trays%22%3A%7B%22notifications%22%3A0%2C%22disputes%22%3A0%7D%7D; _px3=e30e20cfa8622d5d59892791a23fdac93c4cf9ae7ace606a4429c83c91848ba3:lAiYMQ2qqCP260qEzbzj/JmP4tyITCENNoDoT6RjDGPcf0KXiOg+WuNKmMjSx2Dvg+vinCwmnqbK/a5jo7woaw==:1000:UMloBb+ESm7LnYySl9z7fbrToXc4ng7roLCVolQNJ7ffPlvufAXDFxR2cRnG/Nue5qjeWjn5zPNo+pDS0vlqgO2shiQqfSYhDIBShW7Rf/DOnwoBJgl2k5D5F+EqpeXycYd6ExcfUDipbNPspTMwHTlp2yURsNjkRt5EPbdwVDw=; session_id=ced70ca98feccb85faf2e96aef6a3958; company_last_accessed=d10826077",
    'referer': "https://www.upwork.com/my-stats/",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
    'cache-control': "no-cache"
    }

def check_notif():
    # response = requests.request("GET", url, headers=headers)
    # response = response.json()
    # notif = False
    # for u_thread in response['trays'][0]['threads']:
    #     if u_thread['read'] == 'f':
    #         print u_thread['subject']
    #         notif = True
    #         break


    response = requests.request("GET", url_unread_count, headers=headers)

    #print response.text
    response = response.json()
    notif = False
    if response['unreadCount'] >  0:
        notif = True


    if notif:
        mixer.init()
        mixer.music.load('C:\Users\Public\Music\Sample Music\Kalimba.mp3')
        mixer.music.play()
        time.sleep(50)

    if not notif:
        print 'No notifications at '+str(datetime.now())


while True:
    check_notif()
    time.sleep(100)