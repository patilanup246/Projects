from selenium import webdriver
import time
import csv
import glob
import os
from time import gmtime, strftime

 
USER_NAME = 'andrewellis3@aol.com'
PASSWORD = 'starsky69--'
 
current_time = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
 
 
all_urls = open('ahrefs_input_urls.txt').read().split('\n')
 
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory" : os.getcwd()+'\\'+current_time
    }
# chrome_options.add_argument("no-sandbox")
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://ahrefs.com/user/login')
 
driver.find_element_by_css_selector('[name="email"]').send_keys(USER_NAME)
driver.find_element_by_css_selector('[name="password"]').send_keys(PASSWORD)
driver.find_element_by_css_selector('[value="Sign in"]').click()
time.sleep(5)
try:
    driver.find_element_by_css_selector('#top_notifications').click()
    time.sleep(2)
    driver.find_element_by_css_selector('.export-notifications__list--removeall--link').click()
    time.sleep(2)
    driver.find_element_by_css_selector('''[onclick="$('#removeNotificationsModal').modal('hide');deleteCSVFile('all');"]''').click()
except:
    pass
 
for url in all_urls:
    driver.get('https://ahrefs.com/site-explorer/backlinks/v5/external-per-domain/subdomains/live/all/all/1/ahrefs_rank_desc?target='+str(url))
     
    time.sleep(5)
    driver.find_element_by_css_selector('[class="export-data "]').click()
     
    time.sleep(10)
     
    driver.execute_script("$('#start_full_export').click()")
     
    time.sleep(5)
     
    driver.execute_script("$('#start_export_button').click()")
     
    time.sleep(5)
 
time.sleep(10)




for file in driver.find_elements_by_css_selector('#top_notifications_files [name="link_to_download"]'):
    driver.execute_script('arguments[0].click()',file)
    time.sleep(10)
 
 
time.sleep(100)

driver.quit()

# is_first = 1
# csv_csv = []
# 
# final_output = open('final_output.csv','w',encoding='utf-8', newline='')
# wr_final = csv.writer(final_output, quoting=csv.QUOTE_ALL)
# 
# for i in glob.glob(os.getcwd()+'\\'+'2018-05-15-18-42-53'+"\\*.csv"):
#     print(i)
#     readCSV1 = csv.reader(open(i,encoding='utf-8'), delimiter=',')
#     m = 0
#     for row in readCSV1:
#         if is_first and m == 0:
#             csv_csv.append(row)
#             is_first = 0
#         if m > 0:
#             csv_csv.append(row)
#         m+=1
# 
# for c in csv_csv:
#     wr_final.writerow(c)
# final_output.close()