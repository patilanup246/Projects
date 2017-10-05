'''
Created on 28-Sep-2017

@author: Administrator
'''
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1280, 1024))  
display.start()

from selenium import webdriver
import time
import pickle

def login_to_linkedin(dri):
    # global driver
    
    username = ''
    password = ''
    
    dri.get('https://www.linkedin.com/uas/login?session_redirect=%2Fvoyager%2FloginRedirect%2Ehtml&fromSignIn=true&trk=uno-reg-join-sign-in')
    
    dri.find_element_by_css_selector('.form-email input').send_keys(username)
    dri.find_element_by_css_selector('.form-password input').send_keys(password)
    dri.find_element_by_css_selector('.form-buttons input').click()
    time.sleep(5)
    
    pickle.dump(dri.get_cookies() , open("linkedin_cookies.pkl","wb"))


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)


login_to_linkedin(driver)

driver.quit()