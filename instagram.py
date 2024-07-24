#!/usr/bin/env python3
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import authenticator

driver = webdriver.Firefox()

class bot:
	def __init__(self, username, password, twofa, receiver, message):
		self.username = username
		self.password = password
		self.user = user
		self.message = message
		self.twofa = twofa
		self.base_url = 'https://www.instagram.com/accounts/login/'
		self.bot = driver
		self.login()

	def login(self):
		self.bot.get(self.base_url)

		# enter username
		enter_username = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'username')))
		enter_username.send_keys(self.username)

		# enter password
		enter_password = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'password')))
		enter_password.send_keys(self.password)

		enter_password.send_keys(Keys.RETURN)
		time.sleep(5)

		# enter 2FA
		enter_twofa = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'verificationCode')))
		enter_twofa.send_keys(self.twofa)

		enter_twofa.send_keys(Keys.ENTER)
		time.sleep(10)

		# save login pop-up
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div').click()
		time.sleep(5)

		# notification pop-up
		self.bot.find_element(By.XPATH,
							'/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
		time.sleep(2)

		# message button
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[5]/div/div/span/div/a/div/div[2]/div/div/span/span').click()
		time.sleep(5)

		# send message button
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div').click()
		time.sleep(2)

		# enter the username
		self.bot.find_element(By.XPATH,
							'/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input').send_keys(user)
		time.sleep(3)

		# click on the account
		self.bot.find_element(By.XPATH,
							'/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/label/div/input').click()
		time.sleep(1)

		# messages button
		self.bot.find_element(By.XPATH,
							'/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div').click()
		time.sleep(5)

		# click on text box
		send = self.bot.find_element(By.XPATH,
									'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
		send.click()
		time.sleep(1)

		# type message
		for i in self.message:
			send.send_keys(i)
		time.sleep(5)

		# send message
		send.send_keys(Keys.RETURN)
		time.sleep(5)


def init(username, password, two_FA_Code, reciever, message):
	bot(username, password, two_FA_Code, reciever, message)

	print("DONE")

auth_code = authenticator.returnTwoFA('Instagram')
user = '_lavannya_15'
message_ = 'THIS MESSAGE IS SEND TO YOU BY MY SCRIPT'
init('zenderwastaken', '02jISG#SNuP5krJ1', auth_code, user, message_)
