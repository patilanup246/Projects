import requests

url = "https://api.yelp.com/v3/businesses/search"

querystring = {"term":"","latitude":"42.375998","longitude":"-72.149388","categories":"gyms"}

headers = {'authorization': 'Bearer Pg3GkiiyQHRGyx9VaDjJ1zdLqo-gZDbDKvjGcFYrN-FEM0-x_j_w-rE1v1JqheL85OQW43aDQ63pkdWii2AI7Dweb1cS68Y8_Pa8Bz2X4VQnvk_zCDB_bV5xLMXEWXYx'}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
