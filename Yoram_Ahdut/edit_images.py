# -*- coding: utf-8 -*-
'''
Created on 09-Jan-2018

@author: Administrator
'''
import requests, csv, os
from pyquery import PyQuery
from selenium import webdriver
from glob import glob
from PIL import Image



images = ['9807462t1gnk-9013_1-1.jpg','9184341t1gnk-9011_1.png','6682919t11088x634038370278593750_l-1.jpg','5148383t11084x634038370272812500_l-copy-300x300.jpg','4698619t2gnk-9009_1.jpg','3007296t1gnk-9015_1-1.jpg']
for imga in images: 
    img = Image.open(imga)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] > 150 and item[1] > 150 and item[2] > 150:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    
    img.putdata(newData)
    img.save(imga+"_edited.png", "PNG")