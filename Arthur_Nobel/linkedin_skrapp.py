'''
Created on Feb 24, 2018

@author: talib
'''
import requests, csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


output_f = open('output.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Link',    'Name',    'Location',    'Headline',    'Email'])





chromeOptions = webdriver.ChromeOptions()
#prefs = {"profile.managed_default_content_settings.images":2}
#chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_extension('./skrapp.crx')
chromeOptions.add_argument("--disable-setuid-sandbox")
#driver = webdriver.Chrome('./chromedriver',chrome_options=chromeOptions)
driver = webdriver.Chrome(chrome_options=chromeOptions)
#driver.get('chrome-extension://neodgnejhhhlcdoglifbmioajmagpeci/options.html')
#driver.find_element_by_id('auto_submit_form').click()
#driver.find_element_by_name('account_key').send_keys('5f6b75f0738a1bd09cf717392c9804a3')
#driver.find_element_by_id('save').click()
#return driver


driver.get('https://www.skrapp.io/login')
driver.find_element_by_css_selector('[name="email"]').send_keys('justtrailersandteasers+account1@gmail.com')
driver.find_element_by_css_selector('[name="pwd"]').send_keys('muidsa1!2@')
driver.find_element_by_css_selector('[type="submit"]').click()


driver.get('https://www.linkedin.com/uas/login-cap?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fcap&source_app=cap&trk=cap_signin')
driver.find_element_by_css_selector('[name="session_key"]').send_keys('kumar.jan08@gmail.com')
driver.find_element_by_css_selector('[name="session_password"]').send_keys('sindhu007')
driver.find_element_by_css_selector('[name="signin"]').click()
time.sleep(5)


for profile in open('input.txt').read().split('\n'):
    details = []
    driver.get(profile)
    time.sleep(10)
    
    name = ''
    location = ''
    headline = ''
    email = '' 
    try:
        name = driver.find_element_by_css_selector('[class^="pv-top-card-section__name"]').text
        location = driver.find_element_by_css_selector('[class^="pv-top-card-section__location"]').text
        headline = driver.find_element_by_css_selector('[class^="pv-top-card-section__headline"]').text
    except Exception as e:
        print (e)
    try:
        driver.find_element_by_css_selector('[class="sk_find_btn_new"]').click()
        time.sleep(10)
        email = driver.find_element_by_css_selector('[class="sk_email_value"] span').text
    except Exception as e:
        driver.get(profile)
        time.sleep(10)
        try:
            driver.find_element_by_css_selector('[class="sk_find_btn_new"]').click()
            time.sleep(10)
            email = driver.find_element_by_css_selector('[class="sk_email_value"] span').text
        except Exception as e1:
            print (e1)
        print (e)
    details.append(profile)
    details.append(name)
    details.append(location)
    details.append(headline)
    details.append(email)
    
    wr.writerow(details)
    print (details)