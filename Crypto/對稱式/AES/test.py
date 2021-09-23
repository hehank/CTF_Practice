#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES

obj = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')

message = b"flag(HappyCrypt)"

# ? Encrypt
ciphertext = obj.encrypt(message)
print(ciphertext)

# ? Decrypt
obj2 = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
print(obj2.decrypt(ciphertext))
