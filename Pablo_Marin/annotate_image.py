# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:20:49 2018

@author: PabloCastano
"""

#annotate image
import fitz
import sys, os, getopt
import requests
import base64
import json,io
from PIL import Image, ImageDraw
import re 
import pandas as pd

#class to deal with text
class class_text:
    """ Defines a class text object.
    
    Attributes: 
    Text and bounding polygi vertices 
    
    Methods:
    Calculates centroid of bounding polygon
    Comparison of classes
    Self Representation 
    
    """
    
    def __init__(self,text,vertices):
        self.text=text
        self.vertices=vertices
        self.x_start=vertices[0]['x']
        self.y_start=vertices[0]['y']
        self.x_end=vertices[2]['x']
        self.y_end=vertices[2]['y']
        
    @property
    def centroid(self):
        return (self.x_start+self.x_end)/2, (self.y_start+self.y_end)/2

    def __lt__(self, other):
        """Use "reading order" in a coordinate system where 0,0 is bottom left"""
        try:
            x0, y0 = self.centroid
            x1, y1 = other.centroid
            return (-y0,x0)<(-y1,x1)
        
        except AttributeError:
            return NotImplemented
            
    def __repr__(self):
        return 'Rectangle: ' + self.text

#pdf to png
def pdftoimages(input_dir,output_dir):
   """    
   Converts pdfs in input dir to .png and stores them in output_dir
   
   Args:
   input_dir = path to location of pdfs
   output_dir= path where images would be stored
   
   Returns:
   Saves a .png image to output_dir
   
   """ 
   dirListing = os.listdir(input_dir)
   files = []
   imagespath = output_dir
   for item in dirListing:
       files.append(item)
   n = len(files)
   for num in range(n):
       doc = fitz.open(input_dir+"/"+files[num])
       for img in doc.getPageImageList(0):
           xref = img[0]
           pix = fitz.Pixmap(doc, xref)
           if pix.n < 5:       # this is GRAY or RGB
               pix.writePNG(os.path.join(imagespath,"p%s-%s.png" % (num, xref)))
           else:               # CMYK: convert to RGB first
               pix1 = fitz.Pixmap(fitz.csRGB, pix)
               pix1.writePNG(os.path.join(imagespath,"p%s-%s.png" % (num, xref)))
               pix1 = None 
           pix=None
           break

   
#response from googgle api       
def get_response(image):
    """ Sends enconded image to google vision and gets json() response
    
    Args: 
    Image
    
    Returns:
    json with response
    
    """
    encoded = base64.b64encode(image.read())
    GOOGLE_CLOUD_VISION_API_URL = 'https://vision.googleapis.com/v1/images:annotate?key='
    API_KEY = 'AIzaSyCKFsYnfYoLFeD2OHpvcjky9opfhHKFnP0'
    api_url = GOOGLE_CLOUD_VISION_API_URL + API_KEY
    header = {'Content-Type': 'application/json'}
    body = json.dumps({
			'requests': [{
				'image': {
					'content': encoded.decode("utf-8"),
				},
				'features': [{
					'type': 'DOCUMENT_TEXT_DETECTION',
				}]
			}]
		})
    d = requests.post(api_url,data=body).json()
    return d

# get contents and bounds from google vision response. return them in a sorted list (by x,y position) of classes
def get_text_bounds(d):
    """ 
    From google vision json response, get text and boung polygon vertices. Each item is stored as class_text, in a list.
    After, sort this list using the class comparison we defined.
    
    Arg:
    d= json response
    
    Returns:
    sorted_xy= sorted list with english reading order 
    """
    text=[]
    item = 1
    while True:
        try:
            data = d['responses'][0]['textAnnotations'][item]['description']
            vert = d['responses'][0]['textAnnotations'][item]['boundingPoly']['vertices']  
            text.append(class_text(data,vert))
            item=item+1
        except:
            break    
    sorted_xy = sorted(text,reverse= True)
    return sorted_xy


# find field
def findfield(parsed_field,textbounds):
    """ 
    Looks for the name of the field in the textbounds, which was previously ordered using english grammar order (first y coordinate  then x coordinate) 
    Returns the bounding polygon
    
    Args:
    Parsed_Field= what we are looking
    TextBound=Ordered text list, with class_text types    
    
    Return:
    List with bounding polygons
    """
    x=len(parsed_field)
    for i in range(len(textbounds)-x):
        h=0
        for j in range(len(parsed_field)): 
            if textbounds[i+j].text.strip()==parsed_field[j].strip():   #similarity condition
                h=h+1
        if h==len(parsed_field):
            return [{'x':textbounds[i].x_start,'y':textbounds[i].y_start},{'x':textbounds[i+h-1].x_end,'y':textbounds[i+h-1].y_end}]
    return []


def draw_bounds(image,bounds,color):
    image=Image.open(image)
    draw=ImageDraw.Draw(image)
    for bound in list(bounds):
        #print (bound[0]['y'],bound[1]['y'],bound[2]['y'],bound[3]['y'])
        draw.polygon([(bound[0]['x'], bound[0]['y']),
                      (bound[1]['x'], bound[0]['y']),
                      (bound[1]['x'], bound[1]['y']),
                      (bound[0]['x'], bound[1]['y'])],
            None, color)  
        
    return image



# get response from google vision
input_dir='C:/Users/talib/workspace/Projects/Pablo_Marin/doc 8.pdf'
output_dir='C:/Users/talib/workspace/Projects/Pablo_Marin'
pdftoimages(input_dir,output_dir)
file=os.listdir(output_dir)[0]
with open(output_dir+'/'+file, "rb") as image:
    d=get_response(image)


# This is the ordered text
text=[i.text for i in get_text_bounds(d)]  

#search fields
#fields=['CNPJ/CEI' , 'Razão/Nome', 'CEP', '11 Nome', 'CPF', 'Data de Admissão' ,'Data do Prévio Aviso', 'Data de Afastamento','Cod.Afastamento', 'VALOR LÍQUIDO']
#text=[]
#for field in fields:
    #parsed_field=[word for word in re.split('(\W)', field) if word!=' ' ] 
    #text.append(findfield(parsed_field,get_text_bounds(d)))


#draw bounds
#with open(output_dir+'/'+file, "rb") as image:
 #   img=draw_bounds(image,text,'red')
  #  img.save('C:/Users/PabloCastano/Downloads/out/doc_annotated.png')
