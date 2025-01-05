import instagram
import authenticator
import encrypt_decrypt
import json
import os

print('\n')

username = ''
password = ''
twofa = ''
secret = ''
reciever = ''
message = ''

def first_time_setup():
	username = input('Enter account username: ')
	password = input('Enter account password: ')
	twofa = input('Do you have 2FA? (y/n): ')
	secret = ''
	if twofa.lower() == 'y':
		secret = input('Enter Instagram secret code: ')

	rel = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(rel, 'login.json'), 'w', encoding='utf-8') as f:
		info = {
			'username': username,
			'password': encrypt_decrypt.encrypt(password).decode(),
			'twofa': twofa,
			'secret': encrypt_decrypt.encrypt(secret).decode()
		}

		json.dump(info, f)

def retrieve_user_info():
	rel = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(rel, 'login.json'), 'r') as f:
		info = json.load(f)

	username = info['username']
	password = encrypt_decrypt.decrypt(info['password'].encode())
	twofa = info['twofa']
	secret = encrypt_decrypt.decrypt(info['secret'].encode())

	return username, password, twofa, secret

if not os.path.isfile('login.json'):
	print('Running first time setup...')
	print('-' * 40 + '\n')
	first_time_setup()

receiver_username = input('Input reciever username: ')
message = input('Input message: ')

username, password, twofa, secret = retrieve_user_info()
code = authenticator.returnCode(secret)
instagram.bot(username=username, password=password, twofa=twofa, code=code, receiver=receiver_username, message=message)
