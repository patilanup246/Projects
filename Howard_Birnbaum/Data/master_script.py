# -*- coding: utf-8 -*-

import glob
import csv
import os
import json


 
# for i in glob.glob("files/*.csv"):
#     print (i)
#     if 'mendotahearth' in i:
#         output_canada = open(i.split('_')[1]+'.csv','w',encoding='utf-8', newline='')
#         wr_c = csv.writer(output_canada, quoting=csv.QUOTE_ALL)
#         wr_c.writerow(['Item','address','city','company','country','email','phone_number','postal_code','state','web_site_url','Scraped_site'])
#         mm = []
#           
#         input_csv = csv.reader(open(i), delimiter=',')
#         for row in input_csv:
#             if not row in mm:
#                  
#                 mm.append(row)
#                 wr_c.writerow(row)
#       
#       
#     else:
#         with open(i,'r') as in_file, open(i.split('_')[1]+'.csv','w',encoding='utf-8', newline='') as out_file:
#             seen = set()
#             for line in in_file:
#                 line = line
#                   
#                 if line in seen: continue
#                  
#                 seen.add(line)
#                 out_file.write(line)

    


usa_code_csv_temp = csv.reader(open('input/us_postal_codes.csv'), delimiter=',')
canada_code_csv_temp = csv.reader(open('input/ca_postal_codes.csv'), delimiter=',')
usa_code_csv = []
canada_code_csv = []
for c in usa_code_csv_temp:
    usa_code_csv.append(c)
    
for c in canada_code_csv_temp:
    canada_code_csv.append(c)





canadian_state_short = ['ON','QC','NS','NB','MB','BC','PE','SK','AB','NL']
canadian_state_long  = ['ONTARIO','QUEBEC','NOVA SCOTIA','NEW BRUNSWICK','MANITOBA','BRITISH COLUMBIA','PRINCE EDWARD ISLAND','SASKATCHEWAN','ALBERTA','NEWFOUNDLAND AND LABRADOR','ON','QC','NS','NB','MB','BC','PE','SK','AB','NL']

usa_state_short      = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
usa_state_long       = ['ALABAMA','ALASKA','ARIZONA','ARKANSAS','CALIFORNIA','COLORADO','CONNECTICUT','DELAWARE','FLORIDA','GEORGIA','HAWAII','IDAHO','ILLINOIS','INDIANA','IOWA','KANSAS','KENTUCKY','LOUISIANA','MAINE','MARYLAND','MASSACHUSETTS','MICHIGAN','MINNESOTA','MISSISSIPPI','MISSOURI','MONTANA','NEBRASKA','NEVADA','NEW HAMPSHIRE','NEW JERSEY','NEW MEXICO','NEW YORK','NORTH CAROLINA','NORTH DAKOTA','OHIO','OKLAHOMA','OREGON','PENNSYLVANIA','RHODE ISLAND','SOUTH CAROLINA','SOUTH DAKOTA','TENNESSEE','TEXAS','UTAH','VERMONT','VIRGINIA','WASHINGTON','WEST VIRGINIA','WISCONSIN','WYOMING','AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']


output_canada = open('CANADA_LIST.csv','w',encoding='utf-8', newline='')
wr_canada = csv.writer(output_canada, quoting=csv.QUOTE_ALL)
wr_canada.writerow(['Item','address','city','company','country','email','phone_number','postal_code','state','web_site_url','Scraped_site'])

output_usa = open('USA_LIST.csv','w',encoding='utf-8', newline='')
wr_usa = csv.writer(output_usa, quoting=csv.QUOTE_ALL)
wr_usa.writerow(['Item','address','city','company','country','email','phone_number','postal_code','state','web_site_url','Scraped_site'])


json_usa = []
json_canada = []


def verify_canada(row):
    zip = row[7]
    city = row[2]
    state = row[8]
    
    if not zip:
        for i in canada_code_csv:
            if i[0].lower() in row[1].lower():
                row[7] = i[0]
                break
