from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests
import csv
import re
import time

username = ''
password = ''

def get_contacts(user):
	follower_names = []
	following_names = []
	mydriver = webdriver.Chrome(executable_path='../chromedriver_win32/chromedriver.exe')
	mydriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
	time.sleep(5)
	inputs = mydriver.find_elements_by_class_name('zyHYP')
	for key,input in enumerate(inputs):
		if key == 0:
			input.send_keys(username)
		if key == 1:
			input.send_keys(password)
	button = mydriver.find_element_by_class_name('L3NKy')
	button.click()
	time.sleep(5)
	accept = mydriver.find_element_by_class_name('HoLwm')
	accept.click()
	search = mydriver.find_element_by_class_name('x3qfX')
	search.send_keys(user)
	time.sleep(10)
	double_ll = mydriver.find_elements_by_class_name('yCE8d')
	for key,double in enumerate(double_ll):
		if key == 0:
			double.click()
	time.sleep(5)
	follow_links = mydriver.find_elements_by_class_name('Y8-fY')
	for key, link in enumerate(follow_links):
		if key == 1:
			link.click()
			followers = mydriver.find_elements_by_class_name('FPmhX')
			for follower in followers:
				follower_names.append(follower.text)
			time.sleep(5)
			exit = mydriver.find_element_by_class_name('glyphsSpriteX__outline__24__grey_9')
			exit.click()
	follow_links = mydriver.find_elements_by_class_name('Y8-fY')
	for key, link in enumerate(follow_links):
		if key == 2:
			link.click()
			followings = mydriver.find_elements_by_class_name('FPmhX')
			for following in followings:
				following_names.append(following.text)
			time.sleep(5)
			exit = mydriver.find_element_by_class_name('glyphsSpriteX__outline__24__grey_9')
			exit.click()
	time.sleep(120)
	with open('followers.csv', 'w') as write:
		csv_writer = csv.writer(write)
		for name in follower_names:
			csv_writer.writerow([name])
	with open('following.csv', 'w') as write:
		csv_writer = csv.writer(write)
		for name in following_names:
			csv_writer.writerow([name])
	
get_contacts('sethrogen')

