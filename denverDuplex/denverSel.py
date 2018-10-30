from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import csv

data_set = []
prices = []

def job(url, row):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_class_name("reply_button").click()
	### row.append(driver.find_element_by_id("replylink").input.value)
	### data_set.append(row)
	
def get_info(url, row):
	headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
	with requests.Session() as s:
		get_data = s.get(url, headers=headers)
		soup = BeautifulSoup(get_data.content, 'lxml')
		print(soup)
		descr = soup.find('section', id='postinbody')
		pattern = re.search(r"\$\d+", descr.text)
		if pattern:
			print(pattern.group())
			# row.append(pattern.group())
		if pattern == '':
			print('null')
			# row.append('No info')
		
	#job(url, row)
		
def retrieve_url(file):
	with open(file) as csv_file:
		reader = csv.reader(csv_file)
		headers = next(reader)
		for row in reader:
			if row != []:
				print('going in')
				get_info(row[1], row)
				time.sleep(random.randint(1,6))

retrieve_url('denverRoo.csv')
retrieve_url('denverApa.csv')
				
#csv_file = open('denverCombo.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['City', 'URL', 'Title', 'DatePosted', 'Price', 'Email', 'Phone'])
# for data in data_set:
	# csv_writer.writerow([data])