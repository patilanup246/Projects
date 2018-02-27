'''
Created on May 5, 2017

@author: Mukadam
'''
import urllib
images_file = open('file_images.txt','r').read().split('\n')
for image in images_file:
    print images_file.index(image)
    print 'Images/'+image.replace('http://images.gotinder.com/','').rsplit('/')[1]
    urllib.urlretrieve(image, 'Images/'+image.replace('http://images.gotinder.com/','').rsplit('/')[1])