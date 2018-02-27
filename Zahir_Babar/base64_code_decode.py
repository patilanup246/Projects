# -*- coding: utf-8 -*-
'''
Created on 21-Jan-2018

@author: Administrator
'''
from selenium import webdriver
import time


driver = webdriver.Chrome()   # for opening browser



driver.get('https://www.google.com')

driver.find_element_by_name('btnI').send_keys('how to automate')
time.sleep(5)  # waiting for next instruction

driver.quit()