#     if not zip:
#         for i in canada_code_csv:
#             if row[2].lower() in i[1].lower():
#                 row[7] = i[1]
#                 break
    state_corrected = 0
    for i in canada_code_csv:
        if row[7].lower()[:3] in i[0].lower():
            row[8] = i[2]
            state_corrected = 1
            break
        
    if not state_corrected:
        for i in canada_code_csv:
            if row[2].lower() in i[1].lower():
                row[8] = i[2]
                state_corrected = 1
                break
            
            
    if not city:
        for i in canada_code_csv:
            if row[7].lower()[:3] in i[0].lower():
                row[2] = i[1].split('(')[0].split(',')[0]
                break
            
    if row[9]:
        if not 'http' in row[9]:
            row[9] = 'http://'+row[9].strip()
        if row[9] == 'http://':
            row[9] = ''
    
    row[5] = row[5].lower()
    if not '@' in row[5]:
        row[5] = ''

    row[9] = row[9].lower()
    if '@' in row[9]:
        row[9] = ''
    
    if row[5] == 'info@':
        row[5] = ''
        
    if '|' in row[5]:
        row[5] = row[5].split('|')[0]
    #return row
    
    if 'fax' in row[6].lower(): 

        row[6] = row[6].split('Fax')[0].strip()
    return row

def verify_usa(row):
    zip = row[7]
    city = row[2]
    state = row[8]
    
    if not zip:
        for i in usa_code_csv:
            if i[0].lower() in row[1].lower():
                row[7] = i[0]
                break
#     if not zip:
#         for i in canada_code_csv:
#             if row[2].lower() in i[1].lower():
#                 row[7] = i[1]
#                 break
    state_corrected = 0
    for i in usa_code_csv:
        if row[7].lower() == i[0].lower():
            row[8] = i[2]
            state_corrected = 1
            break
        
    if not state_corrected:
        for i in usa_code_csv:
            if row[2].lower() in i[1].lower():
                row[8] = i[2]
                state_corrected = 1
                break
            
            
    if not city:
        for i in usa_code_csv:
            if row[7].lower() == i[0].lower():
                row[2] = i[1].split('(')[0].split(',')[0]
                break
            
    if row[9]:
        if not 'http' in row[9]:
            row[9] = 'http://'+row[9].strip()
        if row[9] == 'http://':
            row[9] = ''
    
    row[5] = row[5].lower()
    if not '@' in row[5]:
        row[5] = ''

    row[9] = row[9].lower()
    if '@' in row[9]:
        row[9] = ''
    
    if row[5] == 'info@':
        row[5] = ''
        
    if '|' in row[5]:
        row[5] = row[5].split('|')[0]

    if 'fax' in row[6].lower():

        row[6] = row[6].split('Fax')[0].strip()
    return row


def read_csv(csv_name,checker):
    readCSV1 = csv.reader(open(csv_name+'.csv',encoding='utf-8'), delimiter=',')
    csv_csv = []
    for row in readCSV1:
        
        r = []
        for m in row:
            r.append(str(m).replace('&#039;','\'').replace('&#39;','\'').replace('&amp;','&').replace('&#44;',',').replace('&#038;','&').replace('&#8211;','-').replace('&#8217;','\'').replace('&#8220;','"').replace('&#8221;','"').replace('&#8216;','\'').replace('\n',',').replace('null','').replace('None','').replace('Â','').replace('Ã','').replace('©','e').replace('ª','').replace('§','c'))
        
        
        csv_csv.append (r)

    if checker == 'state':
        for row in csv_csv:
            if check_in_state(row) == 'USA':
                row.append(csv_name)
                row[4] = 'USA'
                verify_usa(row)
                wr_usa.writerow(row)
            if check_in_state(row) == 'CANADA':
                row.append(csv_name)
                row[4] = 'Canada'
                row = verify_canada(row)
                wr_canada.writerow(row)
    
    
    if checker == 'address':
        for row in csv_csv:
            if check_in_address(row) == 'USA':
                row.append(csv_name)
                row[4] = 'USA'
                verify_usa(row)
                wr_usa.writerow(row)
            if check_in_address(row) == 'CANADA':
                row.append(csv_name)
                row[4] = 'Canada'
                row = verify_canada(row)
                wr_canada.writerow(row)   
    
    if checker == 'address_spaces':
        for row in csv_csv:
            if check_in_address_spaces(row) == 'USA':
                row.append(csv_name)
                row[4] = 'USA'
                verify_usa(row)
                wr_usa.writerow(row)
            if check_in_address_spaces(row) == 'CANADA':
                row.append(csv_name)
                row[4] = 'Canada'
                row = verify_canada(row)
                wr_canada.writerow(row)  
                
    if checker == 'address_space':
        for row in csv_csv:
            if check_in_address_space(row) == 'USA':
                row.append(csv_name)
                row[4] = 'USA'
                verify_usa(row)
                wr_usa.writerow(row)
            if check_in_address_space(row) == 'CANADA':
                row.append(csv_name)
                row[4] = 'Canada'
                row = verify_canada(row)
                wr_canada.writerow(row)  
            
   
