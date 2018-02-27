'''
Created on 29-Oct-2017

@author: Administrator
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from pyquery import PyQuery
import csv
from time import gmtime, strftime



def read_file(path):
    return open(path, encoding='utf-8').read()

def write_to_csv_file(file_object):
    pass

def get_driver_element(driver, css_selector):
    return driver.find_elements_by_css_selector(css_selector)