import requests

resp = requests.get('https://new-talibhmukadam.c9users.io/scraper?shops_root_url=http%3A%2F%2Fwww.saizeriya.co.jp%2Frestaurant%2Findex.php&via_page_url_regex=%5C%2Frestaurant%5C%2Fsearch_map%5C.php%5C%3Farea%28%5Cd%2B%29%3D%28%5Cd%2B%29&single_shop_url_regex=%5C%2Frestaurant%5C%2Fshop_detail%5C.php%5C%3Fcd%3D%28%5Cd%2B%29')
print resp.text.encode('ascii','ignore')