# -*- coding: utf-8 -*-
"""
Use this to get all ~55,000 of the allrecipes.com recipe URLs

@author: Derek
"""


from urllib.request import urlopen
# import pandas as pd
from bs4 import BeautifulSoup
import re
import pickle

# load using pickle
# urlList = pickle.load(open("urlList.p", "rb"))

# create empty list for URLs (unless you loaded previous URLs)
urlList = []

#f = open('abc.txt','w')


# loop through all 2827 pages
for i in range(1, 2):
#for i in range(1, 2828):
    # print page
    print(i)
    
    # specify url -- this will end up looping from page=1 through page=2827
    url = "http://allrecipes.com/recipes/?sort=Title&page=" + str(i)
    
    #Query the website and return the html to the variable 'page'
    page = urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    
    #print(soup.prettify())
    htmlUrls = soup.find_all('article', {'class': "fixed-recipe-card"})
#    htmlUrls = soup.find_all('article', {'class': "grid-col--fixed-tiles"})

    # use regex to extract the and paste the URLs, the append to the list
    for html in htmlUrls:
        temp = re.search('(?<=href="\/recipe)(.*)(?=">)', str(html))
        # if regex finds does not find a match, skip
        if temp != None:
            temp = "http://www.allrecipes.com/recipe" + str(temp.group(1))
            urlList.append(temp)


# use the output for scrape.py

# save urlList using pickle
pickle.dump(urlList, open( "urlList.p","wb" ))

# save text list
with open("urlList.txt", 'a') as out:
    for url in urlList:
        out.write(url + '\n')