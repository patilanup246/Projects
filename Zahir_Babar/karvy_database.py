'''
Created on Apr 2, 2018

@author: talib
'''
import MySQLdb
import time
import threading
from queue import Queue
from selenium import webdriver
import requests
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import re
lock = threading.Lock()
import shutil
from pyvirtualdisplay import Display
  
display = Display(visible=0, size=(1280, 1024))
display.start()

DB_ADDRESS = "35.154.103.232"
DB_USER = "office_eoffice"
DB_PASS = "thegolden123"
DB_NAME = "office_nw"

KARVY_USER = 'redltd891'
KARVY_PASS = 'karvy123'

#CAMS_USER = 'BACC'
#CAMS_PASS = 'Cams123@'

CAMS_USER = 'SVSD'
CAMS_PASS = 'Sunil@1979'

SUNDARAM_USER = 'ARN-69442'
SUNDARAM_PASS = 'redmoney@12'

OUTPUT_DIRECTORY = "/opt/tomcat/webapps/ROOT/output/"
#OUTPUT_DIRECTORY = 'output/'

KARVY_THREADS = 1
CAMS_THREADS = 1
SUNDARAM_THREADS = 1

POLLING_TIME = 600


def start_webdriver_karvy():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.images': 2})
    #return webdriver.Chrome(chrome_options=chrome_options)
    return webdriver.Chrome('./chromedriver',chrome_options=chrome_options, service_args=["--verbose","--log-path=script_logs_karvy.log"])
    
    
def start_webdriver_cams(id1, folio_num):
    site_name = str(id1)+'_'+str(folio_num)
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory" : os.getcwd()+'\\CAMS\\'+site_name.replace('/',''),
        'profile.managed_default_content_settings.images': 2
        }
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_experimental_option("prefs",prefs)
    #return webdriver.Chrome(chrome_options=chrome_options)
    return webdriver.Chrome('./chromedriver',chrome_options=chrome_options, service_args=["--verbose","--log-path=script_logs_cams.log"])

def start_webdriver_sundaram(id1, folio_num):
    site_name = str(id1)+'_'+str(folio_num)
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory" : os.getcwd()+'\\SUNDARAM\\'+site_name
        }
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_argument("no-sandbox")
    #return webdriver.Chrome(chrome_options=chrome_options)
    return webdriver.Chrome('./chromedriver',chrome_options=chrome_options, service_args=["--verbose", "--log-path=script_logs_sundaram.log"])
    
    
def login_karvy(driver,user,pass1):
    driver.get('https://www.karvymfs.com/karvy/Distributor/Distributor_Login.aspx')
    driver.find_element_by_css_selector('[name="txtUserId"]').send_keys(user)
    driver.find_element_by_css_selector('[name="txtPassword"]').send_keys(pass1)
    driver.find_element_by_css_selector('[name="btnSubmit"]').click()

def login_cams(driver,user, pass1):
    driver.get('https://fundsnet.camsonline.com/eCRMS/index.aspx')
    driver.find_element_by_css_selector('[name="UserCode"]').send_keys(user)
    driver.find_element_by_css_selector('[name="UserPwd"]').send_keys(pass1)
    driver.find_element_by_css_selector('[alt="Login"]').click()

def login_sundaram(driver,user, pass1):
    driver.get('https://www.sundarambnpparibasfs.in/distributorservices/?amcid=bnpss')
    driver.find_element_by_css_selector('[class="iceInpTxt"]').send_keys(user)
    driver.find_element_by_css_selector('[class="iceInpSecrt"]').send_keys(pass1)
    driver.find_element_by_css_selector('[class="iceCmdBtn button"]').click()



