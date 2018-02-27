'''
Created on May 13, 2017

@author: Mukadam
'''
import requests

url = "http://www.webmail.co.za/register.php"

payload = "page=page1&firstname=Feroz&surname=karp&userid=rangwalaindore14&domain=webmail.co.za&password=muidsa1!2%40&confirm=muidsa1!2%40&pquestion=1&panswer=bb&altemail=&cell=1234567890&gender=M&bday=19&bmonth=01&byear=1952&location=NE&gplocations=&gplocations=&language=ZU&street=&TheButton=Register"
headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-encoding': "gzip, deflate",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'content-length': "295",
    'content-type': "application/x-www-form-urlencoded",
    'cookie': "PHPSESSID=8lis5k4202vo6880bo3b9bflq5; _ga=GA1.3.648507849.1494686926; _gid=GA1.3.2021247570.1494687214",
    'host': "www.webmail.co.za",
    'origin': "http://www.webmail.co.za",
    'referer': "http://www.webmail.co.za/register.php",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'postman-token': "5e2e86e4-dd4f-2e6e-baa4-3a6487aad2d6"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)