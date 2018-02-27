# -*- coding: utf-8 -*-
from flask import Flask,redirect
from flask import request
from flask import render_template
import requests
import re, json, urllib
#from selenium import webdriver
import webbrowser
from pyquery import PyQuery
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from Tkinter import *
app = Flask(__name__)

@app.route('/home')
def my_form():
    return render_template("my-form.html")



@app.route('/', methods=['POST'])
def my_form_post():

  
    _location = ''
    _keywords = ''
    try:
        _location = urllib.quote(request.form['location'].decode('utf-8').encode('utf-8')).replace('%252C','%2C')
    except:
        pass
    try:
        _keywords = request.form['keyword']
    except:
        pass    
    total_pages = ''
    min_price = ''
    max_price = ''
    try:
        total_pages = int(request.form['page'])
    except:
        pass
    try:
        min_price = request.form['min']
    except:
        pass
    try:    
        max_price = request.form['max']
    except:
        pass    
    
    url = "https://s.taobao.com/search"
     
    headers = {
        'cache-control': "no-cache"
        }
    file_output_taobao = open('taobao_log.txt','w')
    file_output_taobaoUnsorted = open('taobao_logUnsorted.txt','w')
    file_output_tmall = open('tmall_log.txt','w')
    file_output_tmallUnsorted = open('tmall_logUnsorted.txt','w')
    file_output_taobao_price_rating = open('file_output_taobao_price_rating.txt','w')
    file_output_tmall_price_rating = open('file_output_tmall_price_rating.txt','w')
    taobao_cumulative_file = open('taobao_cumulative_file.txt','w')
    tmall_cumulative_file = open('tmall_cumulative_file.txt','w')
    taobao_items = []
    tmall_items = []
      
      
      
      
    headers_tmall_price = {
        'accept': "*/*",
        'accept-encoding': "gzip, deflate, sdch, br",
        'accept-language': "en-US,en;q=0.8",
        'cookie': "ubn=p; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; l=ApqaM34S6mepOo4/-L2v7B9lakq8lh6l; cna=rQm+EBJFl1kCAWDj3JQkBb/N; v=0; uc3=sg2=VWt7i4yuT4%2BEWEqblgMiZ6YO4yfrB8f%2FwpXaiPn8JKI%3D&nk2=B0e7gw9uQA%3D%3D&id2=UNcODt7csDI6&vt3=F8dBzLKPMvY4hCQs6uw%3D&lg2=UtASsssmOIJ0bQ%3D%3D; existShop=MTUxMDIzOTA5NA%3D%3D; uss=U%2BIpR9GiNt8pa1LTZNlohJRNPJst57TIn4YN6ygs88TF08tSdmIMXrwwMQ%3D%3D; lgc=dexi201; tracknick=dexi201; cookie2=7dfe76613a5eef136d631af81a172b87; sg=133; mt=np=&ci=107_1; cookie1=Vq0XBlmn%2BzK2f%2Br9FI8%2BHfPj%2BYPqnZCjjUhCAhgazjE%3D; unb=376936213; skt=bbe7accd5ced7e94; t=80cf98aed697f34f6f2dc855afe2d946; _cc_=URm48syIZQ%3D%3D; tg=0; _l_g_=Ug%3D%3D; _nk_=dexi201; cookie17=UNcODt7csDI6; uc1=cookie14=UoTde9RyaRiT7w%3D%3D&lng=zh_CN&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&existShop=false&cookie21=V32FPkk%2FgPzW&tag=10&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&pas=0; ucn=unshyun; linezing_session=uvrpdnskzlt9EaG93hGMnPGs_1510249528650AvLW_27; _tb_token_=efe003335735e; isg=AoqKYW--5MGlG2uw132ALDnX23Ds0w6_zPmuRxTDM11oxyqB_Ate5dB3sQTh",
        'referer': "https://detail.tmall.com/item.htm?spm=a230r.1.14.267.76bf523Q8aJ60&id=539022854554&ns=1&abbucket=3&skuId=3220262955330",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        'cache-control': "no-cache"
        }
      
    for page in range(0,total_pages):
        #querystring = {"data-key":"s","ajax":"true","q":open('keywords.txt','r').read(),"imgfile":"","commend":"all","sort":"sale-desc","search_type":"item","data-value":str(page*44)
        #response = requests.request("GET", url, headers=headers, params=querystring)
        print ('https://s.taobao.com/search?sort=sale-desc&data-key=s&ajax=true&q={}&loc={}&data-value={}&filter=reserve_price[{},{}]'.format(_keywords,_location,str(page*44),str(min_price),str(max_price)))
        response = requests.get('https://s.taobao.com/search?sort=sale-desc&data-key=s&ajax=true&q={}&loc={}&data-value={}&filter=reserve_price[{},{}]'.format(_keywords,_location,str(page*44),str(min_price),str(max_price)))
          
        #file_output.write(response.text.encode('ascii','ignore'))
      
        for item in response.json()['mods']['itemlist']['data']['auctions']:
            item_page_link = item['detail_url']
            mod_item_page_link = item_page_link.replace('//detail.','')
            #item_id = re.findall(r'\d+', item_page_link)[0]
            item_id = str(item['nid'])
            print ('Scraping Page - '+str(page+1) +', item - '+str(response.json()['mods']['itemlist']['data']['auctions'].index(item)+1))
            try:
                taobao_obj = {}
                tmall_obj ={}
                if 'tmall' in item_page_link:
                    neg_count_store = []
                    print ('stage - 1')
                    print ('https://dsr-rate.tmall.com/list_dsr_info.htm?itemId='+str(item_id))
                    resp_tmall = requests.get('https://dsr-rate.tmall.com/list_dsr_info.htm?itemId='+str(item_id)).text.replace('jsonp128','')[3:-2]
                    print (resp_tmall)
                    print ('stage - 2')
                    j_tmall = json.loads(resp_tmall)
                    print ('stage - 3')
                    tmall_obj['link'] = mod_item_page_link
      
                    #Added by Anil-START
                    tmall_obj['gradeAvgRating'] = j_tmall['dsr']['gradeAvg']
                    tmall_obj['rateTotalRating'] = j_tmall['dsr']['rateTotal']
                    #Added by Anil-END
                    tmall_obj['rating'] = int(j_tmall['dsr']['gradeAvg']*j_tmall['dsr']['rateTotal'])
                      
                    '''
                        Added - Negative count
                        @author: Tasneem
                    '''
                    print ('stage - 4')
                    print ('https://rate.tmall.com/listTagClouds.htm?isAll=true&callback=jsonp937&isInner=true&itemId='+str(item_id))
                    resp_tmall_neg_count = requests.get('https://rate.tmall.com/listTagClouds.htm?isAll=true&callback=jsonp937&isInner=true&itemId='+str(item_id)).text.replace('jsonp937(','')[1:-1]
                    #print (resp_tmall_neg_count)
                    j_neg_count = json.loads(resp_tmall_neg_count)
                    print ('stage - 5')
                    for tag_cloud in j_neg_count['tags']['tagClouds']:
                        if not tag_cloud['posi']:
                            #print tag_cloud['count']
                            neg_count_store.append(str(tag_cloud['count']))
                    tmall_obj['neg_rating'] = ', '.join(neg_count_store)
                    #print tmall_obj['neg_rating']
                    
                      
                      
                      
                    '''
                    added price and rating for tmall 29/05/17
                    Author - Tasneem
                    '''
                    print ('https://detail.tmall.com/item/{}.htm'.format(str(item_id)))
                    resp_rating_tmall = requests.get('https://detail.tmall.com/item.htm?id={}'.format(str(item_id))).text
                      
                    pq_tmall = PyQuery(resp_rating_tmall)
                    file_output_tmall_price_rating.write(str(item_id)+'\t')
                    print ('len of '+str(pq_tmall('[class="shopdsr-score-con"]')))
                    tmall_obj['rating_0'] = ''
                    tmall_obj['rating_1'] = ''
                    tmall_obj['rating_2'] = ''
                    r_i = 0
                    for rating in pq_tmall('[class="shopdsr-score-con"]'):
                        tmall_obj['rating_'+str(r_i)] = str(rating.text)
                        file_output_tmall_price_rating.write(str(rating.text)+'\t')
                        r_i+=1
                    url = "https://mdskip.taobao.com/core/initItemDetail.htm"
      
                    querystring = {
                            "itemId":str(item_id)
                            }
                    print (url)
                    response_tmall_price = requests.request("GET", url, headers=headers_tmall_price, params=querystring).json()
                    #print response_tmall_price.decode('utf-8').encode('utf-8')
                    #tmall_price_json = json.loads(re.search( r'\((.*)\)', response_tmall_price, re.M|re.I).group())
                    tmall_price_keys = response_tmall_price['defaultModel']['itemPriceResultDO']['priceInfo'].keys()
                    t_prices = []
                    for key in tmall_price_keys:
                        file_output_tmall_price_rating.write(str(response_tmall_price['defaultModel']['itemPriceResultDO']['priceInfo'][key]['promotionList'][0]['price'])+', ')
                        t_prices.append(str(response_tmall_price['defaultModel']['itemPriceResultDO']['priceInfo'][key]['promotionList'][0]['price']))
                    tmall_obj['price'] = ''
                    tmall_obj['price'] = ', '.join(t_prices)
                    tmall_obj['Score'] = ''#str(item['gradeAvgRating'])+str(item['rateTotalRating'])+str(item['neg_rating'])+str(item['rating'])+str(item['rating_0'])+str(item['rating_1'])+str(item['rating_2'])+(item['Score'])
                    tmall_items.append(tmall_obj)
                    file_output_tmall_price_rating.write('\n')
                    file_output_tmall_price_rating.flush()
                      
                      
                      
                  
                if 'taobao' in item_page_link:
                    print ('https://rate.taobao.com/detailCommon.htm?auctionNumId='+str(item_id))
                    resp_taobao = requests.get('https://rate.taobao.com/detailCommon.htm?auctionNumId='+str(item_id)).text[3:-1]
                      
                    j_taobao = json.loads(resp_taobao)
                      
                    taobao_obj['link'] = mod_item_page_link
      
                    #Added by Anil-START
                    taobao_obj['goodRating'] = j_taobao['data']['count']['good']
                    taobao_obj['normalRating'] = j_taobao['data']['count']['normal']
                    taobao_obj['badRating'] = j_taobao['data']['count']['bad']
                    #Added by Anil-END
                                                           
                    taobao_obj['rating'] = int(j_taobao['data']['count']['good'] - j_taobao['data']['count']['normal'] - j_taobao['data']['count']['bad'])
                    
                      
                      
                    # Added by Tasneem 23/05/17
                    # This code will get price, seller rating and number of stars
                    print ('https://item.taobao.com/item.htm?id='+str(item_id))
                    resp_taobao_page = requests.get('https://item.taobao.com/item.htm?id='+str(item_id)).text
                      
                    pq_tao = PyQuery(resp_taobao_page)
                      
                    taobao_price_rating = str('https://item.taobao.com/item.htm?id='+str(item_id))+'\t'+str(item['view_price'])+'\t'
                    taobao_obj['price'] = str(item['view_price'])
                    #print pq_tao('.tb-rmb-num').text()
                    ratings =[' ',' ',' ']
                    r_i=0
                    taobao_obj['rating_0'] =''
                    taobao_obj['rating_1'] = ''
                    taobao_obj['rating_2'] = ''
                    for rating in pq_tao('[class="tb-shop-rate"] a'):
                        ratings[r_i] = rating.text.replace('\n','').replace('\r','').strip()
                        taobao_obj['rating_'+str(r_i)] = rating.text.replace('\n','').replace('\r','').strip()
                        r_i+=1
                    taobao_price_rating += '\t'.join(ratings) +'\t'
                    taobao_price_rating +=  str(len(pq_tao('.tb-shop-rank i'))) + '\t'
                    taobao_obj['Seller_stars'] = str(len(pq_tao('.tb-shop-rank i')))
                    taobao_obj['crown_color'] = ''
                    if pq_tao('.tb-shop-rank'):
                        taobao_price_rating += pq_tao('.tb-shop-rank').attr('class').replace('tb-shop-rank','').replace('tb-rank-','')
                        taobao_obj['crown_color'] = pq_tao('.tb-shop-rank').attr('class').replace('tb-shop-rank','').replace('tb-rank-','')
                    
                    #taobao_obj['Score'] = ''
                    file_output_taobao_price_rating.write(taobao_price_rating+'\n')
                    file_output_taobao_price_rating.flush()
                    
                    taobao_obj['Score'] = ''#int(float(taobao_obj['goodRating']))+ int(float(taobao_obj['normalRating']))+ int(float(taobao_obj['badRating']))+int(float(taobao_obj['price']))+int(float(taobao_obj['rating_0']))+int(float(taobao_obj['rating_1']))+int(float(taobao_obj['rating_2']))+int(float(taobao_obj['Seller_stars']))
                    taobao_items.append(taobao_obj)
            
            
            except Exception as e:
                #file_output_tmall_price_rating.write('\n')
                #file_output_tmall_price_rating.flush()
                print (e)
                  
    for item in sorted(taobao_items, key=lambda k: int(k['rating']), reverse = True):
        file_output_taobao.write('https:'+item['link']+'\t'+ str(item['rating'])+'\n')
    for item in sorted(tmall_items, key=lambda k: int(k['rating']), reverse = True):
        file_output_tmall.write(item['link']+'\t'+ str(item['rating'])+'\n')
    file_output_taobao.close()
    file_output_tmall.close()
      
    #Added by Anil-START
    for item in taobao_items:
        file_output_taobaoUnsorted.write('https:'+item['link']+'\t'+ str(item['goodRating'])+'\t'+ str(item['normalRating'])+'\t'+ str(item['badRating'])+'\n')
        taobao_cumulative_file.write('https:'+item['link']+'\t'+ str(item['goodRating'])+'\t'+ str(item['normalRating'])+'\t'+ str(item['badRating'])+'\t'+str(item['price'])+'\t'+str(item['rating_0'])+'\t'+str(item['rating_1'])+'\t'+str(item['rating_2'])+'\t'+str(item['Seller_stars'])+'\t'+str(item['crown_color'])+'\t'+str(taobao_obj['Score'])+'\n')
    for item in tmall_items:
        file_output_tmallUnsorted.write(item['link']+'\t'+ str(item['gradeAvgRating'])+'\t'+ str(item['rateTotalRating'])+'\t'+item['neg_rating']+'\n')
        tmall_cumulative_file.write(item['link']+'\t'+ str(item['gradeAvgRating'])+'\t'+ str(item['rateTotalRating'])+'\t'+str(item['neg_rating'])+'\t'+str(item['rating'])+'\t'+str(item['price'])+'\t'+str(item['rating_0'])+'\t'+str(item['rating_1'])+'\t'+str(item['rating_2'])+str(item['Score'])+'\n')
    taobao_cumulative_file.close()
    tmall_cumulative_file.close()
    file_output_taobaoUnsorted.close()
    file_output_tmallUnsorted.close()
    #Added by Anil-END
       
       
    