def get_report_karvy(driver, folio_num,pdf,type_file,user,pass1):
    login_karvy(driver,user,pass1)
    driver.get('https://www.karvymfs.com/karvy/Distributor/Query/QueryNew.aspx')
    if 'Query New' in driver.title: 
        select = Select(driver.find_element_by_css_selector('[name="ctl00$MiddleContent$ddlfunds"]'))
        select.select_by_value(type_file)
        
        driver.find_element_by_css_selector('[name="ctl00$MiddleContent$txtAcNo"]').send_keys(folio_num)
        driver.find_element_by_css_selector('[name="ctl00$MiddleContent$btnQuery"]').click()
        
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="ctl00_MiddleContent_dgQueryDets"] tbody tr:nth-of-type(2) td:nth-of-type(4) a[href]')))
        element.click()
        
        try:
            element2 = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="rdDetailed"]')))
            element2.click()
        except Exception as e:
            pass
        
        time.sleep(0.3)
        element3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="chkAllItems"]')))
        element3.click()
        
        element4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="btnViewAndPrint"]')))
        element4.click()
        
        element_frame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="hidName"][value]')))
        pdf = str(element_frame.get_attribute('value'))
        return pdf



def get_report_cams(driver, folio_num,acc,user,pass1):
    login_cams(driver,user,pass1)
    
    driver.find_element_by_css_selector('[href*="BOL_InvLocate.aspx"]').click()
    
    driver.find_element_by_css_selector('[name="txtFolionoloc"]').send_keys(folio_num)
    
    
    select = Select(driver.find_element_by_css_selector('[name="drpfundfolio"]'))
    select.select_by_value(acc)
    

    driver.find_element_by_css_selector('[name="btnGofolio"]').click()
    
    page_sour = driver.page_source
    driver.get('https://fundsnet.camsonline.com/eCRMS/BrokerOnlineSite/BrokerOnline/'+str(re.findall("var qry = '(.*?)';", page_sour)[0]))
    
    driver.find_element_by_css_selector('[name="rdStmtType"][value="FULL"]').click()
    driver.find_element_by_css_selector('[name="btnview"]').click()
    
    time.sleep(3)
    
def get_report_sundaram(driver, folio_num, tried,user,pass1):

    login_sundaram(driver,user,pass1)
       
    element_0 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[src="images/report.jpg"]')))
    element_0.click()
    
    element_1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="searchBrokF:investorsoafolio2:_2"]')))
    element_1.click()
    
    element_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="searchBrokF:textfolio"]')))
    element_2.send_keys(folio_num)
    time.sleep(0.5)
    element_3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name*="searchBrokF:j_idt"]')))
    element_3.click()
    time.sleep(0.5)
    element_3.click()
    time.sleep(0.5)
    element_4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="searchBrokF:SlctSoaBrokerM:_4"]')))
    element_4.click()
    time.sleep(0.5)
    element_5 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="searchBrokF:SlctFileModeBrokerM:_2"]')))
    element_5.click()
    time.sleep(0.5)
    element_6 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="searchBrokF:j_idt232"]')))
    element_6.click()
    
    time.sleep(3)
    

def update_table_karvy(report_url, id1, folio_num):

    db = MySQLdb.connect(DB_ADDRESS,DB_USER,DB_PASS,DB_NAME )
    cursor = db.cursor()

    if folio_num:   
        r = requests.get('https://www.karvymfs.com/karvy/Distributor/Query/'+report_url)
        with open('KARVY/'+str(id1)+'_'+str(folio_num)+'.pdf', 'wb') as f:  
            f.write(r.content)
        shutil.move(os.path.join('KARVY/', str(id1)+'_'+str(folio_num)+'.pdf'), OUTPUT_DIRECTORY+str(id1)+'_'+str(folio_num)+'.pdf')
        sql_download_url = "UPDATE soa_requests SET download_url = '{}'   WHERE id = {};".format(str(id1)+'_'+str(folio_num)+'.pdf',id1)
        sql_status = "UPDATE soa_requests SET status = {}   WHERE id = {};".format(1,id1)
    else:
        sql_download_url = "UPDATE soa_requests SET download_url = '{}'   WHERE id = {};".format(report_url,id1)
        sql_status = "UPDATE soa_requests SET retry_counter = retry_counter + 1   WHERE id = {};".format(id1)
        
    try:
        cursor.execute(sql_download_url)
        cursor.execute(sql_status)
        db.commit()
    except Exception as e:
        print (e)
        db.rollback()
            
    db.close()
    
