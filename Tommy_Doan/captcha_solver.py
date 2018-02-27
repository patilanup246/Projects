'''
Created on Feb 23, 2018

@author: tasneem
'''
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import shutil
import time
username = 'goahrefs8@gmail.com'
password = '12345678'


def get_captcha_text(image_url):
    api_key = '7521586f459073ecf09891f79bc91e5f'
    #Downloading the captcha image to be sent to 2captcha
    response = requests.get(image_url, stream=True)
    with open('captcha.jpeg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        
        
    #send captcha image to 2captcha for solving
    two_captcha_url = 'http://2captcha.com/in.php?json=1'
    files = {'file': open('captcha.jpeg', 'rb')}
    data = {'key': api_key, 'method': 'post'}
    r_send_image = requests.post(two_captcha_url, files=files, data=data).json()
    
    #get captcha id to be used for getting the solved captcha details.
    captcha_id =  r_send_image['request']
    
    #will wait maximum 20 seconds for the captcha image to get solved.
    captcha_waiting_time = 20
    while captcha_waiting_time > 0:
        r_receive = "http://2captcha.com/res.php"
        querystring = {"key":api_key,"action":"get","id":captcha_id,"json":"1"}
        
        r_receive_final = requests.request("GET", r_receive, params=querystring).json()
    
        if r_receive_final['status'] == 1:
            return r_receive_final['request']
            break
        
        #wait for 1 second
        time.sleep(1)
        
        captcha_waiting_time-=1




#Create a instance of webdriver
DRIVER = webdriver.Chrome()
 
#Go to login page of Merch By Amazon
DRIVER.get('https://merch.amazon.com/dashboard')
 
#Input username
DRIVER.find_element_by_css_selector('[type="email"]').send_keys(username)
 
#Input Password
DRIVER.find_element_by_css_selector('[type="password"]').send_keys(password)
 
#Click Login 
DRIVER.find_element_by_css_selector('[id="signInSubmit"]').click()
 
#get Captcha image source
image_element = WebDriverWait(DRIVER, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="gear-invite-captcha-container"]')))
image_url = image_element.get_attribute('src')


#Solve Captcha 
print (get_captcha_text(image_url))


#waiting for 60 second before calling driver quit
time.sleep(60)

DRIVER.quit()


     
    