#!/usr/bin/env python3
import os
import time
import json
import hmac
import base64
import struct
import hashlib

# main magical function
def get_hotp_token(secret, intervals_no):
	key = base64.b32decode(normalize(secret), True)
	msg = struct.pack(">Q", intervals_no)
	h = bytearray(hmac.new(key, msg, hashlib.sha1).digest())
	o = h[19] & 15
	h = str((struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000)

	return prefix0(h)


# The TOTP token is just a HOTP token seeded with every 30 seconds
def get_totp_token(secret):
	return get_hotp_token(secret, intervals_no=int(time.time())//30)


# Normalizes secret by removing spaces and padding with = to a multiple of 8
def normalize(key):
	k2 = key.strip().replace(' ','')
	if len(k2)%8 != 0:
		k2 += '='*(8-len(k2)%8)

	return k2

# Prefixes code with leading zeros if missing
def prefix0(h):
	if len(h) < 6:
		h = '0'*(6-len(h)) + h

	return h


def returnTwoFA(label):
	rel = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	with open(os.path.join(rel,'secrets.json'), 'r') as f:
		secrets = json.load(f)
	for x, key in sorted(list(secrets.items())):
		if x == label:
			return get_totp_token(key)