def update_table_cams(report_url, id1, folio_num):
    db = MySQLdb.connect(DB_ADDRESS,DB_USER,DB_PASS,DB_NAME )
    cursor = db.cursor()

    if folio_num:   
        sql_download_url = "UPDATE soa_requests SET download_url = '{}'   WHERE id = {};".format(str(id1)+'_'+str(folio_num).replace('/','')+'.pdf',id1)
        sql_status = "UPDATE soa_requests SET status = {}   WHERE id = {};".format(1,id1)
        
        try:
            site_name = str(id1)+'_'+str(folio_num)
            site_name = site_name.replace('/','')
            path =  os.getcwd()+'\\CAMS\\'+site_name.replace('/','')
            for file in os.listdir(path):
                os.rename(os.path.join(path, file), os.path.join(path, site_name+'.pdf'))
                shutil.move(os.path.join(path, site_name+'.pdf'), OUTPUT_DIRECTORY+site_name+'.pdf')
        except Exception as e:
            print (e)
        
    else:
        sql_download_url = "UPDATE soa_requests SET download_url = '{}'   WHERE id = {};".format(report_url,id1)
        sql_status = "UPDATE soa_requests SET retry_counter = retry_counter + 1   WHERE id = {};".format(id1)
        
    try:
        cursor.execute(sql_download_url)
        cursor.execute(sql_status)
        db.commit()
    except Exception as e:
        print (e)
        db.rollback()
            
    db.close()
    
    
def update_table_sundaram(report_url, id1, folio_num):
    db = MySQLdb.connect(DB_ADDRESS,DB_USER,DB_PASS,DB_NAME )
    cursor = db.cursor()

    if folio_num:   
        sql_download_url = "UPDATE soa_requests SET download_url = '{}'   WHERE id = {};".format(str(id1)+'_'+str(folio_num).replace('/','')+'.pdf',id1)
        sql_status = "UPDATE soa_requests SET status = {}   WHERE id = {};".format(1,id1)
        
        try:
            site_name = str(id1)+'_'+str(folio_num)
            path =  os.getcwd()+'\\SUNDARAM\\'+site_name
            print (os.listdir(path))
            for file in os.listdir(path):
                print (file)
                os.rename(os.path.join(path, file), os.path.join(path, site_name+'.pdf'))
                shutil.move(os.path.join(path, site_name+'.pdf'), OUTPUT_DIRECTORY+site_name+'.pdf')
        except Exception as e:
            print (e)
        
    else:
        sql_download_url = "UPDATE soa_requests SET download_url = '{}'   WHERE id = {};".format(report_url,id1)
        sql_status = "UPDATE soa_requests SET retry_counter = retry_counter + 1   WHERE id = {};".format(id1)
        
    try:
        cursor.execute(sql_download_url)
        cursor.execute(sql_status)
        db.commit()
    except Exception as e:
        print (e)
        db.rollback()
            
    db.close()




def worker_karvy(q):
    is_instantiated = 0

    while not q.empty():
        try:
            t = q.get()
            DRIVER = start_webdriver_karvy()
            is_instantiated = 1
            pdf_file = ''
            pdf_file = get_report_karvy(DRIVER, str(t[1]),pdf_file,t[2],t[3],t[4])
            update_table_karvy(pdf_file, t[0],t[1])
        except Exception as e:
            update_table_karvy(str(e), t[0],'')
            print (e)
        finally:
            if is_instantiated == 1:
                DRIVER.quit()
            q.task_done()
            
def worker_cams(q):
    is_instantiated = 0

    while not q.empty():
        try:
            t = q.get()
            DRIVER = start_webdriver_cams(t[0], t[1])
            is_instantiated = 1
            get_report_cams(DRIVER, t[1],t[2],t[3],t[4])
            update_table_cams('', t[0],t[1])
        except Exception as e:
            update_table_cams(str(e), t[0],'')
            print (e)
        finally:
            if is_instantiated == 1:
                time.sleep(3)
                DRIVER.quit()
            q.task_done()
            
