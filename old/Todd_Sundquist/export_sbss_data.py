'''
Created on 07-Dec-2017

@author: Administrator
'''
import json
import csv
fileinput_json = json.loads(open('sidebysidestuff_output.txt').read())
output_f = open('sidebysidestuff_export.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)

# print (len(fileinput_json))
# j_keys = []
# for i in fileinput_json:
#     for k in i.keys():
#         j_keys.append(k)
# print ('start')
# listt = list(set(j_keys))
# listt.pop(0)
# 
# wr.writerow(listt)
# 
# for i in fileinput_json:
#     details = []
#     for l in listt:
#         try:
#             details.append(i[l])
#         except Exception as e:
#             #print (e)
#             details.append('')
#     wr.writerow(details)
#             

for i in fileinput_json:
    others = []
    details = []
    for k in i.keys():
        if k in ['URL','name','code','brand','availability','description','price','images']:

            details.append(i[k])
            #print (k)
        else:
            if not k in ['old_price','saved_amount']:
                others.append(k+' : '+i[k])
    
    details.append('\n'.join(others))
    #print (details)
    wr.writerow(details)