'''
Created on 09-Dec-2017

@author: Administrator
'''
from selenium import webdriver
import requests
import time

chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
#chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--no-sandbox")
#chromeOptions.add_extension('anticaptcha.crx')
chromeOptions.add_argument("--disable-setuid-sandbox")
driver = webdriver.Chrome('./chromedriver.exe',chrome_options=chromeOptions)

def login():
    driver.get('https://www.linkedin.com/')
    driver.find_element_by_id('login-email').send_keys('Tasneem.rangwala05@gmail.com')
    driver.find_element_by_id('login-password').send_keys('muidsa1!2@')
    driver.find_element_by_id('login-submit').click()
login()
time.sleep(30)

output_f = open('linkedin_normal_output','w',encoding='utf-8')
for comp_id in open('linkedin_normal_input').read().split('\n'):
    driver.get('https://www.linkedin.com/company/'+str(comp_id))
    time.sleep(5)
    try:
        driver.find_element_by_css_selector('.org-about-company-module__show-details-button').click()
    except Exception as e:
        login()
    output = str(comp_id)+'\t'
    
    try:
        output += driver.find_element_by_css_selector('.org-top-card-module__name').text+'\t'
    except:
        output += '\t'
        
    try:
        output += driver.find_element_by_css_selector('.org-top-card-module__location').text+'\t'
    except Exception as e:
        #print (e)
        output += '\t'
        
    try:
        output += driver.find_element_by_css_selector('.org-about-company-module__company-staff-count-range').text+'\t'
    except:
        output += '\t'
    
    try:
        output += driver.find_element_by_css_selector('.company-industries').text+'\t'
    except:
        output += '\t'    
    
    try:
        output += driver.find_element_by_css_selector('.org-about-company-module__headquarters').text+'\t'
    except:
        output += '\t'
    
    try:
        output += driver.find_element_by_css_selector('.org-about-us-company-module__website').text+'\n'
    except Exception as e:
        output += '\n'
    print (output)
    output_f.write(output)
    output_f.flush()
    time.sleep(25)