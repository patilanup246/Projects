import requests

url = "https://api.skrapp.io/api/v2/find"



headers = {
    'host': "api.skrapp.io",
    'connection': "keep-alive",
    'accept': "*/*",
    'origin': "chrome-extension://gklkbifnmojjpmbkojffeamiblineife",
    'x-access-key': "1730948352cO9GcaTqbVFTsblIrR6VLpdbGmVsHxJt",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.52 Safari/537.36",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9"
    }


domain = 'adroll.com'
fullname = 'Kenny Diep'
querystring = {"fullName":fullname,"domain":domain,"context":"profile","liv":"nli"}
response = requests.request("GET", url, headers=headers, params=querystring, verify = False)

print(response.json())
