import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url = "https://mdskip.taobao.com/core/initItemDetail.htm"

querystring = {"itemId":"539022854554"}

headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'referer': "https://detail.tmall.com/item.htm?spm=a230r.1.14.267.76bf523Q8aJ60&id=539022854554&ns=1&abbucket=3&skuId=3220262955330",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
file_o = open('file_o.txt','w')
file_o.write(response.text.decode('utf-8').encode('utf-8'))