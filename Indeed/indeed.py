from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests
import csv
import re
import time


mydriver = webdriver.Chrome(executable_path='../chromedriver_win32/chromedriver.exe')
mydriver.get('https://www.indeed.com/jobs?q=software&l=Louisville%2C+KY&sort=date')
time.sleep(5)
pages = mydriver.find_element_by_id("resultsCol");
areas = pages.find_elements_by_css_selector('a');
for area in areas:
	apple = area.get_attribute('href')
	if apple is not None:
		pattern1 = re.search(r'\/rc\/', apple)
		pattern2 = re.search(r'\/pagead\/', apple)
		if pattern1 or pattern2:
			area.click()
			time.sleep(10)