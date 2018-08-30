from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import re, sys
import csv

starting_url = input('What is the starting URL : \n')
st = input('What is the scraping type (single/multiple) : \n')
sp = input('What is the starting page : \n')
tz = input('What is the timezone : \n')
DELAY = 10


driver = webdriver.Chrome()
output_f = open('oddsportal.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['T1',	'T2',	'Date',	'Time',	'T1 (1)',	'T2 (1)',	'T1 (2)',	'T2 (2)',	'T1 (3)',	'T2 (3)',	'T1 (4)',	'T2 (4)',	'T1 (5)',	'T2 (5)',	'T1 (6)',	'T2 (6)',	'T1 (7)',	'T2 (7)',	'T1 (8)',	'T2 (8)',	'T1 (9)',	'T2 (9)', 'T1 (10)','T2 (10)','T1 (11)',	'T2 (11)','T1 (12)',	'T2 (12)',	'T1 (13)',	'T2 (13)',	'T1 (14)',	'T2 (14)',	'T1 (15)',	'T2 (15)',	'T1 (16)',	'T2 (16)',	'T1 (17)',	'T2 (17)',	'T1 (18)',	'T2 (18)',	'T1 (19)',	'T2 (19)','T1 (20)',	'T2 (20)'])


def get_all_links(scrape_type, page_num):
    ALL_LINKS = []
    start_page = page_num
    while True:
        
        driver.get(starting_url+'/#/page/{}/'.format(str(start_page)))
        
        try:
            WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#event-wait-msg-main[style="display: block;"]')))
        except Exception as e:
            print (e)

        try:
            WebDriverWait(driver, DELAY).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, '#event-wait-msg-main[style="display: block;"]')))
        except Exception as e:
            print (e)

        all_links = driver.find_elements_by_css_selector('[class="name table-participant"] a')
        for a in all_links:
            ALL_LINKS.append (a.get_attribute('href'))
        
        try:
            driver.find_element_by_css_selector('#emptyMsg [class="cms"]')
            break
        except:
            pass

        if scrape_type == 'single':
            break

        start_page+=1

    return ALL_LINKS


def change_time_zone(zoneid):
    driver.get('http://www.oddsportal.com')
    driver.get('http://www.oddsportal.com/set-timezone/{}/'.format(str(zoneid)))

def get_info(url):
    details = []
    driver.get(url)
    
    game_names = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))
    home = game_names.text.split(' - ')[0]
    away = game_names.text.split(' - ')[1]

    details.append (home)
    details.append (away)

    date_time = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.date')))
    date_string = date_time.text.split(', ')[1]
    time_string = date_time.text.split(', ')[2]
    details.append (date_string)
    details.append (time_string)

    try:
        results = WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="result"]')))
        driver.execute_script('''a = $('sup'); for (i=0;i<a.length;i++){a[i].remove()};''')
        try:
            driver.execute_script('''a = $('[class="result"] strong'); for (i=0;i<a.length;i++){a[i].remove()};''')
        except:
            pass
        
        
        for r in re.findall('\((.*?)\)',results.text):
            for a in r.split(', '):
                details.append (a.split(':')[0])
                details.append (a.split(':')[1])
    except Exception as e:
        print ('No results section')

    wr.writerow(details)

change_time_zone(int(tz))
links = get_all_links(st, int(sp))
li = 1
for link in links:
    try:
        print ('Extracting : {}/{}'.format(str(li),str(len(links))))
        print (link)
        get_info(link)
    except Exception as e:
        print (e)
    li+=1
time.sleep(5)
driver.quit()
