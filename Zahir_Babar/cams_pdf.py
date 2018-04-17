'''
Created on Mar 19, 2018

@author: talib
'''
from selenium import webdriver

import time
import os
from selenium.webdriver.support.ui import Select

import sys

import re



import requests

url = "https://fundsnet.camsonline.com/Acctstmt/AcctStmt.aspx"

payload = ""
headers = {
    'origin': "https://fundsnet.camsonline.com",
    'upgrade-insecure-requests': "1",
    'content-type': "application/x-www-form-urlencoded",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "https://fundsnet.camsonline.com/eCRMS/BrokerOnlineSite/BrokerOnline/BOL_AcctStmt.aspx?J0zF4CyAxT5yzPSmiR3i2623UdoU4VcC0n0syVM3vE9sdRyqEAzpCPLwL8ii73wPG7dyRrEX6etWXRxCW4Dy%2fkO30mg8oVrFRqMlOZgllkvTDL%2bKelKjYybaNNjNDmKZjH%2b12L6X1pJiFGFtWhbhKCnGFhVvPINEzMMPeXtpa4VsPwkDD%2fH5yg6QQ2uhonlMlu4XIhoOSlDnHjNPW4cbi9tIfECgkCx5hlvApszGxp2WdCHmRN9j6IIraOclHUB8zN6zebbdBoeeaiH1IFrum8FpP4NwpTskRwGJf%2b23yZlcMgUTIUXBoELem27Hj8U46P7z38UNCF1r7gNSsDyHM%2fUCTXoDtvrqXwS1OaKlC4wMDvVx3NT5SvJGSbhafG8XryzL4pjqIY5LDZUwovzOJaLjtftwcH7Qz5n4zO%2bOJnlfcTQmQoFrbkD6EykFeR%2f9s3mhrI3h8t9UUUdnKQn1baYjwCIyQhBIaCRS%2fii3P%2fkTa1GH9FkOTepdWUJOxeVv3Qf%2bHXAqqYHoccCvOkR37quDhqVdIochoZCRgEfsvHKaI1th9d9Xdq5wuKPpxrtC2aHI27TS2M%2fhj6cluyQJTkMtaRRA1onIMbicECVxOIqwgKFm4B2hUcGY13LsqC12o1HBgs%2fI7QgbpnbFsPHDLY%2fkLKytmbjwJIkH9%2bZ98SOOcVKIOrv%2f5URxzmr9JuNOi79T0aynEDZ%2bhHUwzxQHkiv5zxPy%2fu3UfgKxYoqbbhU1kZqs6iige9CFvmZSvXT%2bXPK0x3zDgTLGnagIwSvtK6VZ7HjChsNpsRCSEz%2fKr7CsqBnlvf4cugNxj7VtNL2cST8dAHDNb%2b%2fgL0lSXsEpvvFDIFROL6MaoECC82eIASIlqPnMrFu9o7gngJPRIZroMqxY9E4m4CiB5Fsv5QW1KU2LlRabulNPiqn53NNmHp%2fqLGXFHZiv0ZzuKvpzucfO",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'cookie': "__CSRFCOOKIE=a9ee5cb8-6c68-4cec-97cb-4ef2f6fe56c4; cookiesession1=0899E82FFFJBG8NLMSBHQRR4MBJUF59D; ASP.NET_SessionId=xdjw0hmh2lsdn20zo2uwuwdr; __CSRFCOOKIE=a9ee5cb8-6c68-4cec-97cb-4ef2f6fe56c4; cookiesession1=0899E82FFFJBG8NLMSBHQRR4MBJUF59D; ASP.NET_SessionId=jQwufETmc3untrx2wyirsf3c5vc4mox1551",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)



folio_num = '1036924530'
account = 'B'

site_name = str(folio_num)+'_'+str(account)
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
prefs = {
    "download.default_directory" : os.getcwd()+'\\CAMS\\'+site_name,
    'profile.managed_default_content_settings.images': 2
    }
chrome_options.add_experimental_option("prefs",prefs)
DRIVER = webdriver.Chrome(chrome_options=chrome_options)

def login(driver):
    driver.get('https://fundsnet.camsonline.com/eCRMS/index.aspx')
    driver.find_element_by_css_selector('[name="UserCode"]').send_keys('BACC')
    driver.find_element_by_css_selector('[name="UserPwd"]').send_keys('Cams123@')
    driver.find_element_by_css_selector('[alt="Login"]').click()

    


def get_report(driver, folio_num,acc):
    login(driver)
    
    driver.find_element_by_css_selector('[href*="BOL_InvLocate.aspx"]').click()
    
    driver.find_element_by_css_selector('[name="txtFolionoloc"]').send_keys(folio_num)
    
    
    select = Select(driver.find_element_by_css_selector('[name="drpfundfolio"]'))
    select.select_by_value(acc)
    

    driver.find_element_by_css_selector('[name="btnGofolio"]').click()
    
    page_sour = driver.page_source
    driver.get('https://fundsnet.camsonline.com/eCRMS/BrokerOnlineSite/BrokerOnline/'+str(re.findall("var qry = '(.*?)';", page_sour)[0]))
    
    driver.find_element_by_css_selector('[name="rdStmtType"][value="FULL"]').click()
    driver.find_element_by_css_selector('[name="btnview"]').click()
    


try:
    print (get_report(DRIVER, str(folio_num),str(account))) 
except Exception as e:
    print (e)
finally:
    time.sleep(20000)
    DRIVER.quit()