import requests, csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.parse

output_f = open('output_bing_linkedin.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Link',    'Headline',    'Title',    'Industry',    'Connection', 'Location'])

driver = webdriver.Chrome()

driver.get('https://www.bing.com/search?q=a')

for linkedin_url in open('input_linkedin_urls.txt',encoding="utf-8").read().split('\n'):
    details = []
    details.append(linkedin_url)
    try:
#         driver.find_element_by_css_selector('[class="b_searchbox"]').clear()
#         driver.find_element_by_css_selector('[class="b_searchbox"]').send_keys(linkedin_url)
#         driver.find_element_by_css_selector('[type="submit"]').click()
        driver.get('https://www.bing.com/search?q='+urllib.parse.quote(str(linkedin_url), safe=''))
        #time.sleep(1)
        ele = driver.find_element_by_css_selector('[id="b_results"] .b_algo')
        
        details.append (ele.find_element_by_css_selector('h2 a').text)
        ele2 = ele.find_elements_by_css_selector('.b_vlist2col strong')
        title = ''
        industry = ''
        connection = ''
        location = ''
        for e in ele2:
            if 'Location:' in e.text:
                location = e.find_element_by_xpath("..").text
            if 'Industry:' in e.text:
                industry =  e.find_element_by_xpath("..").text
            if 'Connections:' in e.text:
                connection =  e.find_element_by_xpath("..").text
            if 'Title:' in e.text:
                title =  e.find_element_by_xpath("..").text
                
        
        
        
        details.append(title)
        details.append(industry)
        details.append(connection)
        details.append(location)
    
    
    except Exception as e:
        print (e)
    print (linkedin_url)
    wr.writerow(details)
    
