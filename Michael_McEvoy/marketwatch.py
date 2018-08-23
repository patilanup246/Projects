'''
Created on Aug 2, 2018

@author: tasneem
'''

import requests
import csv
import time




TIME_INTERVAL = 60


while True:

    output_f = open('marketwatch_output.csv','w',encoding='utf-8', newline='')
    wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
    wr.writerow(['SPX',    'DJIA',    'NDX',    'RUT',    'BKTEM',    'EFA',    'TLT'])
    
    
    item_list = [
                "INDEX/US//SPX",
                "INDEX/US//DJIA",
                "INDEX/US/XNAS/NDX",
                "INDEX/US//RUT",
                "INDEX/XX//BKTEM",
                "FUND/US/ARCX/EFA",
                "FUND/US/XNAS/TLT"
                ]
    
    
    def get_data(item):
    
        url = "https://www.marketwatch.com/watchlist/app/quotesandheadlines"
        
        payload={
                  "symbols": [
                    item
                  ]
                }
        headers = {
            'accept': "*/*",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US,en;q=0.9",
            'content-type': "application/json",
            'origin': "https://www.marketwatch.com",
            'referer': "https://www.marketwatch.com/watchlist",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            'x-requested-with': "XMLHttpRequest"
            }
        
        response = requests.request("POST", url, json=payload, headers=headers)
        
        return(response.json()[0]['Quote']['LiveData']['Price'])
      
    details = []
    for i in item_list:   
        details.append (get_data(i))
        
    wr.writerow(details)
    
    time.sleep(TIME_INTERVAL)
    
    if not TIME_INTERVAL:
        break