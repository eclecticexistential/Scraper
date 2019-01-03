from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests
import csv
import re
import time


def get_contacts():
	words = ['Business', 'Zip', 'Phone', 'Certification', 'Country']
	array = []
	with open('final.csv', 'w') as write:
		csv_writer = csv.writer(write)
		csv_writer.writerow(['Name', 'City', 'State', 'Address', 'Zip Code', 'Phone', 'Website'])
		with open('contacts.csv', 'r') as reader:
			info = csv.reader(reader)
			for row in info:
				if len(row) > 0:
					sentence = (row[0].replace('\t', ' ')) + ' '
					name = re.search(r'^[A-Z][a-z]* [A-Z][a-z]*', sentence)
					if name:
						broke = name.group().split(' ')
						if broke[0] not in words:
							array.append(name.group())
					name2 = re.search(r'^[A-Z]. [A-Z][a-z]* [A-Z][a-z]*', sentence)
					if name2:
						array.append(name2.group())
					city_state = re.search(r'[A-Z][a-z]* [A-Z]{2}',sentence)
					if city_state:
						data = city_state.group()
						city = data[:-3]
						state = data[-2:]
						if len(city) > 2:
							array.append(city)
							array.append(state)
					street = re.search(r'Address .*', sentence)
					if street:
						loc = (street.group()).replace('Address ', '')
						check = loc.split(' ')
						if 'Ste.' not in check and check[1] != '2' and len(check) != 3:
							array.append(loc)
					zip_code = re.search(r'Zip Code \d{5}', sentence)
					if zip_code:
						digits = (zip_code.group()).replace('Zip Code ', '')
						array.append(digits)
					phone_number = re.search(r'Phone Number .*', sentence)
					if phone_number:
						phone = (phone_number.group()).replace('Phone Number ', '')
						array.append(phone)
					web_site = re.search(r'www..*.com', sentence)
					if web_site:
						array.append(web_site.group())
					end = re.search(r'Certification', sentence)
					if end:
					#'Name', 'City', 'State', 'Address', 'Zip Code', 'Phone', 'Website'
						if len(array) > 3:
							got_website = array[3]
							if got_website[:3] != 'www':
								array.append('Null')
								csv_writer.writerow(array)
							elif got_website[:3] == 'www':
								try:
									entry = array[0], array[1], array[2], array[4], array[5], array[6], array[3]
									csv_writer.writerow(entry)
								except IndexError:
									print("Check Zip Code.")
									print(array)
									entry = array[0], array[1], array[2], array[4], 'Null', array[5], array[3]
									csv_writer.writerow(entry)
						array = []
	
get_contacts()
	

