import requests

url = "http://beta.speedtest.net/api/results.php"

payload = "serverid=13384&testmethod=ws&hash=ad351218251eb26f951d38a7503fb77b&source=st4-js&configs%5Bworkers%5D=false&configs%5BlatencyProtocol%5D=ws&configs%5BdownloadProtocol%5D=xhr&configs%5BuploadProtocol%5D=xhr&configs%5Bhost%5D=speedtest.paradisetele.net&configs%5Bport%5D=8080&configs%5BserverVersion%5D=2.5&configs%5BserverBuild%5D=2017-08-15.1314.4ae12d5&ping=23&jitter=1.4444444444444444&upload=509&download=20080"
headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'content-length': "412",
    'content-type': "application/x-www-form-urlencoded",
    'cookie': "_dc_gtm_UA-389482-3=1; _g_m=; bknx_fa=1507952168151; bknx_ss=1507952168151; _gat_UA-389482-3=1; _ga=GA1.2.111915767.1507952168; _ga=GA1.3.111915767.1507952168; stnetsid=picd19204fajhlppbf1eif9g32; st4-sid=s%3AHoGio5ZTaUAGFjRjFSUxD7pNUlFiF6AE.f36XE%2Fco4TSvL8USi5RCUE97tg5ILzU11c6%2FC%2BxXNVo",
    'host': "beta.speedtest.net",
    'origin': "http://beta.speedtest.net",
    'pragma': "no-cache",
    'referer': "http://beta.speedtest.net/result/6705427321",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.52 Safari/537.36",
    'x-requested-with': "XMLHttpRequest"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)