# -*- coding: utf-8 -*-
'''
Created on 02-Feb-2018

@author: Administrator
'''
import requests, csv, re, math, time, sys
from pyquery import PyQuery
from selenium import webdriver
from selenium.webdriver.support.ui import Select

URL = sys.argv[1]
file_name = sys.argv[2]

output_f = open(file_name+'.csv','w',encoding='utf-8', newline='')
WR = csv.writer(output_f, quoting=csv.QUOTE_ALL)
WR.writerow(['Property ID',    'Type',    'Tax Area',    'Open Space',    'Historic Property',    'Multi-Family Redevelopment',    'Township',    'Range',    'Legal Description',    'Land Use Code',    'Section',    'Address',    'Name',    'Mailing Address Line 1',    'Mailing Address Line 2',    '% Ownership',    'Taxes and Assessment: Amount Due - line 1',    'Taxes and Assessment: Amount Due - line 2',    'Value: Taxable Value',    'Land: Type',    'Land: Description',    'Land: Acres',    'Land: Eff Front',    'Land: Eff Depth',    'Land: Market Value',    'Land: Prod. Value',])
 
 
DRIVER = webdriver.Chrome('./chromedriver')
links_file =  open('links_temp.txt','w',encoding='utf-16')
   
   
def is_city(driver):
    try:
        driver.find_element_by_css_selector('#propertySearchOptions_city')
        return True
    except Exception as e:
        return False
       
def get_all_cities(driver):
    cities = []
    for city in driver.find_elements_by_css_selector('#propertySearchOptions_city option'):
        cities.append(city.get_attribute('value'))
    return cities
   
def get_total_pages(driver):
    try:
        total_results =  (re.sub("\D", "", re.search(r'of (.*?) for',driver.find_element_by_css_selector('#propertySearchResults_pageHeading').text).group(1)))
        return (int(math.ceil(float(total_results)/250))+1)
    except Exception as e:
        return 0
   
def search_by_city(driver, city):
    select = Select(driver.find_element_by_id('propertySearchOptions_city'))
    select.select_by_value(city)
       
    select = Select(driver.find_element_by_id('propertySearchOptions_taxyear'))
    select.select_by_index(0)
       
    select = Select(driver.find_element_by_id('propertySearchOptions_recordsPerPage'))
    select.select_by_index(len(select.options)-1)
       
    driver.find_element_by_id('propertySearchOptions_search').click()
       
def search_by_owner(driver, keyword):
       
    driver.find_element_by_id('propertySearchOptions_ownerName').send_keys(keyword)
       
    select = Select(driver.find_element_by_id('propertySearchOptions_taxyear'))
    select.select_by_index(0)
       
    select = Select(driver.find_element_by_id('propertySearchOptions_recordsPerPage'))
       
    select.select_by_index(len(select.options)-1)
       
    driver.find_element_by_id('propertySearchOptions_search').click()
       
try:
    DRIVER.get(URL+'/propertyaccess/?cid=0')
    DRIVER.find_element_by_css_selector('#propertySearchOptions_advanced').click()
    if is_city(DRIVER):
        cities = get_all_cities(DRIVER)
           
        for city in cities:
            search_by_city(DRIVER, city)
            total_pages = get_total_pages(DRIVER)
            if total_pages:
                for page in range(1,total_pages):
                    DRIVER.get(URL+'/propertyaccess/SearchResults.aspx?cid=0&rtype=address&page='+str(page))  
                    for l in DRIVER.find_elements_by_css_selector('#propertySearchResults_resultsTable tr td a[onmouseover*="window.status=\'View Details\'"]'):
                        #print (l.get_attribute('href'))
                        links_file.write(l.get_attribute('href')+'\n')
                        links_file.flush()
            DRIVER.get(URL+'/propertyaccess/?cid=0')
            DRIVER.find_element_by_css_selector('#propertySearchOptions_advanced').click()
               
                   
    else:
        for i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            for j in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                search_by_owner(DRIVER, i+j)
                total_pages = get_total_pages(DRIVER)
                if total_pages:
                    for page in range(1,total_pages):
                        DRIVER.get(URL+'/propertyaccess/SearchResults.aspx?cid=0&rtype=address&page='+page)
                        for l in DRIVER.find_elements_by_css_selector('#propertySearchResults_resultsTable tr td a[onmouseover*="window.status=\'View Details\'"]'):
                            #print (l.get_attribute('href'))
                            links_file.write(l.get_attribute('href')+'\n')
                            links_file.flush()
                DRIVER.get(URL+'/propertyaccess/?cid=0')
                DRIVER.find_element_by_css_selector('#propertySearchOptions_advanced').click()
except Exception as e:
       
    print (e)
    time.sleep(10)
    DRIVER.quit()
    
def get_driver_css_element(driver,css_selector):
    try:
        return str(driver.find_element_by_css_selector(css_selector).text)
    except:
        return ''
      
DRIVER = webdriver.Chrome('./chromedriver')
for u in open('links_temp.txt',encoding='utf-16').read().split('\n'):
    print (u)
    try:
        DRIVER.get(u)
        #pq = PyQuery(r.text)
        details = []
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(2) td:nth-of-type(2)'))
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(4) td:nth-of-type(2)'))
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(5) td:nth-of-type(2)'))
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(6) td:nth-of-type(2)'))
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(7) td:nth-of-type(2)'))
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(8) td:nth-of-type(2)'))
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(9) td:nth-of-type(2)'))
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(10) td:nth-of-type(2)'))
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(2) td:nth-of-type(4)'))
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(5) td:nth-of-type(4)'))
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(9) td:nth-of-type(4)'))
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(12) td:nth-of-type(2)'))
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(16) td:nth-of-type(2)'))
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(17) td:nth-of-type(2)'))
        details.append ('')
        details.append (get_driver_css_element(DRIVER,'[summary="Property Details"] tr:nth-of-type(17) td:nth-of-type(4)'))
        details.append (get_driver_css_element(DRIVER,'.statementTableData .statementDetailTable tr td:nth-of-type(9)'))
        details.append ('')    
        details.append (get_driver_css_element(DRIVER,'#valuesDetails tr:nth-of-type(19) td:nth-of-type(3)'))
        details.append (get_driver_css_element(DRIVER,'#landDetails tr:nth-of-type(2) td:nth-of-type(2)'))
        details.append (get_driver_css_element(DRIVER,'#landDetails tr:nth-of-type(2) td:nth-of-type(3)'))
        details.append (get_driver_css_element(DRIVER,'#landDetails tr:nth-of-type(2) td:nth-of-type(4)'))
        details.append (get_driver_css_element(DRIVER,'#landDetails tr:nth-of-type(2) td:nth-of-type(6)'))
        details.append (get_driver_css_element(DRIVER,'#landDetails tr:nth-of-type(2) td:nth-of-type(7)'))
        details.append (get_driver_css_element(DRIVER,'#landDetails tr:nth-of-type(2) td:nth-of-type(8)'))
        details.append (get_driver_css_element(DRIVER,'#landDetails tr:nth-of-type(2) td:nth-of-type(9)'))
        
        WR.writerow(details)
        
    except Exception as e:
        print(e)

DRIVER.quit()

