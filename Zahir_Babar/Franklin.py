'''
Created on 12-Dec-2017

@author: Administrator
'''
import requests
from flask import Flask, request
app = Flask(__name__)
import json


@app.route('/get_reports')
def hello_world():
    report_name = request.args.get('report_name')
    start_date = request.args.get('start_date').split('_')
    end_date = request.args.get('end_date').split('_')

    start_date = '/'.join(start_date)
    end_date   = '/'.join(end_date)
    try:
        return call_reports(report_name,start_date,end_date)
    
    except Exception as e:
        return 'Something went wrong with the request \n '+str(e)
    
    


def call_reports(report_name, start_date, end_date):
    url = "https://api.franklintempleton.com/v1/ide/services/reportMailback"
    
    querystring = {"distId":"ARN-69442","emailId":"redmoneyindore@gmail.com","userType":"90"}
    
    if report_name == 'my_transaction':
        payload = {"reports": [{"emailId": "redmoneyindore@gmail.com","reportId": "50","fromDate": start_date,"toDate": end_date,"format": "DBF"}]}
    
    if report_name == 'active_sip':
        payload = {"reports": [{"emailId": "redmoneyindore@gmail.com","reportId": "744","fromDate": start_date,"toDate": end_date,"format": "DBF"}]}
    
    if report_name == 'closed_sip':    
        payload = {"reports": [{"emailId": "redmoneyindore@gmail.com","reportId": "743","fromDate": start_date,"toDate": end_date,"format": "DBF"}]}
    
    if report_name == 'investor_folio':
        payload = {"reports": [{"emailId": "redmoneyindore@gmail.com","reportId": "160","fromDate": start_date,"toDate": end_date,"format": "DBF"}]}
    
    if report_name == 'client_wise':
        payload = {"reports": [{"emailId": "redmoneyindore@gmail.com","reportId": "100","fromDate": start_date,"toDate": end_date,"format": "DBF","value": 0}]}
    
    
    headers = {
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9",
        'Connection': "keep-alive",
        'Content-Length': "129",
        'Content-Type': "application/json;charset=UTF-8",
        'Host': "api.franklintempleton.com",
        'Origin': "https://accounts.franklintempletonindia.com",
        'Referer': "https://accounts.franklintempletonindia.com/guest/",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.70 Safari/537.36"
    }
    
    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    
    resp = json.loads(response.text)
    
    try:
        return (resp['status'])
    except Exception as e:
        return  (resp[0]['errorDescription'])
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)