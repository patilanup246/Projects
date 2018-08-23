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
        
    t = '''
    <html>
        <head>
            <base target="_blank">
            <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.css">
            <script type="text/javascript" src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
            <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.js"></script>
        </head>
        <body>
        <table id = "table_id" class="dataTable display cell-border nowrap" style="display: none;">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Disclosures Count</th>
                </tr>
            </thead>
            <tbody>
'''
    try:
        db = psycopg2.connect(host=DB_ADDRESS,user=DB_USER,password=DB_PASS,database=DB_NAME )
        cursor = db.cursor()
        cursor.execute('select id, firstname, lastname, disclosure_count, disclosures  from individuals where cast("disclosure_count"as int) > 0 order by cast("disclosure_count" as int) DESC')
        print ('select id, firstname, lastname, disclosure_count, disclosures  from individuals where cast("disclosure_count"as int) > 0')
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
    t+='''</tbody></table>
    <script>
    $(document).ready( function () {
    $("td").css("text-align", "center");
    $('#table_id').DataTable({
    "pageLength": 25
    });
    $('#table_id').show();
    $('#table_id_wrapper').css("padding", "2%");
    
} );
    </script>
    
    </body>
    
    '''
    return t

@app.route('/search')
def hello():
    startdate       = request.args.get('startdate')
    enddate         = request.args.get('enddate')
    mind            = request.args.get('mind')
    maxd            = request.args.get('maxd')
    return run_query(startdate,enddate,mind,maxd)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)