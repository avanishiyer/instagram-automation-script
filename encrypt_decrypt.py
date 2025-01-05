from cryptography.fernet import Fernet
import os

def generate_key():
	key = Fernet.generate_key()

	print(type(key))
	rel = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(rel,'.key'), 'w') as f:
		f.write(key.decode())

def encrypt(txt):
	if not os.path.isfile('.key'):
		generate_key()

	rel = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(rel,'.key'), 'r') as f:
		key = f.read().encode()
		fernet = Fernet(key)

	enc = fernet.encrypt(txt.encode())
	return enc

def decrypt(txt):
	rel = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(rel,'.key'), 'r') as f:
		key = bytes(f.read(), 'utf-8')
		fernet = Fernet(key)

	dec = fernet.decrypt(txt).decode()
	return dec
