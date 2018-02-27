import requests
import urllib
#f = open('categories.txt','w')
store_list_json = []
category_list = []
site1 = '?page=1;store=;site=ct;format=json;count=36;q=*'

def get_categories(site,stage):
    x = 'http://api.canadiantire.ca/search/api/v0/product/en/'+site
    r = requests.get(x).json()
    try:
        for cat in r['facets'][0]['facet-values']:
            if stage<5:
                if stage == 4:
                    print(cat['link'])
                    #f.write(cat['link']+'\n')
                    #f.flush()
                try:
                    get_categories(cat['link'], stage+1)
                except Exception as e:
                    print (e)
    except Exception as e:
        print (e)

def get_canadian_tire_store_list():
    global store_list_json
    store_list_json = requests.get('http://www.canadiantire.ca/dss/services/v2/stores?lang=en&radius=20000&maxCount=9999&storeType=store&lat=53.760861&lng=-98.813876').json()

def get_category_list():
    global category_list
    r = requests.get('http://api.canadiantire.ca/search/api/v0/product/en/?page=1;store=;site=ct;format=json;count=36;q=*').json()
    for category in r['facets'][0]['facet-values']:
        cat = {}
        cat[category['label']]= category['link']
        category_list.append(cat)

get_canadian_tire_store_list()
#get_category_list()
#print (category_list)


#read category list
f_cat = open('categories.txt').read().split('\n')

def get_price(sku,store):
    r = requests.get('http://services.canadiantire.ca/ESB/PriceAvailability?SKU='+sku+'&Store='+store+'&Banner=CTR&isKiosk=FALSE&Language=E').json()
    #print ('http://services.canadiantire.ca/ESB/PriceAvailability?SKU='+sku+'&Store='+store+'&Banner=CTR&isKiosk=FALSE&Language=E')
    promo_price = 0
    price = 0
    try:
        promo_price = r[0]['Promo']['Price']
    except Exception as e:
        pass
    try:
        price = r[0]['Price']
    except Exception as e:
        pass
    try:
        quantity = r[0]['Quantity']
    except:
        pass
    return {'promo_price':promo_price,'price':price,'quantity':quantity}


def get_cat_from_url(url):
    a = url.split(';')
    q1 =''
    q2 = ''
    q3 = ''
    q4 = ''
    for i in a:
        if (i.split('=')[0]=='q1'):
            q1 = urllib.unquote(i.split('=')[1]).replace('+',' ')
        if (i.split('=')[0]=='q2'):
            q2 = urllib.unquote(i.split('=')[1]).replace('+',' ')
        if (i.split('=')[0]=='q3'):
            q3 = urllib.unquote(i.split('=')[1]).replace('+',' ')
        if (i.split('=')[0]=='q4'):
            q4 = urllib.unquote(i.split('=')[1]).replace('+',' ')
    return {'q1':q1,'q2':q2,'q3':q3,'q4':q4}

for cat in f_cat:
    print ('http://api.canadiantire.ca/search/api/v0/product/en/'+cat)
    r = requests.get('http://api.canadiantire.ca/search/api/v0/product/en/'+cat).json()
    #for i in range(0,r['pagination']['total']):

    for p in r['results']:

        for s in store_list_json:
            #print (s)
            if len(p['field']['sku-id']) == 7:
                print(p['field']['prod-name'])
                print(p['field']['prod-id'])
                prices = get_price(p['field']['sku-id'],s['storeNumber'])
                print(prices['price'])
                print(prices['promo_price'])
                cate = get_cat_from_url(cat)
                print (cate['q1'])
                print (cate['q2'])
                print (cate['q3'])
                print (cate['q4'])
                print (s['storeName'],s['storeCityName'],s['storeProvince'],s['storePostalCode'],s['storeAddress1'],s['storeAddress2'])




#get_categories(site1,1)

