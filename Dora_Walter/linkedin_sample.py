import requests

url = "https://www.linkedin.com/sales/search/results/companies"

querystring = {"geoScope":"BY_REGION","facet":["CCR","I","CS"],"facet.CCR":"us:0","facet.I":"80","facet.CS":"E","REV":"USD","count":"80","start":"880","trackingInfoJson.contextId":"41310F70D686F0148076737EFE2A0000","trackingInfoJson.requestId":"983bb9e8-f2c7-42a5-ad18-a515fa022ccc","_":"1508854131983"}

headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "max-age=0",
    'cookie': "bcookie=\"v=2&7d34372d-be42-4b3b-86b3-f2c0d99bccd0\"; bscookie=\"v=1&201706271356155f29c45a-56f5-43a7-810e-c41320aa4b27AQHjbn8brLS93r41PhdUg6J7BX0l2OKB\"; visit=\"v=1&M\"; _chartbeat2=CPININBdwgIaBHAZGD.1501329820447.1501329820462.1; VID=V_2017_07_29_14_270; ELOQUA=GUID=bad3f81505f04e63972f9883d15649c7; sl=\"v=1&7COn6\"; liap=true; JSESSIONID=\"ajax:0199749234779539518\"; li_at=AQEDAQXQY1AFuXeEAAABXzR07qAAAAFfWIFyoFYAcKG7jm8zcRKaqmoPetarJHdYfUzaNZfdzFhd8bzacf4xkJiJczMN0ob2ldArdchEAeuEC1V7Q7yuKDXizqo798C6JAiGhJg-Vu10uPMHJetTPy1K; lidc=\"b=SB92:g=50:u=261:i=1508854114:t=1508912926:s=AQH7PvxaK7hmzvPsfEZBj9FnOxZJ_lhh\"; _ga=GA1.2.151815404.1498571786; _lipt=CwEAAAFfTra4KKSq2qKDT7XsddpBDnirLM1GVYv8oN1whM98L-u4FRrAVfHf38BN4YxZCUY3FATJLQNnHlEYQH-IIaCZQMfv_PKqCm4VU5D5DSXSwoqkwWb8dPT1Xogp4Zg9k-dIx2AztgzcxueFBSike2vTjWF9FFdip0UmGRMkzUdz5b6n_yYV5Ipxcz6Lm1b1PLuVOrJOm271-pMwpWHobBXR6Oe2vJpdP2yAWvslWL5-zRaZSJtQe8_smEVMdpbj56UA99wdm-OyjEaqmL31QR0IMxpqY9dMrz8fagre7LwAqgCfTur312-b9o36GXXRoIz3THZi5eAktq1cO-U_gSry5OM8buxH_-_lMYKntDdgWOJP_4a5o5RHJkrQ43dd_ySbcmP9rpK7xr2-012fIQxzDr6QSb7hotVx8oyOEwwjsP91afbmAJ260HvoZehg65gOz5wDt25aj5Z3g3Y0TbtuQDeZ4pis1ZAqZZX1qlJG3qd7yP1GXOUW4A7f91HMQQg8tHQTjSRnFkDMTeQoo2wMNiYhQthr08CQalyeY7ObtTZwmrG4TuQqbhgA_p0vSabtWJg; li_a=AQJ2PTEmc2FsZXNfY2lkPTI4ODM2OTAwMiUzQSUzQTk0MDg0NTAyBlyeyR-171Vi0PVagT07DZ9cWGI; lang=\"v=2&lang=en-us\"; sdsc=22%3A1%2C1508854688515%7ECAOR%2C0vqBI3QFDvPVux%2B%2BhoLR3lM7OZoM%3D",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
    }



response = requests.request("GET", url, headers=headers, params=querystring)

for j in response.json()['searchResults']:
    print (j['companyId'])