def check_in_state(nam):
    if nam[8].strip().upper() in usa_state_long:
        return 'USA'
    if nam[8].strip().upper() in canadian_state_long:
        return  'CANADA'
    return ''
    
    
def check_in_address(nam):
    if 'CANADA' in nam[1].upper():
        return 'CANADA'
    if 'USA' in nam[1].upper():
        return 'USA'
    if any(', '+item in nam[1].upper() for item in usa_state_long): 
        return 'USA'
    if any(', '+item in nam[1].upper() for item in canadian_state_long): 
        return 'CANADA'
    if any(' '+item+' ' in nam[1].upper() for item in usa_state_long): 
        return 'USA'
    if any(' '+item+' ' in nam[1].upper() for item in canadian_state_long): 
        return 'CANADA'
    
    return ''

def check_in_address_spaces(nam):
    if 'CANADA' in nam[1].upper():
        return 'CANADA'
    if 'USA' in nam[1].upper():
        return 'USA'
    if any(' '+item+' ' in nam[1].upper() for item in usa_state_long): 
        return 'USA'
    if any(' '+item+' ' in nam[1].upper() for item in canadian_state_long): 
        return 'CANADA'
    
    if any(', '+item in nam[1].upper() for item in usa_state_long): 
        return 'USA'
    if any(', '+item in nam[1].upper() for item in canadian_state_long): 
        return 'CANADA'
    
    return ''


def check_in_address_space(nam):
    if 'CANADA' in nam[1].upper():
        return 'CANADA'
    if 'USA' in nam[1].upper():
        return 'USA'
    if any(' '+item in nam[1].upper() for item in usa_state_long): 
        return 'USA'
    if any(' '+item in nam[1].upper() for item in canadian_state_long): 
        return 'CANADA'
    
    if any(', '+item in nam[1].upper() for item in usa_state_long): 
        return 'USA'
    if any(', '+item in nam[1].upper() for item in canadian_state_long): 
        return 'CANADA'
    
    if any(' '+item+' ' in nam[1].upper() for item in usa_state_long): 
        return 'USA'
    if any(' '+item+' ' in nam[1].upper() for item in canadian_state_long): 
        return 'CANADA'
    
    return ''
    
