import time
import sqlite3
from selenium import webdriver




chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_extension('input_file/anticaptcha.crx')
chromeOptions.add_argument("--disable-setuid-sandbox")
driver = webdriver.Chrome('./input_file/chromedriver.exe',chrome_options=chromeOptions)
#driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get('chrome-extension://neodgnejhhhlcdoglifbmioajmagpeci/options.html')
driver.find_element_by_id('auto_submit_form').click()
driver.find_element_by_name('account_key').send_keys('5f6b75f0738a1bd09cf717392c9804a3')
driver.find_element_by_id('save').click()

driver.get('https://www.google.co.in/search?site=&source=hp&q=d')
#time.sleep(5)



conn = sqlite3.connect('input_file/data.db')
cursor = conn.execute("SELECT name, city, zip_code, country, state, id from DATAB where website = 'Not found'")


results = []
for row in cursor:
    r = []
    r.append(row[0])
    r.append(row[1])
    r.append(row[2])
    r.append(row[3])
    r.append(row[4])
    r.append(row[5])
    results.append(r)
    
conn.close()
conn1 = sqlite3.connect('input_file/data.db')
for row in results:

    
    try:
        print (row[0]),
        #print (row[5])
#         driver.find_element_by_css_selector('.gsfi[title="Search"]').clear()
#         driver.find_element_by_css_selector('.gsfi[title="Search"]').send_keys(
#                                                                                 str(row[0])+'  '+
#                                                                                 str(row[1])+'  '+
#                                                                                 str(row[2])+'  '+
#                                                                                 str(row[3])+'  '+
#                                                                                 str(row[4])
#                                                                                 )
        driver.get('https://www.google.co.in/search?site=&source=hp&q='+str(row[0])+'  '+
                                                                                str(row[1])+'  '+
                                                                                str(row[2])+'  '+
                                                                                str(row[3])+'  '+
                                                                                str(row[4]))
        
        
        #driver.find_element_by_css_selector('.gsfi[title="Search"]').send_keys(Keys.RETURN)
        #time.sleep(50)
        
        try:
            #element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, "rhs_block")))
            try:
                conn1.execute("UPDATE DATAB set phone_google = '"+str(driver.find_element_by_css_selector('span._Xbe._ZWk.kno-fv [data-dtype="d3ph"] span').text)+"' where id = '"+row[5]+"'")
                conn1.commit()           
            except Exception as e:
                conn1.execute("UPDATE DATAB set phone_google = 'Not found' where id = '"+row[5]+"'")
                conn1.commit()   
                #print (e)
                pass
            try:
                conn1.execute("UPDATE DATAB set website = '"+str(driver.find_element_by_css_selector('._b1m.kp-hc a.ab_button[role="button"]').get_attribute('href'))+"' where id = '"+row[5]+"'")
                #conn1.execute("UPDATE DATAB set website = '"+str(driver.find_element_by_xpath('//*[@class="fl"][contains(text(), "Website")]').get_attribute('href'))+"' where id = '"+row[5]+"'")
                print (str(driver.find_element_by_css_selector('._b1m.kp-hc a.ab_button[role="button"]').get_attribute('href')))
                conn1.commit()
            except Exception as e:
                conn1.execute("UPDATE DATAB set website = 'Not found-2' where id = '"+row[5]+"'")
                conn1.commit()
                print ('website not found-2')
                pass
        except Exception as e:
            print (e)
            pass
    except Exception as e:
        print (e)
        pass
#     finally:
#         driver.quit()
conn1.close()
