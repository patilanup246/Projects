'''
Created on Apr 28, 2018

@author: talib
'''
import openpyxl
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

API_KEY = 'PyQXWOelDWPaDGaIcrxBGaYInW6CtE'
COUNTRY = 'UK'



output_log = open('account_verifier_log.txt','w')
wb = load_workbook('Account_verifier_info.xlsx')
ws = wb.active

i = 0
for row in ws.rows:
    if i > 0:
        try:
            
            un =    row[0].value
            pw =    row[1].value
            
            
            driver = webdriver.Chrome()
            
            r = requests.get('http://smspva.com/priemnik.php?metod=get_number&country=&service=opt86&apikey='.format(COUNTRY,API_KEY)).json()
            n = str(r['number'])
            r_id = str(r['id'])
            
            
            driver.get('https://www.nike.com/gb/en_gb/p/settings')
            
            add_mobile = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.mobile-number--add-button')))
            add_mobile.click()
            
            mn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="mobileNumber"]')))
            mn.send_keys(n)
            
            
            
            
            driver.find_element_by_css_selector('[name="legalterms"]').click()

            for i in range(1,5):
                r_s = requests.get('http://smspva.com/priemnik.php?metod=get_sms&country={}&service=opt86&id={}&apikey={}'.format(COUNTRY,r_id,API_KEY)).json()
                

        except Exception as e:
            
            print (e)