#     taobao_cumulative_array_all = []
#     taobao_cumulative_file = open('taobao_cumulative_file.txt','w')
#     for i in open('file_output_taobaoUnsorted.txt').read().split('\n'):
#         taobao_cumulative_array = []
#         for j in i.split('\t'):
#             taobao_cumulative_array.append(j)
#         taobao_cumulative_array_all.append(taobao_cumulative_array)
#     for i in open('file_output_taobao_price_rating.txt').read().split('\n'):
#         ii=0
#         taobao_cumulative_array = []
#         for j in i.split('\t'):
#             if ii>0: 
#                 taobao_cumulative_array.append(j)
#             ii+=1
#         taobao_cumulative_array_all.append(taobao_cumulative_array)
#     
       
    '''
        open chrome and first 10 pages of taobao:
        
    '''
      
#     tabs= 0
#     for url in open('taobao_log.txt','r').read().split('\n'):
#         if tabs > 10:
#             break
#         #driver = webdriver.Chrome()
#         print (url.split('\t')[0])
#         webbrowser.open(url.split('\t')[0])
#         tabs+=1
#       
    return redirect('http://127.0.0.1:5000/get_results')
    

    

@app.route('/get_results', methods=['GET'])
def get_results():      
     
    
    output_html = '<!DOCTYPE html><html>'
    output_html += '''<head><base target="_blank"><script type="text/javascript">

    function get_links_all() {
    if (document.getElementById('pag').value != ''){
    j =  $('table[style =""] tr:not(.filtered) td a')
    if (document.getElementById('pag').value > j.length){
    l = j.length;
    }else{
    l = document.getElementById('pag').value;
    }
    for (i=0;i<l;i++){
    window.open($(j[i]).attr("href"));
    }
}
    }

    function yesnoCheck() {
        if (document.getElementById('taobao_cumulative_file').checked) {
            document.getElementById('1taobao_cumulative_file').style.display = '';
        } else{
             document.getElementById('1taobao_cumulative_file').style.display = 'none';
        }
        if (document.getElementById('tmall_cumulative_file').checked) {
            document.getElementById('1tmall_cumulative_file').style.display = '';
        } else{
             document.getElementById('1tmall_cumulative_file').style.display = 'none';
        }
        if (document.getElementById('taobao_log').checked) {
            document.getElementById('1taobao_log').style.display = '';
        }else{
             document.getElementById('1taobao_log').style.display = 'none';
        }
        if (document.getElementById('taobao_logUnsorted').checked) {
            document.getElementById('1taobao_logUnsorted').style.display = '';
        }else{
             document.getElementById('1taobao_logUnsorted').style.display = 'none';
        }
        if (document.getElementById('tmall_log').checked) {
            document.getElementById('1tmall_log').style.display = '';
        }else{
             document.getElementById('1tmall_log').style.display = 'none';
        }
        if (document.getElementById('tmall_logUnsorted').checked) {
            document.getElementById('1tmall_logUnsorted').style.display = '';
        }else{
             document.getElementById('1tmall_logUnsorted').style.display = 'none';
        }
        }

    </script>
    
    <!-- choose a theme file -->
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <link rel="stylesheet" type="text/css" href="static/tablesorter-master/css/theme.blue.css">
    <link href="{{ url_for('static', filename='tablesorter-master/css/theme.blue.css') }}" />
    <!-- load jQuery and tablesorter scripts -->
    <script type="text/javascript" src="static/tablesorter-master/js/jquery.tablesorter.js"></script>
    <script type="text/javascript" src="static/tablesorter-master/js/jquery.tablesorter.widgets.js"></script>
    
    <script>
    $(function(){
        $("#1taobao_cumulative_file").tablesorter({
        theme: 'blue',
        widgets: ["zebra", "filter"]
        });
    });
    $(function(){
        $("#1tmall_cumulative_file").tablesorter({
        theme: 'blue',
        widgets: ["zebra", "filter"]
        });
    });
    $(function(){
        $("#1taobao_log").tablesorter({
        theme: 'blue',
        widgets: ["zebra", "filter"]
        });
    });
    $(function(){
        $("#1taobao_logUnsorted").tablesorter({
        theme: 'blue',
        widgets: ["zebra", "filter"]
        });
    });
    $(function(){
        $("#1tmall_log").tablesorter({
        theme: 'blue',
        widgets: ["zebra", "filter"]
        });
    });
    $(function(){
        $("#1tmall_logUnsorted").tablesorter({
        theme: 'blue',
        widgets: ["zebra", "filter"]
        });
    });
    </script>

    <!-- tablesorter widgets (optional) -->
    
    
    
    </head>'''
    output_html+='<body>'
    output_html+='''<input type="radio" onclick="javascript:yesnoCheck();" name="yesno" id="taobao_cumulative_file"/>file_output_taobao_price_rating: Full data including Price and Rating (Taobao)<br>
                    <input type="radio" onclick="javascript:yesnoCheck();" name="yesno" id="tmall_cumulative_file"/>file_output_tmall_price_rating<br>
                    <input type="radio" onclick="javascript:yesnoCheck();" name="yesno" id="taobao_log"/>taobao_log<br>
                    <input type="radio" onclick="javascript:yesnoCheck();" name="yesno" id="taobao_logUnsorted"/>taobao_logUnsorted<br>
                    <input type="radio" onclick="javascript:yesnoCheck();" name="yesno" id="tmall_log"/>tmall_log<br>
                    <input type="radio" onclick="javascript:yesnoCheck();" name="yesno" id="tmall_logUnsorted"/>tmall_logUnsorted<br>
                    <br>
                    Number of top links to open: <input type="textbox" name="pag" id="pag" value="10"/><br>
                    <button type="button" id="get_links" onclick="javascript:get_links_all();">Open top links</button>
<br>'''
    output_html+= '<table  style="display: none" border="1" id="1taobao_cumulative_file" style="width:100%"><thead>'           
    
    for h in ['Id','Good rating','Normal rating','Bad rating','Price','Seller Rating 1','Seller Rating 2','Seller Rating 3','Seller stars','Seller Crown','Score']:
        output_html+='<th>'+h+'</th>'
    output_html+='</thead><tbody>'
    
    for i in open('taobao_cumulative_file.txt').read().split('\n'):
        output_html+='<tr>'
        i_l = 0
        for j in i.split('\t'):
            if i_l == 0:
                output_html+='<td><a href="'+j+'">'+j+'</a></td>'
            else:
                output_html+='<td>'+j+'</td>'
            i_l+=1
        output_html+='</tr>'
    output_html+='</tbody></table>'
    
    
    
    output_html+= '<table style="display: none" border="1"  id="1tmall_cumulative_file" style="width:100%"><thead>'   
    for h in ['Link','Average Rating','Total Rating','Negative Ratings','Calculated Rating','Price','Seller Rating 1','Seller Rating 2','Seller Rating 3','Score']:
        output_html+='<th>'+h+'</th>'
    output_html+='</thead><tbody>'        
    for i in open('tmall_cumulative_file.txt').read().split('\n'):
        output_html+='<tr>'
        i_l = 0
        for j in i.split('\t'):
            if i_l == 0:
                output_html+='<td><a href="https://detail.tmall.com/item.htm?id='+j+'">https://detail.tmall.com/item.htm?id='+j+'</a></td>'
            else:
                output_html+='<td>'+j+'</td>'
            i_l+=1
        output_html+='</tr>'
    output_html+='</tbody></table>'
    
    
    
    
    output_html+= '<table  style="display: none" border="1"  id="1taobao_log" style="width:100%"><thead>'  
    for h in ['Id','Rating']:
        output_html+='<th>'+h+'</th>'
    output_html+='</thead><tbody>'             
    for i in open('taobao_log.txt').read().split('\n'):
        output_html+='<tr>'
        i_l = 0
        for j in i.split('\t'):
            if i_l == 0:
                output_html+='<td><a href="'+j+'">'+j+'</a></td>'
            else:
                output_html+='<td>'+j+'</td>'
            i_l+=1
        output_html+='</tr>'
    output_html+='</tbody></table>'
    
    
    
    
    output_html+= '<table  style="display: none" border="1"  id="1taobao_logUnsorted" style="width:100%"><thead>'       
    for h in ['Id','Good Rating','Normal Rating','Bad Rating']:
        output_html+='<th>'+h+'</th>'
    output_html+='</thead><tbody>'        
    for i in open('taobao_logUnsorted.txt').read().split('\n'):
        output_html+='<tr>'
        i_l = 0
        for j in i.split('\t'):
            if i_l == 0:
                output_html+='<td><a href="'+j+'">'+j+'</a></td>'
            else:
                output_html+='<td>'+j+'</td>'
            i_l+=1
        output_html+='</tr>'
    output_html+='</tbody></table>'
    
    
    

    output_html+= '<table  style="display: none" border="1"  id="1tmall_log" style="width:100%"><thead>'    
    for h in ['Id','Rating']:
        output_html+='<th>'+h+'</th>'
    output_html+='</thead><tbody>'           
    for i in open('tmall_log.txt').read().split('\n'):
        output_html+='<tr>'
        for j in i.split('\t'):
            output_html+='<td>'+j+'</td>'
        output_html+='</tr>'
    output_html+='</tbody></table>'
    
    
    
  
    output_html+= '<table style="display: none"  border="1"  id="1tmall_logUnsorted" style="width:100%"><thead>'  
    for h in ['Id','Avg Rating','Total Rating','Negative Rating']:
        output_html+='<th>'+h+'</th>'
    output_html+='</thead><tbody>'           
    for i in open('tmall_logUnsorted.txt').read().split('\n'):
        output_html+='<tr>'
        for j in i.split('\t'):
            output_html+='<td>'+j+'</td>'
        output_html+='</tr>'
    output_html+='</tbody></table>'
    
    

    output_html+='</body></html>'
    #processed_text = text.upper()
    return output_html

if __name__ == '__main__':
    app.run()