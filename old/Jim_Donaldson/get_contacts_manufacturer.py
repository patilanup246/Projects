import requests
import re
url = "https://www.linkedin.com/voyager/api/search/cluster"

querystring = {"count":"10","guides":"List(v->PEOPLE,facetGeoRegion->us:0,title->\"Vice President of Operations\" OR \"Director of Operations\" OR \"Vice President of Manufacturing\" OR \"Director of Manufacturing\" OR \"Vice President of Manufacturing Engineering\" OR \"Director of Manufacturing Engineering\" OR \"Vice President of Production\" OR \"Director of Production\" OR \"Vice President of Logistics\" OR \"Director of Logistics\" OR \"Vice President of Quality\" OR \"Director of Quality\" OR \"Vice President of Plant Operations\" OR \"Director of Plant Operations\" OR \"Vice President of Good Movement\" OR \"Director of Good Movement\" OR \"Vice President of Non Conforming Materials\" OR \"Director of Non Conforming Materials\" OR \"RFID\" OR \"Process Improvement\" OR \"Founder\" OR \"Co-Founder\",company->Maxim Integrated)","origin":"FACETED_SEARCH","q":"guided","start":"10"}

headers = {

    'cookie': "bcookie=\"v=2&7d34372d-be42-4b3b-86b3-f2c0d99bccd0\"; bscookie=\"v=1&201706271356155f29c45a-56f5-43a7-810e-c41320aa4b27AQHjbn8brLS93r41PhdUg6J7BX0l2OKB\"; visit=\"v=1&M\"; li_at=AQEDASI-xJgBUpw0AAABXYluA_kAAAFdjo4jeFYArlW6-0JdEXmkIqM1WCycqCn4teFPoJGnJ2xOdwbQxkQk6mUIS3h_t73bSUTlMmfRlmSEDm2Goebx1e483jsnGw5Ly8PUbCvQ2Z6u8VVVgLOpXi-1; liap=true; sl=\"v=1&MbX4q\"; JSESSIONID=\"ajax:0020470289555367885\"; lang=\"v=2&lang=en-us\"; sdsc=1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D; _ga=GA1.2.151815404.1498571786; lidc=\"b=OB04:g=442:u=15:i=1501315834:t=1501370034:s=AQGP4Mq2D8GKFHQ3odNdHCA5wS1ay_Oi\"; _lipt=CwEAAAFdjWjA5oiTAgeTh7mH6Q-TXweOC9TkD7mBela1x2bAiSowyXPzOAz9yl8CKDzF9oTfev672up-3Dk5ZmQ6PnUuTO8F9IXCzRZbk98FtiBULZaoYuq3dtjKxiESsqikXR_aswZpxdM09ldrxsELr5FgoAVuAW7E7OwiZhdetnS7nHHs8N-YGXC10SDHLQctjm-fxpMw7rUnyIcyofEljtY",
    'csrf-token': "ajax:0020470289555367885"

    }

response = requests.request("GET", 'https://www.linkedin.com/voyager/api/search/cluster?count=10&guides=List(v-%3EPEOPLE,facetGeoRegion-%3Eus%3A0,title-%3E%22Vice%20President%20of%20Operations%22%20OR%20%22Director%20of%20Operations%22%20OR%20%22Vice%20President%20of%20Manufacturing%22%20OR%20%22Director%20of%20Manufacturing%22%20OR%20%22Vice%20President%20of%20Manufacturing%20Engineering%22%20OR%20%22Director%20of%20Manufacturing%20Engineering%22%20OR%20%22Vice%20President%20of%20Production%22%20OR%20%22Director%20of%20Production%22%20OR%20%22Vice%20President%20of%20Logistics%22%20OR%20%22Director%20of%20Logistics%22%20OR%20%22Vice%20President%20of%20Quality%22%20OR%20%22Director%20of%20Quality%22%20OR%20%22Vice%20President%20of%20Plant%20Operations%22%20OR%20%22Director%20of%20Plant%20Operations%22%20OR%20%22Vice%20President%20of%20Good%20Movement%22%20OR%20%22Director%20of%20Good%20Movement%22%20OR%20%22Vice%20President%20of%20Non%20Conforming%20Materials%22%20OR%20%22Director%20of%20Non%20Conforming%20Materials%22%20OR%20%22RFID%22%20OR%20%22Process%20Improvement%22%20OR%20%22Founder%22%20OR%20%22Co-Founder%22,company-%3EMaxim%20Integrated)&origin=FACETED_SEARCH&q=guided&start=10', headers=headers)



for p in re.findall('entityUrn":"urn:li:fs_miniProfile:(.*?)"',response.text):
    print p