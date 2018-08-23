'''
Created on May 19, 2018

@author: tasneem
'''
import linkedin_properties
from selenium import webdriver
def create_driver():
    try:
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
#         driver = webdriver.Chrome(chrome_options=options)
        driver = webdriver.Firefox()
        return driver
    except Exception as e:
        print (e)