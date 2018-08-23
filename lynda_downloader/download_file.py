'''
Created on 20-Dec-2017

@author: Administrator
'''
import requests
# rv = requests.get('https://files3.lynda.com/secure/courses/630600/VBR_MP4h264_main_HD720/630600_09_04_3D30_animation.mp4?7O7wramuHc8LIX2Do0ghxi1EDquj3-hH5TRebI6lQalodS8nIS0nyI6TLHvCtrwI9yH2PbXsi6Vg9njLJFEES5HjDrwnbAuLc7rbeALdk3OWw37xgQwp-QDRh_NBvteYM3tDYYwAp8oYJcEqAN6mNl-BqFXJLFr38jFICPaaCAbxosy1DASQqRjpLMi5k73bcQ&c3.ri=3769974259700046713')
# with open('aa'+'.mp4', "wb") as code:
#     code.write(rv.raw)

i = 1
for u in open('java_essential_training.txt').read().split('\n'):
    print (u.split('\t')[2])
    rv = requests.get(u.split('\t')[1])
    with open(str(i)+'  '+u.split('\t')[2].replace('/','').replace('\\','').replace(':','').replace('*','').replace('?','').replace('"','').replace('<','').replace('>','').replace('|','')+'.mp4', "wb") as code:
        code.write(rv.content)
    i+=1