for i in glob.glob("*.csv"):
    
    if i.lower() == "amantii.csv":
        read_csv('amantii','state')
     
    if i.lower() == "ambiancefireplaces.csv":
        read_csv('ambiancefireplaces','state')
         
    if i.lower() == "americanfyredesigns.csv":
        read_csv('americanfyredesigns','state')
         
    if i.lower() == "americanhearth.csv":
        read_csv('americanhearth','state')
         
    if i.lower() == "classicflame.csv":
        read_csv('classicflame','address')
 
    if i.lower() == "dimplex.csv":
        read_csv('dimplex','state')
         
    if i.lower() == "eldoradostone.csv":
        read_csv('eldoradostone','state')
         
    if i.lower() == "enviro.csv":
        read_csv('enviro','address')
         
    if i.lower() == "europeanhome.csv":
        read_csv('europeanhome','state')
         
    if i.lower() == "fireplacex.csv":
        read_csv('fireplacex','state')
         
    if i.lower() == "firerock.csv":
        read_csv('firerock','state')
         
    if i.lower() == "fireside.csv":
        read_csv('fireside','address')
         
    if i.lower() == "flarefireplaces.csv":
        read_csv('flarefireplaces','state')
         
    if i.lower() == "furrion.csv":
        read_csv('furrion','state')
         
    if i.lower() == "hearthnhome.csv":
        read_csv('hearthnhome','state')
 
    if i.lower() == "hearthstonestoves.csv":
        read_csv('hearthstonestoves','address')
         
    if i.lower() == "heatilator.csv":
        read_csv('heatilator','state')
         
    if i.lower() == "heatnglo.csv":
        read_csv('heatnglo','state')
         
    if i.lower() == "heatsurge.csv":
        read_csv('heatsurge','state')
         
    if i.lower() == "hpba.csv":
        read_csv('hpba','state')
         
    if i.lower() == "hwamna.csv":
        read_csv('hwamna','address_spaces')
         
    if i.lower() == "blazeking.csv":
        read_csv('blazeking','address_space')
         
    if i.lower() == "ironstrike.csv":
        read_csv('ironstrike','state')
         
    if i.lower() == "jotul.csv":
        read_csv('jotul','state')
         
    if i.lower() == "lopistoves.csv":
        read_csv('lopistoves','state')
         
    if i.lower() == "majesticproducts.csv":
        read_csv('majesticproducts','state')
         
    if i.lower() == "mendotahearth.csv":
        read_csv('mendotahearth','state')
         
    if i.lower() == "modernflames.csv":
        read_csv('modernflames','state')
         
    if i.lower() == "monessenhearth.csv":
        read_csv('monessenhearth','state')
         
    if i.lower() == "montigo.csv":
        read_csv('montigo','state')
         
    if i.lower() == "napoleonfireplaces.csv":
        read_csv('napoleonfireplaces','state')
         
    if i.lower() == "nehpba.csv":
        read_csv('nehpba','state')
         
    if i.lower() == "ortalheat.csv":
        read_csv('ortalheat','state')
         
    if i.lower() == "pacificenergy.csv":
        read_csv('pacificenergy','state')
         
    if i.lower() == "pilgrimhearth.csv":
        read_csv('pilgrimhearth','state')
         
    if i.lower() == "quadrafire.csv":
        read_csv('quadrafire','state')
         
    if i.lower() == "rhpeterson.csv":
        read_csv('rhpeterson','state')
         
         
    if i.lower() == "sehpba.csv":
        read_csv('sehpba','state')
         
    if i.lower() == "stellarhearth.csv":
        read_csv('stellarhearth','state')
         
    if i.lower() == "storesnear.csv":
        read_csv('storesnear','state')
         
    if i.lower() == "thfireplaces.csv":
        read_csv('thfireplaces','state')
         
    if i.lower() == "townandcountryfireplaces.csv":
        read_csv('townandcountryfireplaces','state')
         
    if i.lower() == "welovefireplacesandgrills.csv":
        read_csv('welovefireplacesandgrills','state')
     
    if i.lower() == "ihp.csv":
        read_csv('ihp','state')
         
    if i.lower() == "ihp.csv":
        read_csv('ihp','state')   
         
    if i.lower() == "empirezoneheat.csv":
        read_csv('empirezoneheat','state')      
         
    if i.lower() == "whitemountainhearth.csv":
        read_csv('whitemountainhearth','state')   

    if i.lower() == "superiorfireplaces.csv":
        read_csv('superiorfireplaces','state')  
        
    if i.lower() == "hpbacanada.csv":
        read_csv('hpbacanada','state') 
         
         
         
    if i.lower() == "kozyheat.csv":
        read_csv('kozyheat','address')
         
    if i.lower() == "stollfireplace.csv":
        read_csv('stollfireplace','address')    
     
    if i.lower() == "kumastoves.csv":
        read_csv('kumastoves','address')         
 
    if i.lower() == "marquisfireplaces.csv":
        read_csv('marquisfireplaces','address')        
     
    if i.lower() == "morsoe.csv":
        read_csv('morsoe','address')  
         
    if i.lower() == "northwesthpba.csv":
        read_csv('northwesthpba','address')  
         
    if i.lower() == "rasmussengaslogs.csv":
        read_csv('rasmussengaslogs','address')  
         
    if i.lower() == "stuvamerica.csv":
        read_csv('stuvamerica','address')  
         
    if i.lower() == "twinstarhome.csv":
        read_csv('twinstarhome','address')  
         
    if i.lower() == "valorfireplaces.csv":
        read_csv('valorfireplaces','address')
        

        

     

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        