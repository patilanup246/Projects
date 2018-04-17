# -*- coding: utf-8 -*-

import glob
import csv
import os
import json

for i in glob.glob("*.json"):
    print (i)
    with open(i) as f_i:
        j_dup = json.loads(f_i.read())

    unique = { each['address'] : each for each in j_dup }.values()
    #print (unique)
    f_j = open(i.split('_')[1],'w')
    f_j.write(str(json.dumps(list(unique))))
    f_j.close()
    
    
    
    
