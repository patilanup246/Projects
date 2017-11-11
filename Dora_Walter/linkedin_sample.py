import requests

url = "https://www.linkedin.com/sales/search/results/companies"



headers = {
    'accept': "*/*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache",
    'cookie': "visit=\"v=1&M\"; __utma=226841088.1787484206.1508864129.1509282281.1509282281.1; __utmz=226841088.1509282281.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); jobs_hru=false; bcookie=\"v=2&d6533bc1-24ed-48f6-86c6-b4ac5a6ebc44\"; bscookie=\"v=1&201711041302065590903c-f776-4104-8137-4f620c755ba8AQE9aIACAUAcdU86PTha3if7s3u6cwN4\"; _ga=GA1.2.1787484206.1508864129; _lipt=CwEAAAFfl66kCcFxpe6DG0yML2w_04I5kUTmyhSJZWs9Ijy4Og_xXS-aHb_aFFvtWmtCHEHNyWiNYTR2Z7A65DGQ8aRiS3r8btFKCr8cNhOIHteaQ8_TNE5P_8sSejOl8k5Fc01VVm2GZhQvpDdf2eO8PhNRBdVmqicUgdFSPiQVt1bOe-AOuNh3BEvTcB_v7hnv936alK3s-3-aBcSgGg1ufI4HnpQF7hwIexqfoQ-w-V9eY9E-t3MCWsgbJCDN4h2owzQpw5XkPUXuaXZYMstvpzWLFcXr-C0ZtKd7Bss9bqHce_mP6bYOoEdPSoVQi9mdEDIUVxqoVZCpGpnO8XVYfXsnPuNzRB23XVqmC6Wai4IQ1zAUiC7u0nOh99Z0yVSm2K6aWdaZLT3bakfP6wRvr9DcYvwgBIdsp7BpBLjxDVqKmyjr6suRHJdNeBR8BNIHpiGzyVf3M7a2d_QFPwqoKMXMRXuc0XtFo-xXhpt65QDIdx0DZu_WS3WSY7b9TlupKAAX7vfsUL_OyQSXwRnoqg; li_at=AQEDAQXQY1ACim0pAAABX3zQFNwAAAFfyiH12VEAq9WHH9jAPdVYU8h5qqvUXtp9qdEUdeIIsm90aS0pYNaV7vlSZlMZiirMRQ1DvC0MS0GEoUiffnL522ntuyxCgF1N_Mf9QXhwqGtsWgp152Ckdyw_; liap=true; sl=\"v=1&VQmmX\"; JSESSIONID=\"ajax:7847239372892592655\"; lidc=\"b=SB92:g=52:u=274:i=1510319943:t=1510400346:s=AQEjcbXsDbDcYzKAagsk3ax8NNdzaxdU\"; li_a=AQJ2PTEmc2FsZXNfY2lkPTI4ODM2OTAwMiUzQSUzQTk0MDg0NTAyXns_javxvshaYnNX5BhH_53s0rw; lang=\"v=2&lang=en-us\"; sdsc=1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D",
    'pragma': "no-cache",
    'referer': "https://www.linkedin.com/sales/search/companies?geoScope=BY_REGION&facet=CCR&facet=I&facet=CS&facet.CCR=us%3A0&facet.I=80&facet.CS=C&facet.CS=D&REV=USD&minCompanyGrowth=99&maxCompanyGrowth=100&count=25&start=0&trackingInfoJson.contextId=F81E65B9FFBBF514C0ED85791F2B0000",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    'x-li-identity': "dXJuOmxpOm1lbWJlcjo5NzU0Mjk5Mg",
    'x-requested-with': "XMLHttpRequest"
    }


output_f =  open('output_f','w')
#print(response.text)
for i in ['v','w','x','y','z']:
    for j in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
    
        querystring = {"":"","keywords":i+j,"geoScope":"BY_REGION","facet":["CCR","I","CS"],"facet.CCR":"us:0","facet.I":"80","facet.CS":["C","D"],"REV":"USD","count":"1000","start":"0"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        print (str(i+j) + '-- '+ str(len(response.json()['searchResults'])))
        for j in response.json()['searchResults']:
            output_f.write (str(j['companyId'])+'\n')
            output_f.flush()