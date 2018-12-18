from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests
import csv
import re
import time


def check_email(user, passw, num=0):
	mydriver = webdriver.Chrome(executable_path='../chromedriver_win32/chromedriver.exe')
	mydriver.get('https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1')
	time.sleep(2)
	email = mydriver.find_element_by_id('identifierId')
	email.send_keys(user)
	time.sleep(3)
	next = mydriver.find_element_by_id('identifierNext')
	next.click()
	time.sleep(5)
	password = mydriver.find_element_by_name('password')
	password.send_keys(passw)
	nextBtn = mydriver.find_element_by_id('passwordNext')
	nextBtn.click()
	if(user == 'seriouslyyouguysseriously@gmail.com' and num != 0):
		compose = mydriver.find_element_by_id(':iy').find_element_by_class_name('T-I J-J5-Ji T-I-KE L3')
		compose.click()
		while(num > 0):
			time.sleep(30)
			num -= 1

credentials = {0:[],1:[]}
dur = len(credentials)-1

while dur >= 0:
	stats = credentials[dur]
	check_email(stats[0],stats[1])
	time.sleep(30)
	dur-=1


