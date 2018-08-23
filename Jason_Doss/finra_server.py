# -*- coding: utf-8 -*-
'''
Created on Jul 21, 2018

@author: talib
'''
from flask import Flask, request
from flask_compress import Compress
app = Flask(__name__)
Compress(app)
import psycopg2
import json
import datetime

HEADER_compare = '''
    <head>
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <base target="_blank">
    <link rel="stylesheet" type="text/css" href="static/table_css.css">
    <style>
        a {color: white;}

    </style>
    </head>
    <section>
  <h1>Broker Check Report</h1>
  <div class="tbl-header">
    <table cellpadding="0" cellspacing="0" border="0">
      <thead>
        <tr>
          <th>No.</th>
          <th>Broker ID</th>
          <th>First Name</th>
          <th>last Name</th>
          <th>Details</th>
        </tr>
      </thead>
    </table>
  </div>
  <div class="tbl-content">
    <table cellpadding="0" cellspacing="0" border="0">
      <tbody>
'''

HEADER_search = '''
    <head>
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <base target="_blank">
    <link rel="stylesheet" type="text/css" href="static/table_css.css">
    <style>
        a {color: white;}

    </style>
    </head>
    <section>
  <h1>Broker Check Report</h1>
  <div class="tbl-header">
    <table cellpadding="0" cellspacing="0" border="0">
      <thead>
        <tr>
          <th>No.</th>
          <th>Broker ID</th>
          <th>First Name</th>
          <th>last Name</th>
          <th>Disclosures in Time Range</th>
        </tr>
      </thead>
    </table>
  </div>
  <div class="tbl-content">
    <table cellpadding="0" cellspacing="0" border="0">
      <tbody>
'''


FOOTER = '''</tbody>
    </table>
  </div>
</section>


<div class="made-with-love">
  Made with
  <i>♥</i> by
  <a href="https://www.upwork.com/freelancers/~0141be70c628b72e75">Tasneem Rangwala</a> 
</div>
    <script>
    $(document).ready( function () {
    $('#table_id_wrapper').css("padding", "2%");
    $('a').css("color", "white !important");
    $('#table_id').show();
} );
    </script>
    
    
    </body>
    
    '''


DB_ADDRESS = "localhost"
DB_USER = "jasondoss"
DB_PASS = "jasondoss1!2@"
DB_NAME = "postgres"
def run_query(startdate,enddate,mind,maxd):
    if not startdate:
        
        start_yy = 1900
        start_mm = 1
        start_dd = 1
    else:
        startdate = startdate.split('-')
        start_yy = int(startdate[0])
        start_mm = int(startdate[1])
        start_dd = int(startdate[2])
    if not enddate:
        end_yy = 2100
        end_mm = 12
        end_dd = 31
    else:
        enddate = enddate.split('-')
        end_yy = int(enddate[0])
        end_mm = int(enddate[1])
        end_dd = int(enddate[2])
    if not mind:
        mind = 1
    if not maxd:
        maxd = 100000000
        
    print ()
        
    t = HEADER_search
    try:
        db = psycopg2.connect(host=DB_ADDRESS,user=DB_USER,password=DB_PASS,database=DB_NAME )
        cursor = db.cursor()
        
        cursor.execute('select scrape_id from individual_scrape_id order by scrape_id desc limit 1')
        data = cursor.fetchall()
        
        current_scrape_id = str(data[0][0])
        
        cursor.execute('select id, firstname, lastname, disclosure_count, disclosures  from individuals where cast("disclosure_count"as int) > 0  and scrape_id = \'{}\' order by lastname ASC'.format(current_scrape_id))
        
        data = cursor.fetchall()
        
        total_rows = 0
    
        for d in data:
            
            if total_rows < 10000:
                dis_count = 0
                
                
                
                for disc in json.loads(d[4]):
                    eventdate = disc.get('eventDate','')
                    if eventdate:
                        eventdate = eventdate.split('/')
                        mm = int(eventdate[0])
                        dd = int(eventdate[1])
                        yy = int(eventdate[2])
                        
                        if datetime.date(start_yy, start_mm, start_dd) <= datetime.date(yy, mm, dd) <= datetime.date(end_yy, end_mm, end_dd):
                            dis_count+=1
                    else:
                        dis_count+=1
                
                #print (dis_count)
                if int(mind) <= dis_count <= int(maxd):
                    total_rows+=1
                    t+='<tr>'
                    t+='<td>'+str(total_rows)+'</td>'
                    for a in range(4):
                        
                        if a == 0:
                            t+='<td><a href="https://brokercheck.finra.org/individual/summary/{}">'.format(d[a])+str(d[a]).capitalize()+'</a></td>'
                        if a == 3:
                            t+='<td>'+str(dis_count)+'</td>'
                        if a == 1 or a== 2:
                            t+='<td>'+str(d[a]).capitalize()+'</td>'
                    t+= '</tr>'
            
            else:
                break
            
            
            
        
    except Exception as e:
        print (e)
    finally:
        db.close()
    t+= FOOTER
    return t


def compare_query(compare):
    t = HEADER_compare
    try:
        db = psycopg2.connect(host=DB_ADDRESS,user=DB_USER,password=DB_PASS,database=DB_NAME )
        cursor = db.cursor()
        
        cursor.execute('select scrape_id from individual_scrape_id order by scrape_id desc limit 1')
        data = cursor.fetchall()
        
        current_scrape_id = int(data[0][0]) - int(compare)
        
        cursor.execute('''
        
                        SELECT 
                        new.id, 
                        new.firstname, 
                        new.lastname, 
                        cast(new.disclosure_count as int) - cast(old.disclosure_count as int), 
                        cast(new.cemp_count as int) - cast(old.cemp_count as int), 
                        cast(new.pemp_count as int) - cast(old.pemp_count as int) 
                        
                        FROM individuals AS old 
                        
                        LEFT JOIN individuals AS new 
                        ON new.id = old.id 
                        
                        WHERE new.scrape_id = '{}'
                        
                        and old.scrape_id = '{}' 
                        
                        order by new.lastname
                        
        
        
        '''.format(str(current_scrape_id),str(current_scrape_id-1)))  
        data = cursor.fetchall()
        total_rows = 0
        for d in data:
            if int(d[3]) == 0 and int(d[4]) == 0 and int(d[5]) == 0:
                pass

            else:  
                details = ''
                if not int(d[3]) == 0:
                    details+= 'Disclosures          : {} <br>'.format(d[3])
                    pass
                if not int(d[4]) == 0:
                    details+= 'Current Employments  : {} <br>'.format(d[4])
                if not int(d[5]) == 0:
                    details+= 'Previous Employments : {} <br>'.format(d[5])
                
                total_rows+=1
                t+='<tr>'
                t+='<td>'+str(total_rows)+'</td>'
                t+='<td><a href="https://brokercheck.finra.org/individual/summary/{}">'.format(d[0])+str(d[0]).capitalize()+'</a></td>'
                t+='<td>'+str(d[1]).capitalize()+'</td>'
                t+='<td>'+str(d[2]).capitalize()+'</td>'
                t+='<td>'+str(details)+'</td>'
    
                t+= '</tr>'
    
        
    except Exception as e:
        print (e)
    finally:
        db.close()
    
    
    
    
    t+= FOOTER
    return t
        

@app.route('/search')
def search():
    startdate       = request.args.get('startdate')
    enddate         = request.args.get('enddate')
    mind            = request.args.get('mind')
    maxd            = request.args.get('maxd')
    return run_query(startdate,enddate,mind,maxd)


@app.route('/compare')
def compare():
    comp       = request.args.get('compare')
    return compare_query(comp)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)