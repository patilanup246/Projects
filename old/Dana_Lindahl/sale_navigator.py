
import requests
from pyquery import PyQuery
from time import gmtime, strftime
from selenium import webdriver
import csv
import time
driver = webdriver.Chrome()

username = ''
password = ''


driver.get('https://www.linkedin.com/sales')

driver.find_element_by_id('session_key-login').send_keys(username)
driver.find_element_by_id('session_password-login').send_keys(password)
driver.find_element_by_id('btn-primary').click()

time.sleep(5)
file_export = open('sales_nav_output'+'_'+strftime("%Y-%m-%d_%H-%M-%S", gmtime())+'.csv', 'w', newline='',encoding='utf-8')
wr = csv.writer(file_export, quoting=csv.QUOTE_ALL)
headerscsv = ['Company_Name','Address','Website','Industry','Size']
wr.writerow(headerscsv)


driver.get(open('target_url.txt').read())
all_links = []
while True:
    time.sleep(10)
    for comp in driver.find_elements_by_css_selector('.name-link.account-link'):
        all_links.append(comp.get_attribute('href'))
    
    try:
        driver.find_element_by_css_selector('.next-pagination.page-link.disabled')
        break
    except Exception as e:
        ele1 = driver.find_element_by_css_selector('.next-pagination.page-link')
        driver.execute_script("arguments[0].click();", ele1)

for link in all_links:
    driver.get(link)
    time.sleep(2)
    try:
        data_all = []
        name = driver.find_element_by_css_selector('.acct-name').text.strip()
        address = driver.find_elements_by_css_selector('.account-term-desc')[1].text.strip()
        website = driver.find_elements_by_css_selector('.account-term-desc')[2].text.strip()
        industry = driver.find_element_by_css_selector('.industry.detail').text.strip()
        size = driver.find_element_by_css_selector('.size.detail').text.strip()
        data_all.append(name)
        data_all.append(address)
        data_all.append(website)
        data_all.append(industry)
        data_all.append(size)
        wr.writerow(data_all)
        print (str(name)+'\t'+ str(address)+'\t'+ str(website)+'\t'+ str(industry)+'\t'+ str(size))
    except Exception as e:
        print (e)
        pass
    

driver.quit()