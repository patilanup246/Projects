'''
Created on Apr 10, 2018

@author: talib
'''
import sys
from selenium import webdriver 
chrome_options = webdriver.ChromeOptions()

email = 'bob@hotmail.com'
message = 'This is a test.  The quick brown fox jumped over the lazy dog.'
name    = 'Bob Barker'
subject = 'This is a subject'
    
    
driver = webdriver.Chrome(chrome_options=chrome_options)
    
def fill_values(label,value):
    a = driver.find_element_by_css_selector('form').find_element_by_xpath("//*[contains(text(),'{}')]".format(label))
    count = 0
    while True:
        if count > 5:
            break
        try:
            a.find_element_by_xpath('..//input').send_keys(value)
            break
        except Exception as e:
            a = a.find_element_by_xpath("..")
        count+=1
driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdBzvALrGZB3QZqfBA9oomiauKneGrOD6Qiycd536bNsP3tJQ/viewform')

        