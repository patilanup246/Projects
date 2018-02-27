# -*- coding: utf-8 -*-
'''
Created on 30-Jan-2018

@author: Administrator
'''
import csv,sys
from selenium import webdriver
import time
from urllib.parse import urlparse, parse_qs


# URL = 'https://treasurer.yumacountyaz.gov/treasurer/treasurerweb/search.jsp'
# file_name = 'treasurer'

URL = sys.argv[1]
file_name = sys.argv[2]
start_keyword = ''
try:
    start_keyword = sys.argv[3]
except Exception as e:
    pass
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
# driver = webdriver.Chrome(executable_path ='C:\\Users\\Administrator\\workspace\\Project\\Projects\\chromedriver\\chromedriver.exe', chrome_options=options)
# driver1 = webdriver.Chrome(executable_path ='C:\\Users\\Administrator\\workspace\\Project\\Projects\\chromedriver\\chromedriver.exe', chrome_options=options)
driver = webdriver.Chrome('./chromedriver')
driver1 = webdriver.Chrome('./chromedriver')




output_f = open(file_name+'.csv','w',encoding='utf-16', newline='')
WR = csv.writer(output_f, quoting=csv.QUOTE_ALL)
WR.writerow(['Account Number','Parcel Number','Owners','Address Line 1','Address Line 2','Situs Address','Legal','Property Type','Actual','Assessed','Total Due'])
products_url = ''

def login(driver,url):
    driver.get(url)
    driver.find_element_by_css_selector('form[method="GET"] [type="submit"]').click()
    
def input_keywords(driver, keyword, url):
    driver.get(url)
    driver.find_element_by_css_selector('#TaxAOwnerIDSearchString').send_keys(keyword+'*')
    driver.find_element_by_css_selector('[value="Search"]').click()
    
def get_next_page(driver):
    try:
        page_links = driver.find_elements_by_css_selector('[class="pagelinks"] a')
    
        for p in page_links:
            if p.text.lower() == 'next':
                return (p.get_attribute('href'))
                
                break
    except Exception as e:
        return 0

def get_details(driver, url,wr):
    try:
        details = []
        driver.get(url)
        time.sleep(0.5)
        tr_count = len(driver.find_elements_by_css_selector('#taxAccountSummary tr'))
        account = driver.find_element_by_css_selector('#taxAccountSummary tr:nth-of-type(1) td:nth-of-type(2)').text
        parcel = driver.find_element_by_css_selector('#taxAccountSummary tr:nth-of-type(2) td:nth-of-type(2)').text
        legal =  driver.find_element_by_css_selector('#taxAccountSummary tr:nth-of-type({}) td:nth-of-type(2)'.format(tr_count)).text
        situs =  driver.find_element_by_css_selector('#taxAccountSummary tr:nth-of-type({}) td:nth-of-type(2)'.format(tr_count-1)).text
        address= driver.find_element_by_css_selector('#taxAccountSummary tr:nth-of-type({}) td:nth-of-type(2)'.format(tr_count-2)).text
        total_due = ''
        owners = []
        for i in range(3,4+(tr_count-6)):
            owners.append(driver.find_element_by_css_selector('#taxAccountSummary tr:nth-of-type({}) td:nth-of-type(2)'.format(i)).text)
    
        owners = ', '.join(owners)
        details.append(account)
        details.append(parcel)
        details.append(owners)
        add1 = ''
        add2 = ''
        try:
            add1 = address.split('\n')[0]
        except Exception as e:
            pass
        try:
            add2 = address.split('\n')[1]
        except Exception as e:
            pass
        details.append(add1)
        details.append(add2)
    
        details.append(situs.replace('\n',' ').replace('\r',' ').strip())
        details.append(legal.replace('\n',' ').replace('\r',' ').strip())
        for t in driver.find_elements_by_css_selector('#totals tr'):
            if t.find_element_by_css_selector('td:nth-of-type(1)').text == 'Total Due':
                total_due = (t.find_element_by_css_selector('td:nth-of-type(2)').text)
                break
        property_type = ''
        actual = ''
        assessed = ''
        for p in driver.find_elements_by_css_selector('#taxAccountValueSummary tr'):
            try:
                prop = p.find_element_by_css_selector('td:nth-of-type(1)').text.strip().replace('\n','').replace('\r','')
                actu = p.find_element_by_css_selector('td:nth-of-type(2)').text.strip().replace(',','')
                asse = p.find_element_by_css_selector('td:nth-of-type(3)').text.strip().replace(',','')
                if actu.isdigit() and asse.isdigit():
                    property_type = prop
                    actual = actu
                    assessed = asse
                    break
            except Exception as e:
                #print (e)
                pass
                
        details.append(property_type)
        details.append(actual)
        details.append(assessed)
        details.append(total_due)
        wr.writerow(details)
    except Exception as e:
        print (e)
    #print (details)
    
login(driver, URL)
login(driver1, URL)
do_start =  0
for i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
    for j in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        
        if start_keyword == '':
            do_start = 1
            
        if not start_keyword == '' and start_keyword[0] == i and start_keyword[1] == j:
            do_start = 1
        
        if do_start == 1:
            print ('Getting accounts for keyword : ' +i+j)
            input_keywords(driver, i+j, URL)
            while True:
                account_links = driver.find_elements_by_css_selector('#searchResultsTable td strong a')
                for al in account_links:
                    lk = str(al.get_attribute('href'))
                    o = urlparse(lk)
                    query = parse_qs(o.query)
                    if 'account' in query:
                        if  query['account'][0][:1].lower() == 'r':
                            get_details(driver1, lk, WR)
                            
                next_page = str(get_next_page(driver))
                
                if not next_page == 'None':
                    print ('\t >> Next page : '+next_page)
                    driver.get(next_page)
                else:
                    break
            
            try:
                driver.find_element_by_css_selector('[href*="logout.jsp"]').click()
                login(driver, URL)
            except Exception as e:
                login(driver, URL)
            try:
                driver1.find_element_by_css_selector('[href*="logout.jsp"]').click()
                login(driver1, URL)
            except Exception as e:
                login(driver1, URL)
driver.quit()
driver1.quit()

            