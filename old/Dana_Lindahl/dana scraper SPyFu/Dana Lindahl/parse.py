import pandas as pd
import re
from selenium import webdriver
import time
from datetime import datetime

import sys


def sanit_url(url):
	match = re.search(r'^(https?://)?(.*)', url)

	return match.group(2)

def get_budget(url, driver):
	#driver.get(url)
	get_num_js_code = 'return document.getElementsByClassName("seo-overview-small-chart-number-digits").length'
	get_val_js_code = 'return document.getElementsByClassName("seo-overview-small-chart-number-digits")[2].innerText'
	get_oops_text = 'return document.getElementsByClassName("oops-text").length'

	oops_text_found = False

	for i in range(20):
		num = driver.execute_script(get_num_js_code)
		if driver.execute_script(get_oops_text) > 0:
			oops_text_found = True
		if num != 0 or oops_text_found:
			break;
		time.sleep(1)

	if num == 0:
		if oops_text_found:
			return 'No data'
		else :
			raise RuntimeError('A budget value cannot be loaded for url {}. Please check internet connection or contact application developer.',format(url))

	budget = driver.execute_script(get_val_js_code)

	return budget


websites_df = pd.read_csv('input.csv', usecols=['Website'])
websites_df.columns = ['url']


websites_df = websites_df[websites_df['url'].notnull()]
websites_df = websites_df.drop_duplicates();
websites_df['url'] = websites_df['url'].apply(sanit_url)

# Getting subset

#websites_df = websites_df[1640:1653]


driver = webdriver.Chrome()

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def gutMultipleUrls(urls, driver):
	d_curr_w_hndl = driver.current_window_handle
	init_win_hndls = driver.window_handles

	output = []

	for url in urls:
		driver.execute_script('window.open(arguments[0]);', url)

	for index, win_handle in enumerate([handle for handle in driver.window_handles if handle not in init_win_hndls]):
		driver.switch_to.window(win_handle)

		budget = get_budget(driver.current_url, driver)

		output.append({'url': driver.current_url, 'budget': budget})

		driver.close()

	# Switching back to initial window
	driver.switch_to.window(d_curr_w_hndl)

	return output



budgets_data = [];

total_urls = websites_df.shape[0]

url_chunk_size = 5

i = url_chunk_size
o_file_name = 'budgets ' + datetime.now().strftime('%Y-%m-%d %H-%M-%S') + '.csv'

for url_chunk in chunks(websites_df['url'], url_chunk_size):

	url_chunk = list(map(lambda x: 'https://www.spyfu.com/ppc/overview/domain?query=' + x, list(url_chunk)))

	#spyfu_url = 'https://www.spyfu.com/ppc/overview/domain?query=' + url

	budgets = gutMultipleUrls(list(url_chunk), driver)

	budgets_data += budgets

	print('{} of {} urls parsed ({:.1f}%).'.format(i, total_urls, i/total_urls*100), end='\r')

	#saving partial data every 100 iterations
	if i % 50 == 0:
		budgets_df = pd.DataFrame(budgets_data)
		budgets_df.to_csv(o_file_name, index=False, columns=['url', 'budget'], header=['Domain', 'Est AdWords Monthly Budget'])

	i += len(url_chunk)


driver.quit()	


budgets_df = pd.DataFrame(budgets_data)
budgets_df.to_csv(o_file_name, index=False, columns=['url', 'budget'], header=['Domain', 'Est AdWords Monthly Budget'])

print('')
print('Done')

