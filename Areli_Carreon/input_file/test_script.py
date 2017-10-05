from urllib.parse import quote
import requests

project_number = '233415'
spider_name = 'GS'
shops_root_url = 'https://www.burgerkingjapan.co.jp/stores/index.html'
via_page_url_regex = ''
single_shop_url_regex = 'https:\/\/www.burgerkingjapan.co.jp\/stores\/detail.html\?sn=(\d+)'


shops_root_url = quote(shops_root_url, safe='')
via_page_url_regex = quote(via_page_url_regex, safe='')
single_shop_url_regex = quote(single_shop_url_regex, safe='')


url = "https://app.scrapinghub.com/api/run.json"

payload = "project="+project_number+"&spider="+spider_name+"&shops_root_url="+shops_root_url+"&via_page_url_regex="+via_page_url_regex+"&single_shop_url_regex="+single_shop_url_regex
headers = {
    'authorization': "Basic Nzc4NWU0MmY4YzZiNGE1MDk1NGMxOTUzZTk5NTYxYjc6",
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)