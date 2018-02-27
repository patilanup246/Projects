'''
Created on Feb 15, 2018

@author: talib
'''
import websocket
import json, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get('https://abctalib.slack.com/')
w = open('out_put_up.txt','w',encoding='utf-8')
driver.find_element_by_css_selector('#email').send_keys('talibmukadam@gmail.com')
driver.find_element_by_css_selector('#password').send_keys('muidsa1!2@')
driver.find_element_by_css_selector('#signin_btn').click()
driver.get('https://abctalib.slack.com/messages/C99F3LGKV/')
time.sleep(5)

for u in open('scrape_upwork_input.txt').read().split('\n'):
    try:
        driver.execute_script('document.querySelector("#msg_input p").innerHTML = "{}"'.format(u))
        driver.find_element_by_css_selector('#msg_input').submit()
        time.sleep(5)
        last_message = driver.find_element_by_css_selector('.c-message--last')
        w.write (last_message.find_element_by_css_selector('.c-message--last .c-message__body').text+'\t'+last_message.find_element_by_css_selector('.c-message_attachment__title span').text+'\n')
        w.flush()
    except Exception as e:
        w.write ('\n')
        w.flush()
        print (e)