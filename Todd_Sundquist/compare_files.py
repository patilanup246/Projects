# -*- coding: utf-8 -*-
'''
Created on 05-Feb-2018

@author: Administrator
'''
import csv
import sys


file1 = sys.argv[1]
file2 = sys.argv[2]
# file1 = 'superatv_export-01-30-18.csv'
# file2 = 'superatv_export-02-02-18.csv'
readCSV1 = csv.reader(open(file1,encoding='utf-8'), delimiter=',')
readCSV2 = csv.reader(open(file2,encoding='utf-8'), delimiter=',')

csv1 = []
csv2 = []

cc1 = []
cc2 = []

output_f = open('compare_results.csv','w',encoding='utf-8', newline='')
wr = csv.writer(output_f, quoting=csv.QUOTE_ALL)
wr.writerow(['Issue','Title','SKU','From','To'])
for row in readCSV1:
    cc1.append (row)
    csv1.append (row[8])
    
for row in readCSV2:
    cc2.append(row)
    csv2.append (row[8])
    
    
for c1 in cc1:
    for c2 in cc2:
        if c1[8] == c2[8]:
            if not c1[14] == c2[14]:
                details = []
                details.append('Price Changed')
                details.append(c1[9])
                details.append(str(c1[8]))
                details.append(c1[14])
                details.append(c2[14])
                wr.writerow(details)
            if not c1[11] == c2[11]:
                details = []
                details.append('Fitment Changed')
                details.append(c1[9])
                details.append(str(c1[8]))
                details.append(c1[11])
                details.append(c2[11])
                wr.writerow(details)

            
            break
csv1 = list(set(csv1))
csv2 = list(set(csv2))

for c1 in csv1:
    if not c1 in csv2:
        details = []
        details.append('Removed SKU')
        details.append('')
        details.append(str(c1))
        details.append('')
        details.append('')
        wr.writerow(details)
        
for c2 in csv2:
    if not c2 in csv1:
        details = []
        details.append('Added SKU')
        details.append('')
        details.append(str(c2))
        details.append('')
        details.append('')
        wr.writerow(details)
