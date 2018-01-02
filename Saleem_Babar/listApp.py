import requests

url = "http://listapp.in/api/Login/searchProduct"

payload = "mobile_no=9172574797&user_id=3117&device_type=Android&device_token=doyoRXN4zuI%3AAPA91bEAFuxqSa29iITtgE6Vc-SlQhr0lf0CNaF51lRz4fgbX7yuq6d0uOCrWM1UNCbY02OPb_A1zmyabh8a786DKJFANff8FW88n7ZZbyAshpEq5gMuRYY05cBE0CqoJ2_MdmczPRYU&product_name=a&offset=0&city_id="
headers = {
    'Authorization': "Basic c3lzY3JhZnQ6c2lzMTIz",
    'Content-Type': "application/x-www-form-urlencoded",
    'Content-Length': "258",
    'Host': "listapp.in",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'User-Agent': "okhttp/3.3.0"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)