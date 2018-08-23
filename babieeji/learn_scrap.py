# -*- coding: utf-8 -*-
'''
Created on Aug 13, 2018

@author: tasneem
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


'''

* matches all
^ matches start
$ matches end

[class ^= "value"]
[class $= "value"]
[class *= "value"]

#by_id
css_selector ('#home')
css_selector ('[id="home"]')

#by_class
css_selector ('.nav')
css_selector ('[class= "nav"]')

#by_css_selector
css_selector ('[talib="mukadam"]')
'''

sq = 'wikipedia python'

driver = webdriver.Chrome()
 
#creating a list array to store all the links text
# links_text = []
#  
# #open the given url and search (search_query)
# driver.get('https://www.google.co.in/search?q=' + sq)
#  
# #variable(links_all) will store the links found by 'class'
# links_all = driver.find_elements_by_css_selector('[class="rc"] h3 a')
# for link in links_all:
#     #links found will get stored in list array(links_text) 
#     links_text.append(link.get_attribute("href"))
#  
#  
# print(links_text)


# link = ''
# driver.get('https://www.google.co.in/search?q=' + sq)
# 
# 
# link = driver.find_element_by_css_selector('[class="rc"] h3 a')#.get_attribute('href')
# 
# # for l in link:
# #     print (l.get_attribute('href'))
# 
# link.click()
# #driver.get(link.get_attribute('href'))
# #print(link)
# 
# f= open("result.txt","w+")
# String = ''
# strText = driver.find_element_by_css_selector('[id="toc"]')
# f.write(str(strText))



# f= open("result.txt","w+")
# driver.get('https://vancouver.craigslist.ca/')
# # driver.find_element_by_css_selector('[class="ela"]').click()
# # posts = driver.find_elements_by_css_selector('[class="result-title hdrlnk"]')
# # # for post in posts:
# # #     #print(post.text)
# # #     f.write(str(post.text))
# #  
# # driver.find_element_by_css_selector('a[class="button next"]').click()
# 
# driver.find_element_by_css_selector('[class="apa"]').click()
# posts2= driver.find_elements_by_css_selector('[class="result-title hdrlnk"]')
# for post in posts2:
#     print(post.text)

all_shows = []
driver.get('http://thehobbycenter.org/index.php?q=node/133')
all_shows = driver.find_elements_by_css_selector('[class="views-field-title"]')
# for shows in all_shows:
#     print(shows.text)

# driver.find_element_by_css_selector('[href="http://www.thehobbycenter.org/?q=node/2328"]').click()
# title = driver.find_element_by_css_selector('[class="title"]')
# print(title)
all_results = ['duration', 'date']
# title = driver.find_elements_by_css_selector('[class="view view-all-shows view-id-all_shows view-display-id-page_1 view-dom-id-1"] [class="views-field-title"]')
duration = driver.find_elements_by_css_selector('[class="view view-all-shows view-id-all_shows view-display-id-page_1 view-dom-id-1"] [class="views-field-field-duration-value"]')
# content = driver.find_elements_by_css_selector('[class="view view-all-shows view-id-all_shows view-display-id-page_1 view-dom-id-1"] [class="field-content"]')
date = driver.find_elements_by_css_selector('[class="view view-all-shows view-id-all_shows view-display-id-page_1 view-dom-id-1"] [class="date-display-single"]')
# hall_value = driver.find_elements_by_css_selector('[class="view view-all-shows view-id-all_shows view-display-id-page_1 view-dom-id-1"] [class="views-field-field-hall-value"]')
# learn_more_link = driver.find_elements_by_css_selector('[class="view view-all-shows view-id-all_shows view-display-id-page_1 view-dom-id-1"] [class="views-field-field-learn-url"]')


for events in all_results:
    print(events.text)


time.sleep(5)
driver.quit()
