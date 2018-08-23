# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://www.superatv.com/1-75-2-cage-light-mounting-brackets')

# images = driver.find_elements_by_css_selector('[class="fotorama__img"]')
# 
# # print(image.get_attribute('src'))
# for image in images:
#     print(image.get_attribute('src'))
# 
# title = driver.find_element_by_css_selector('[class="page-title"]').text
# price = driver.find_element_by_css_selector('[class="price"]').text
# details = driver.find_element_by_css_selector('[class="stacked details"]').text
# fitment = driver.find_element_by_css_selector('[class="stacked fitment"]').text
# features = driver.find_element_by_css_selector('[class="stacked features"]').text

# option = Select(driver.find_element_by_css_selector('[class="super-attribute-select"]'))
# option.select_by_index(1)
# print(option.text)
# print(title,'\n\n', price,'\n\n', details,'\n\n', fitment,'\n\n', features, '\n\n')


select_opt = driver.find_element_by_css_selector('[class="super-attribute-select"]')
options = Select(select_opt.select_by_index(1))
print(select_opt.text)










time.sleep(5)
driver.quit()