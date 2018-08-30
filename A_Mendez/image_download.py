from selenium import webdriver
import time, pyautogui
driver = webdriver.Chrome()

time.sleep(60)

driver.get('https://www.adviserinfo.sec.gov/')

time.sleep(20)





for a in open('input_crns.txt').read().split('\n'):
    driver.find_element_by_css_selector('[title="Individual"]').clear()
    driver.find_element_by_css_selector('[title="Individual"]').send_keys(str(a))
    driver.find_element_by_css_selector('[class="usa no-print"]').click()

    time.sleep(0.15)
    c = pyautogui.screenshot()
    
    # Save the image
    c.save('images/'+str(a)+'.png')
