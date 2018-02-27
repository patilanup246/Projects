'''
Created on May 14, 2017

@author: Mukadam
'''
from PIL import Image, ImageFilter
images_file = open('Input_files/before_women.txt','r').read().split('\n')
for image in images_file:
    im = Image.open('Images/before_women/'+image.replace('http://images.modelmydiet.com/i/','')) #Can be many different formats.
    try:
        pix = im.load()
    except Exception,e:
        continue
    print image.replace('http://images.modelmydiet.com/i/','')
    #print im.size #Get the width and hight of the image for iterating over
    #print pix[1,1] #Get the RGBA Value of the a pixel of an image
    
    
    #create a triangle of 
    
    
    for x in range(238,358):
        for y in range(0,120):
            pix[x,y] = (255, 255, 255) # Set the RGBA Value of the image (tuple)
    im.save('Images/before_women/'+image.replace('http://images.modelmydiet.com/i/',''))
    for x in range(0,120):
        for y in range(0,120):
            pix[x,y] = (255, 255, 255) # Set the RGBA Value of the image (tuple)
    im.save('Images/before_women/'+image.replace('http://images.modelmydiet.com/i/',''))
    for x in range(0,120):
        for y in range(679,799):
            pix[x,y] = (255, 255, 255) # Set the RGBA Value of the image (tuple)
    im.save('Images/before_women/'+image.replace('http://images.modelmydiet.com/i/',''))
    for x in range(238,358):
        for y in range(679,799):
            pix[x,y] = (255, 255, 255) # Set the RGBA Value of the image (tuple)        
    
    im.save('Images/before_women_modified/'+image.replace('http://images.modelmydiet.com/i/','')) # Save the modified pixels as png