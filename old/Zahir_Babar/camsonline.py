'''
Created on 16-Dec-2017

@author: Administrator
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

base_url = 'https://www.camsonline.com/DistributorServices/COL_Mailbackservice.aspx'

funds = [
    'B \ Aditya Birla Sun Life Mutual Fund',
    'H \ HDFC Mutual Fund',
    'P \ ICICI Prudential Mutual Fund',
    'L \ SBI Mutual Fund',
    'BG \ Birla Gold and Precious Metals',
    'D \ DSP BlackRock Mutual Fund',
    'O \ HSBC Mutual Fund',
    'G \ IDFC Mutual Fund',
    'IF \ IIFL Mutual Fund',
    'K \ Kotak Mahindra Mutual Fund',
    'F \ L&T Mutual Fund',
    'MM \ Mahindra Mutual Fund',
    'PP \ PPFAS Mutual Fund',
    'RM \ Reliance Money Precious Metals',
    'SH \ Shriram Mutual Fund',
    'T \ TATA Mutual Fund',
    'UK \ Union Mutual Fund'
    
    ]

report_name = 'Investor Transactions for a Period'
output_format = 'TXT' #DBF,TXT,TXTWH,CSV,CSVWH,XLS,XLSWH
delivery_format = 'DOWNLINK' #SENDATTACH

start_date ='16_December_2017'
end_date ='16_December_2017'



def select_multiple(driver,values):
    for value in values:
        element = driver.find_element_by_xpath("//*[contains(text(), '{}')]".format(value))
        ActionChains(driver) \
            .key_down(Keys.CONTROL) \
            .click(element) \
            .key_up(Keys.CONTROL) \
            .perform()
            
def select_report(driver,report_name):
    driver.find_element_by_xpath("//*[contains(text(), '{}')]/input".format(report_name)).click()

            
def select_output_format(driver, output_format):
    driver.find_element_by_css_selector('[value="{}"]'.format(output_format)).click()
    
def select_delivery_format(driver,delivery_format):
    driver.find_element_by_css_selector('[value="{}"]'.format(delivery_format)).click()

driver = webdriver.Chrome()
driver.get(base_url)
driver.find_element_by_css_selector('#txtemail').send_keys('redmoneyindore@gmail.com')
select_multiple(driver,funds)
driver.find_element_by_css_selector('#btnNext').click()

try:
    select_report(driver,report_name)
except Exception as e:
    print ('No such report as {}'.format(report_name))
    


try:
    select_output_format(driver,output_format)
except Exception as e:
    print ('No such report as {}'.format(report_name))
    


try:
    select_delivery_format(driver,delivery_format)
except Exception as e:
    print ('No such report as {}'.format(report_name))
    

driver.find_element_by_css_selector('#btnnext').click()
