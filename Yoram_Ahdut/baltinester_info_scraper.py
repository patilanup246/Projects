# -*- coding: utf-8 -*-
'''
Created on 24-Jan-2018

@author: Administrator
'''
import requests, csv
from pyquery import PyQuery


#driver = webdriver.Chrome(executable_path ='C:\\Users\\Administrator\\workspace\\Project\\Projects\\chromedriver\\chromedriver.exe')


# output_f = open('user_details.csv','w',encoding='utf-16', newline='')
# wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
# 
# products_url = ''
# headers = {
#     'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     'Accept-Encoding': "gzip, deflate",
#     'Accept-Language': "en-US,en;q=0.9",
#     'Cache-Control': "max-age=0",
#     'Connection': "keep-alive",
#     'Cookie': "ASP.NET_SessionId=kwfksytwyilvcw2mch3zct0r; adminUserName=Yoram; adminUserPassword=rami321; admUserId=14",
#     'Host': "www.baltinesterjewelry.com",
#     'Referer': "http://www.baltinesterjewelry.com/adminpower/websiteusersbrowse.aspx",
#     'Upgrade-Insecure-Requests': "1",
#     'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.100 Safari/537.36"
#     }
# for i in range(1,222):
#     r = requests.get('http://www.baltinesterjewelry.com/adminpower/websiteusersedit.aspx?websiteuseridtoedit='+str(i), headers=headers).text
#     pq = PyQuery(r)
#     details = []
#     print (i)
#     details.append(str(i))
#     details.append (pq('#ctl00_ContentPlaceHolder1_txtFirstName').attr('value'))
#     details.append (pq('#ctl00_ContentPlaceHolder1_txtLastName').attr('value'))
#     details.append (pq('#ctl00_ContentPlaceHolder1_txtPhone').attr('value'))
#     details.append (pq('#ctl00_ContentPlaceHolder1_txtMobile').attr('value'))
#     details.append (pq('#ctl00_ContentPlaceHolder1_txtAddress').attr('value'))
#     details.append (pq('#ctl00_ContentPlaceHolder1_txtCity').attr('value'))
#     details.append (pq('#ctl00_ContentPlaceHolder1_txtZip').attr('value'))
#     details.append (pq('#ctl00_ContentPlaceHolder1_DdlIsDivur [selected="selected"]').attr('value'))
#     details.append (pq('#ctl00_ContentPlaceHolder1_txtBirthDate').attr('value'))
#     details.append (pq('#ctl00_ContentPlaceHolder1_txtAnniversaryDate').attr('value'))
#     details.append (pq('#ctl00_ContentPlaceHolder1_DdlCountryId [selected="selected"]').text())
#     details.append (str(pq('#ctl00_ContentPlaceHolder1_DdlStateId [selected="selected"]').text()))
#     print (pq('#ctl00_ContentPlaceHolder1_DdlStateId [selected="selected"]').text())
#     details.append (pq('#ctl00_ContentPlaceHolder1_txtEmail').attr('value'))
#     details.append (pq('#ctl00_ContentPlaceHolder1_txtPassword').attr('value'))
#      
#     wr.writerow(details)
    

output_f = open('order_details.csv','w',encoding='utf-16', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
pq = PyQuery(open('Orders.html',encoding='utf-8').read())

for tr in pq('tr'):
    details = []
    for td in pq(tr)('td'):
        details.append (str(td.text).replace('\n','').replace('\r','').replace(',',';').strip())
        
    wr.writerow(details)
    
    
    