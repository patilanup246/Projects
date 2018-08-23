'''
Created on May 19, 2018

@author: tasneem
'''
import linkedin_properties
from selenium import webdriver
def create_driver():
    try:
        driver = webdriver.Chrome()
        return driver
    except Exception as e:
        print (e)