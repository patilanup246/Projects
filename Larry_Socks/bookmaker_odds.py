from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import re, sys
import csv

# starting_url = input('What is the starting URL : \n')
# st = input('What is the scraping type (single/multiple) : \n')
# sp = input('What is the starting page : \n')
# tz = input('What is the timezone : \n')

DELAY = 10

output_f = open('oddsportal.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Category',	'Opening Odds Time (T1)',	'Opening Odds (T1)',	'Closing Odds Time (T1)',	'Closing Odds (T1)', 'Opening Odds Time (T2)',	'Opening Odds (T2)',	'Closing Odds Time (T2)',	'Closing Odds (T2)'])


driver = webdriver.Chrome()



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



change_time_zone(int(tz))
links = get_all_links(st, int(sp))


driver.get('http://www.oddsportal.com/basketball/usa/nba-2017-2018/cleveland-cavaliers-golden-state-warriors-QoC4sAGp/#over-under;3')

try:
    WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#event-wait-msg-main[style="display: block;"]')))
except Exception as e:
    print (e)

try:
    WebDriverWait(driver, DELAY).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, '#event-wait-msg-main[style="display: block;"]')))
except Exception as e:
    print (e)


for a in driver.find_elements_by_css_selector('[class="more"]'):
    try:
        a.click()
    except Exception as e:
        print (e)


for b in driver.find_elements_by_css_selector('[class="table-container"]'):
    
    cat = b.find_element_by_css_selector('div>strong').text
    
    for a in b.find_elements_by_css_selector('tr.lo'):
        
        try:
            bookmaker_name = a.find_element_by_css_selector('[class="name"]').text
        except:
            continue
        if 'Pinnacle'.lower() == bookmaker_name.lower():

            details = []

            details.append(cat.strip())
            print (cat.strip())

            element_to_hover_over = a.find_element_by_css_selector('.odds:nth-child(3)')
            hover = ActionChains(driver).move_to_element(element_to_hover_over)
            hover.perform()

            T1 = driver.find_element_by_css_selector('[id="tooltiptext"]').text
            T1_closing_odds =  T1.split('Opening odds:')[0].split('\n')[0].strip()
            if T1_closing_odds:
                details.append(" ".join(T1_closing_odds.split(" ")[:3]))
                details.append(T1_closing_odds.split(" ")[3])
            else:
                details.append('')
                details.append('')
            
            T1_opening_odds =  T1.split('Opening odds:')[1]
            if T1_opening_odds:
                details.append(" ".join(T1_opening_odds.split(" ")[:3]).replace('\n',''))
                details.append(T1_opening_odds.split(" ")[3])
            else:
                details.append('')
                details.append('')

            element_to_hover_over = a.find_element_by_css_selector('.odds:nth-child(4)')
            hover = ActionChains(driver).move_to_element(element_to_hover_over)
            hover.perform()

            T2 = driver.find_element_by_css_selector('[id="tooltiptext"]').text
            T2_closing_odds = T2.split('Opening odds:')[0].split('\n')[0].strip()
            if T2_closing_odds:
                details.append(" ".join(T2_closing_odds.split(" ")[:3]))
                details.append(T2_closing_odds.split(" ")[3])
            else:
                details.append('')
                details.append('')

            T2_opening_odds = T2.split('Opening odds:')[1].strip()
            if T2_opening_odds:
                details.append(" ".join(T2_opening_odds.split(" ")[:3]))
                details.append(T2_opening_odds.split(" ")[3])
            else:
                details.append('')
                details.append('')
            wr.writerow(details)




