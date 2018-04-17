'''
Created on Apr 14, 2018

@author: tasneem
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

output_log = open('account_creator_log.txt','w')

wb = load_workbook('Account_creator_info.xlsx')
ws = wb.active

i = 0
for row in ws.rows:
    if i > 0:
        try:
            proxy_value = '80.211.201.9:8888'#row[5].value
            email = row[3].value
            fn =    row[0].value
            ln =    row[1].value
            dob =   row[2].value
            password = row[4].value
            
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % proxy_value)
            
            driver = webdriver.Chrome()
            
            driver.get('https://www.nike.com/us/en_us/p/activity/register')
            
            element0 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="emailAddress"]')))
            element0.send_keys(email)

            driver.find_element_by_css_selector('[name="password"]').send_keys(password)
            driver.find_element_by_css_selector('[name="firstName"]').send_keys(fn)
            driver.find_element_by_css_selector('[name="lastName"]').send_keys(ln)
            driver.find_element_by_css_selector('[name="dateOfBirth"]').send_keys(dob)
            driver.find_element_by_css_selector('[data-componentname="gender"] span').click()
            
            driver.find_element_by_css_selector('[class="checkbox"]').click()
            
            driver.find_element_by_css_selector('[value="CREATE ACCOUNT"]').click()
            
            time.sleep(10)
            
            if 'https://www.nike.com/us/en_us/p/myactivity' == driver.current_url:
                output_log.write(email+'\t\t'+'Passed'+'\n')
                output_log.flush()
                print ('Success')
            else:
                output_log.write(email+'\t\t'+'Failed'+'\n')
                output_log.flush()
                print ('Failed')
            
        except Exception as e:
            print (e)
            output_log.write(email+'\t\t'+'Failed'+'\n')
            output_log.flush()
        finally:
            driver.quit()

        break
    i+=1