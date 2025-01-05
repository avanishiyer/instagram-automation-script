#!/usr/bin/env python3
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import authenticator

class bot:
	def __init__(self, username: str, password: str, twofa: bool, code: str, receiver: str, message: str):
		driver = webdriver.Firefox()

		self.username = username
		self.password = password
		self.receiver = receiver
		self.message = message
		self.twofa = twofa
		self.code = code
		self.login_url = 'https://www.instagram.com/accounts/login/'
		self.dm_url = 'https://www.instagram.com/direct/inbox/'
		self.bot = driver

		self.login()

	def login(self):
		self.bot.get(self.login_url)

		# enter username
		enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
		enter_username.send_keys(self.username)

		# enter password
		enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
		enter_password.send_keys(self.password)

		# press RETURN to go to next screen
		enter_password.send_keys(Keys.RETURN)

		# if account has 2FA
		if self.twofa:
			time.sleep(5)

			# enter 2FA
			enter_code = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'verificationCode')))
			enter_code.send_keys(self.code)

			# press RETURN to go to next screen
			enter_code.send_keys(Keys.ENTER)

		# waiting for page to load
		time.sleep(7)

		# save login pop-up --> press do not save
		WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'div.x1i10hfl'))).click()

		# notification pop-up --> press not now
		WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'button._a9--:nth-child(2)'))).click()

		# messages page
		self.bot.get(self.dm_url)

		# send message button
		WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.xjyslct'))).click()

		# enter the username in input field
		WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'queryBox'))).send_keys(self.receiver)

		# click the tick-box to select the account
		self.bot.find_element(By.XPATH, 'div.x1dm5mii:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > \
			div:nth-child(3) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > input:nth-child(2)').click()
		time.sleep(1)

		# click 'chat' button
		WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.xn3w4p2'))).click()
		time.sleep(5)

		# click on messages text box
		send = self.bot.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div\
			/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
		send.click()
		time.sleep(1)

		# type the message
		# used for loop to solve issue where it won't send the whole message, just the first letter
		for i in self.message:
			send.send_keys(i)
		time.sleep(1)

		# pressing RETURN to sent the message
		send.send_keys(Keys.RETURN)
		time.sleep(2)

		# closing browser
		self.bot.close()


# print('Using account: ' + account_username)
# receiver_username = input('Enter reciever username: ')
# message_ = input('Message: ')

# init(account_username, account_password, auth_code, receiver_username, message_)
