import requests
import os
import urllib.request
from pyquery import PyQuery
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
from time import gmtime, strftime

site_name = 'new-pharm'+'_'+strftime("%Y-%m-%d%H-%M-%S", gmtime())
try:
    os.makedirs(site_name)
except:
    pass

username = ''
password = ''

starting_url = 'http://prices.new-pharm.co.il/'


chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : os.getcwd()+'\\'+site_name}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

try:
    driver.get(starting_url)
    driver.find_element_by_id('ContentPlaceHolder1_btnSearch').click()
    
    
    link_container = []
    
    while True:
        
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "tr td a")))

        links = driver.find_elements_by_css_selector('tr td a')
        
        for l in links:
            try:
                link_container.append (l.get_attribute("href"))
                print (l.get_attribute("href"))
            except Exception as e:
                print (e)
        try:
            driver.find_element_by_css_selector('[disabled="disabled"][name="ctl00$ContentPlaceHolder1$pager$ctl00$ctl01"]')
            driver.quit()
            break
        except Exception as e:
            driver.execute_script("$('[name=\"ctl00$ContentPlaceHolder1$pager$ctl00$ctl01\"]').click()")
            time.sleep(3)
            #print (e)
            
    

    for l in link_container:
        name_link = str(l.split('/')[-1]).lower()
        if 'promofull' in name_link or 'pricefull' in name_link or 'stores' in name_link:
            print (name_link)
            urllib.request.urlretrieve (l, site_name+'/'+ name_link)
    
finally:
    driver.quit()