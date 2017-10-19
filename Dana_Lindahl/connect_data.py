'''
Created on 17-Oct-2017

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



username = 'janevskidalibor@gmail.com'
password = 'NewLogin456'





#creating a output file
file_export = open('connect_data_output'+'_'+strftime("%Y-%m-%d_%H-%M-%S", gmtime())+'.csv', 'w', newline='')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headers = ['URL','Name', 'Website','Headquarters','Phone','Industries','Employees','Revenue','Ownership','Website']
wr.writerow(headers)
target_url = open('target_url.txt').read()

try:
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chromeOptions.add_experimental_option("prefs", prefs)
    # chromeOptions.add_argument('headless')
    chromeOptions.add_argument('disable-gpu')
    driver = webdriver.Chrome('./chromedriver', chrome_options=chromeOptions)
except Exception as e:
    print ('Failed to start chromedriver ' + str(e))
    exit()

def login_to_connect_data(driver):
    try:
        driver.get('https://connect.data.com/login?source=HPTopNav')
        driver.find_element_by_id('j_username').send_keys(username)
        driver.find_element_by_id('j_password').send_keys(password)
        driver.find_element_by_id('_spring_security_remember_me').click()
        driver.find_element_by_class_name('button-standard-text').click()
    except Exception as e:
        print ('Error in entering login information')
    
    try:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-information .screenname")))
        print ("Login Successful")
    except Exception as e:
        print ('Login failed - '+ str(e))

def get_all_links(driver):
    temp_links = []
    time.sleep(5)
    while True:
        
        all_links = driver.find_elements_by_css_selector('.name')
        for link in all_links:
            try:
                temp_links.append((link.find_element_by_css_selector('.companyName').get_attribute("href"),link.find_element_by_css_selector('.website').text))
            except Exception as e:
                pass
        
        page_length_css = len(driver.find_elements_by_css_selector('.table-navigation-button-next.table-navigation-image.table-navigation-next-image'))
        if page_length_css == 4:
            break
        next_page = driver.find_elements_by_css_selector('.table-navigation-button-next.table-navigation-image.table-navigation-next-image-active')
        next_page[0].click()
        time.sleep(3)
    return temp_links

    
login_to_connect_data(driver)
driver.get(target_url)
results_links = get_all_links(driver)
driver.quit()

count = 0
total_results = str(len(results_links)) 
for result in results_links:
    print ('Count : '+str(count)+'/'+total_results+'. Extracting - '+result[0])
    r = requests.get(result[0]).text
    pq = PyQuery(r)
    result_dataset = []
    result_dataset.append(str(result[0]))
    for data in pq('.seo-company-info tr td:nth-child(2)'):
        result_dataset.append(str(data.text).strip())
    result_dataset.append(str(result[1]))
    wr.writerow(result_dataset)
    count+=1

