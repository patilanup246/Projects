'''
Created on 12-Dec-2017

@author: Administrator
'''
import requests
from flask import Flask, request
app = Flask(__name__)
import json
from subprocess import Popen, PIPE, STDOUT

import urllib.parse
from pyquery import PyQuery
@app.route('/get_reports')

def hello_world():
    #report_name = request.args.get('report_name')
    start_date = request.args.get('start_date').split('_')
    end_date = request.args.get('end_date').split('_')

    start_date = '-'.join(start_date)
    end_date   = '-'.join(end_date)
    try:
        return call_reports(start_date,end_date)
    
    except Exception as e:
        return 'Something went wrong with the request \n '+str(e)
    
    


def call_reports(start_date, end_date):
    import requests
    p = Popen(['java', '-jar', './cams_decode.jar',start_date,end_date], stdout=PIPE, stderr=STDOUT)
    for line in p.stdout:
        t =  line
    url = "https://www.camsonline.com/DistributorServices/COL_DisMailSend.aspx"
    print (t)
    viewstate = t.decode("utf-8").replace('\n','').replace('\r','')
    print (viewstate)
    viewstate = urllib.parse.quote_plus(viewstate)
    payload = "__LASTFOCUS=&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATEGENERATOR=DF4ABE4F&__PREVIOUSPAGE=4YyJnQNFbTT9PubnOOSeE3xHP9_XgcjUBVtcKsteNbljjod8wBuWALumOA-z-C98sr4axWLiGBqtYYFB-DWHCYjuqqZz3LhWwgrk4nXtIsKlaqMAGwst8xPumDepYaLOg7vQoUljadeQ3ikuXbB2lw2&ctl00%24PageContent%24txtqrypass=cams123&ctl00%24PageContent%24txtqryrepass=cams123&ctl00%24PageContent%24imgbtnImmediate.x=53&ctl00%24PageContent%24imgbtnImmediate.y=18&ctl00%24PageContent%24hinvfrmdate=&ctl00%24PageContent%24hinvtodate=&ctl00%24PageContent%24hemail=redmoneyindore%40gmail.com&ctl00%24PageContent%24hamc=&ctl00%24PageContent%24hqry=WBR2&ctl00%24PageContent%24hsqlqry=qry%3AWBR2%3B%20brktype%3ARIA%3B%20schemes%3A%3B&fromdt=5-Jan-2018%3B%20todt%3A31-Jan-2018%3B%20relativedateperiod%3A0%3B&brokcode=%3B%20tradetype%3A'P'%2C'JP'%2C'DR'%2C'DP'%2C'DA'%2C'R'%2C'JR'%2C'SI'%2C'SO'%2C'JS'%2C'TI'%2C'TO'%2C'JT'%3B&subbrok=%3B%20trxnsubtype%3A%3B&operator=%3E%3D%3B%20amount%3A0%3B&email=redmoneyindore%40gmail.com%3B%20pertype%3A%3B&relativedatetype=D%3B%20folio%3A%3B%20seq_no%3A%3B&taxstatus=%3B&exclticob=N%3B&custom_column=%3B%20price_deci%3A%3B%20unitdeci%3A%3B&saveformat=XLSWH%3B%20deliveropt%3ADOWNLINK%3B&SFTP=%3B&ctl00%24PageContent%24hconfirm=!p~You%20have%20identified%20yourself%20by%20your%20registered%20email%20id%20redmoneyindore%40gmail.com%20as%20!b%20class%3D%22color%22~Redmoney%20Financial%20Services%20Pvt%20Ltd!%2Fb~!br%2F~!br%2F~You%20wish%20information%20from%20the%20following%20Mutual%20Funds%20!br%20%2F~!b~Aditya%20Birla%20Sun%20Life%20Mutual%20Fund!br%20%2F~HDFC%20Mutual%20Fund!br%20%2F~ICICI%20Prudential%20Mutual%20Fund!br%20%2F~SBI%20Mutual%20Fund!br%20%2F~Birla%20Gold%20and%20Precious%20Metals!br%20%2F~DSP%20BlackRock%20Mutual%20Fund!br%20%2F~HSBC%20Mutual%20Fund!br%20%2F~IDFC%20Mutual%20Fund!br%20%2F~IIFL%20Mutual%20Fund!br%20%2F~Kotak%20Mutual%20Fund!br%20%2F~L%26T%20Mutual%20Fund!br%20%2F~Mahindra%20Mutual%20Fund!br%20%2F~PPFAS%20Mutual%20Fund!br%20%2F~Reliance%20Money%20Precious%20Metals!br%20%2F~Shriram%20Mutual%20Fund!br%20%2F~TATA%20Mutual%20Fund!br%20%2F~Union%20Mutual%20Fund!%2Fb~!br%20%2F~You%20want%20to%20see%20the%20following%20report%20!br%20%2F~!b%20class%3D%22color%22~WBR2.%20Investor%20Transactions%20for%20a%20Period.!br%20%2F~!%2Fb~!br%20%2F~Your%20selection%20criteria%20are%20!br%20%2F~!b%20class%3D%22color%22~Transaction%20Date%20between%205-Jan-2018%20and%2031-Jan-2018!br%20%2F~Transaction%20type(s)%20are%20'P'%2C'JP'%2C'DR'%2C'DP'%2C'DA'%2C'R'%2C'JR'%2C'SI'%2C'SO'%2C'JS'%2C'TI'%2C'TO'%2C'JT'!br%20%2F~Amount%20~%3D%200!br%20%2F~%20Brktype%3ARIA!br%20%2F~Output%20Format%20is%20Excel%20With%20Headers!br%20%2F~Delivery%20Option%20is%20Email%20a%20download%20link!br%20%2F~!%2Fb~!br%20%2F~Not%20including%20this%20query%2C%20you%20have%20submitted%20!b%20class%3D%22color%22~4%20queries!%2Fb~%20costing!b%20class%3D%22color%22~%2096%20units!%2Fb~%20today%2C%20!b%20class%3D%22color%22~89%20queries!%2Fb~%20costing%20!b%20class%3D%22color%22~1227%20units!%2Fb~%20this%20month%2C%20and%20!b%20class%3D%22color%22~89%20queries%20!%2Fb~%20costing%20!b%20class%3D%22color%22~1227%20units%20!%2Fb~%20this%20calendar%20year.%20!font%20color%3Dred~You%20have%20!b~11%20queries%20and%203773%20cost%20budget%20!%2Fb~%20left%20for%20this%20month.%20Please%20ensure%20you%20do%20not%20exceed%20these%20monthly%20budgets%20as%20otherwise%20fresh%20queries%20will%20not%20be%20accepted.!br%20%2F~!br%20%2F~!%2Ffont~!%2Fp~&ctl00%24PageContent%24hdeferred=&ctl00%24PageContent%24hpwd=&ctl00%24PageContent%24hbrktyp=brok&ctl00%24PageContent%24hbrokcode=&ctl00%24PageContent%24hbselsort=&ctl00%24PageContent%24hbselsort_desc=&ctl00%24PageContent%24hbselwhere=&ctl00%24PageContent%24hbselwhere_desc=&ctl00%24PageContent%24hbselfields=&ctl00%24PageContent%24hbselfields_desc=&ctl00%24PageContent%24hbsltable=&ctl00%24PageContent%24hamcs=B%2CH%2CP%2CL%2CBG%2CD%2CO%2CG%2CIF%2CK%2CF%2CMM%2CPP%2CRM%2CSH%2CT%2CUK&ctl00%24PageContent%24hcamsmail=&ctl00%24PageContent%24hqry1=&ctl00%24PageContent%24hqrygrp=&ctl00%24PageContent%24hreport=&ctl00%24PageContent%24houtputformat=XLSWH&ctl00%24PageContent%24hdeloption=DOWNLINK&ctl00%24PageContent%24hfrmdate=5-Jan-2018&ctl00%24PageContent%24htodate=31-Jan-2018&ctl00%24PageContent%24hrdatetype=D&ctl00%24PageContent%24hdPayFromDate=&ctl00%24PageContent%24hdPayToDate=&ctl00%24PageContent%24hrdateperiod=0&ctl00%24PageContent%24hqrymode=N&ctl00%24PageContent%24hseqno=&ctl00%24PageContent%24hrepselecttime=&ctl00%24PageContent%24hschemes=&ctl00%24PageContent%24htradetype=%5C'P%5C'%2C%5C'JP%5C'%2C%5C'DR%5C'%2C%5C'DP%5C'%2C%5C'DA%5C'%2C%5C'R%5C'%2C%5C'JR%5C'%2C%5C'SI%5C'%2C%5C'SO%5C'%2C%5C'JS%5C'%2C%5C'TI%5C'%2C%5C'TO%5C'%2C%5C'JT%5C'&ctl00%24PageContent%24hsubbrok=&ctl00%24PageContent%24hfpincode=&ctl00%24PageContent%24htpincode=&ctl00%24PageContent%24hamount=0&ctl00%24PageContent%24hoper=%3E%5E&ctl00%24PageContent%24hisccode=&ctl00%24PageContent%24hpertype=&ctl00%24PageContent%24htaxstatus=&ctl00%24PageContent%24hpreviousdate1=&ctl00%24PageContent%24hpreviousdate2=&ctl00%24PageContent%24hschtype=&ctl00%24PageContent%24htranstype=&ctl00%24PageContent%24hfolio=&ctl00%24PageContent%24hmonyear=&ctl00%24PageContent%24hcategory=&ctl00%24PageContent%24hacststnry=&ctl00%24PageContent%24hsipfrmdate=&ctl00%24PageContent%24hsiptodate=&ctl00%24PageContent%24hAltBrok=&ctl00%24PageContent%24hConfirm_WBR7=&ctl00%24PageContent%24hExcludeTICOB=N&ctl00%24PageContent%24hICPanNo=&ctl00%24PageContent%24hICBankName=&ctl00%24PageContent%24hICBankACNo=&ctl00%24PageContent%24hValidEUIN=&ctl00%24PageContent%24hpurchase=&ctl00%24PageContent%24hunit=&ctl00%24PageContent%24hsftp=&ctl00%24PageContent%24hMultischeme=&ctl00%24PageContent%24hpayout=&ctl00%24PageContent%24hindicativereport=&ctl00%24PageContent%24hfolioOpt=N&__VIEWSTATE=".replace('5-Jan-2018',start_date).replace('31-Jan-2018', end_date)+viewstate
    headers = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9",
        'Cache-Control': "no-cache",
        'Connection': "keep-alive",
        'Content-Length': "9232",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cookie': "cookiesession1=0ACDD9FDXGHOBF1V3M3ZOGEBKAN6A906; ASP.NET_SessionId=e0u1vjnxxnhsgpfz32qtkg0e; _ga=GA1.2.1425232447.1517402097; _gid=GA1.2.1501364663.1517402097",
        'Host': "www.camsonline.com",
        'Origin': "https://www.camsonline.com",
        'Pragma': "no-cache",
        'Referer': "https://www.camsonline.com/DistributorServices/COL_DisQueryConfirm.aspx",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers)

    pq = PyQuery(response.text)
    return (pq('[class="one-col"] p:nth-of-type(1) b:nth-of-type(1)').text())
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8282)