from pyvirtualdisplay import Display
display = Display(visible=0, size=(1280, 1024))  
display.start()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import sys

linkedin_profile = 'https://www.linkedin.com/in/darwin-wu-35aab658/'
filename = 'output_file.html'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
driver.get('https://www.linkedin.com/fizzy/admin')
driver.delete_all_cookies()
try:
    cookies = pickle.load(open("linkedin_cookies.pkl", "rb"))
    driver.delete_all_cookies()

    for cookie in cookies:
        try:
            driver.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain', 'path')})
        except Exception as e:
            pass

except Exception as e:
    pass


driver.get(linkedin_profile)

try:
    element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "core-rail")))
    f = open(filename,'w')
    f.write(str(element.get_attribute('outerHTML').encode(sys.stdout.encoding, errors='replace')))
    f.close()
finally:
    driver.quit()