def worker_sundaram(q):
    is_instantiated = 0

    while not q.empty():
        try:
            t = q.get()
            DRIVER = start_webdriver_sundaram(t[0], t[1])
            is_instantiated = 1
            get_report_sundaram(DRIVER, t[1],t[2],t[3],t[4])
            
            update_table_sundaram('', t[0],t[1])
        except Exception as e:
            update_table_sundaram(str(e), t[0],'')
            print (e)
        finally:
            if is_instantiated == 1:
                time.sleep(3)
                DRIVER.quit()
            q.task_done()

    
    
while True:
    q_karvy = Queue()
    q_cams = Queue()
    q_franklin = Queue()
    q_sundaram = Queue()
    
    db = MySQLdb.connect(DB_ADDRESS,DB_USER,DB_PASS,DB_NAME)
    cursor = db.cursor()
    cursor.execute("SELECT SR.id, SR.folio_number,SR.amc_code, NOA.karvy_uname, NOA.karvy_pwd from soa_requests as SR INNER JOIN no_of_arn as NOA ON NOA.arn_no = SR.arn_no where SR.data_type = 'karvy' and SR.status = 0 and SR.retry_counter <=3 and NOA.karvy_uname != '' and NOA.karvy_pwd != ''")
    rows = cursor.fetchall()
    for row in rows:
        print (row)
        q_karvy.put(row)
    db.close()
     
     
    db = MySQLdb.connect(DB_ADDRESS,DB_USER,DB_PASS,DB_NAME)
    cursor = db.cursor()
    cursor.execute("SELECT SR.id, SR.folio_number,SR.amc_code, NOA.cams_fundsnet_id, NOA.cams_fundsnet_pwd from soa_requests as SR INNER JOIN no_of_arn as NOA ON NOA.arn_no = SR.arn_no where SR.data_type = 'cams' and SR.status = 0 and SR.retry_counter <=3 and NOA.cams_fundsnet_id != '' and NOA.cams_fundsnet_pwd != ''")
    rows = cursor.fetchall()
    for row in rows:
        print (row)
        q_cams.put(row)
    db.close()
    
    
    db = MySQLdb.connect(DB_ADDRESS,DB_USER,DB_PASS,DB_NAME)
    cursor = db.cursor()
    cursor.execute("SELECT SR.id, SR.folio_number,SR.amc_code, NOA.sbn_uname, NOA.sbn_pwd from soa_requests as SR INNER JOIN no_of_arn as NOA ON NOA.arn_no = SR.arn_no where SR.data_type = 'bnp' and SR.status = 0 and SR.retry_counter <=3 and NOA.sbn_uname != '' and NOA.sbn_pwd != ''")
    rows = cursor.fetchall()
    for row in rows:
        print (row)
        q_sundaram.put(row)
    db.close()
#     
#     
#     db = MySQLdb.connect(DB_ADDRESS,DB_USER,DB_PASS,DB_NAME)
#     cursor = db.cursor()
#     cursor.execute("SELECT id, folio_number,amc_code from soa_requests where data_type = 'franklin' and status = 0")
#     rows = cursor.fetchall()
#     for row in rows:
#         print (row)
#         q_franklin.put(row)
#     db.close()
    
    
    
    
    
    for i in range(KARVY_THREADS):
        t = threading.Thread(target=worker_karvy, args=(q_karvy, ))
        t.start()  
     
     
    for i in range(CAMS_THREADS):
        t = threading.Thread(target=worker_cams, args=(q_cams, ))
        t.start()
         
    for i in range(SUNDARAM_THREADS):
        t = threading.Thread(target=worker_sundaram, args=(q_sundaram, ))
        t.start()
        
    q_karvy.join()
    q_cams.join()
    q_sundaram.join()
    
    
    
    
    time.sleep(POLLING_TIME)
