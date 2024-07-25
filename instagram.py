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
		self.receiver = receiver
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

		# press RETURN to go to next screen
		enter_password.send_keys(Keys.RETURN)
		time.sleep(5)

		# enter 2FA
		enter_twofa = WebDriverWait(self.bot, 20).until(
			expected_conditions.presence_of_element_located((By.NAME, 'verificationCode')))
		enter_twofa.send_keys(self.twofa)

		# press RETURN to go to next screen
		enter_twofa.send_keys(Keys.ENTER)
		time.sleep(10)

		# save login pop-up --> press do not save
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div').click()
		time.sleep(5)

		# notification pop-up --> press not now
		self.bot.find_element(By.XPATH,
							'/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
		time.sleep(2)

		# click messages button in the right collumn
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[5]/div/div/span/div/a/div/div[2]/div/div/span/span').click()
		time.sleep(5)

		# send message button
		self.bot.find_element(By.XPATH,
							'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div').click()
		time.sleep(2)

		# enter the username in input field
		self.bot.find_element(By.XPATH,
							'/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input').send_keys(self.receiver)
		time.sleep(3)

		# click the tick-box to select the account
		self.bot.find_element(By.XPATH,
							'/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/label/div/input').click()
		time.sleep(1)

		# click 'chat' button
		self.bot.find_element(By.XPATH,
							'/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div').click()
		time.sleep(5)

		# click on messages text box
		send = self.bot.find_element(By.XPATH,
									'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
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


# calling the main function through an initialising function
def init(username, password, two_FA_Code, reciever, message):
	bot(username, password, two_FA_Code, reciever, message)

	print("DONE")

auth_code = authenticator.returnTwoFA('Instagram')
account_username = 'zenderwastaken'
account_password = '02jISG#SNuP5krJ1'
receiver_username = ''
message_ = ''

print('Using account: ' + account_username)
receiver_username = input('Enter reciever username: ')
message_ = input('Message: ')

init(account_username, account_password, auth_code, receiver_username, message_)
