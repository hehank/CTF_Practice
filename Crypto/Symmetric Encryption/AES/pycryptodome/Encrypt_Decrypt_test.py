#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES

cipher = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')

message = b"flag(HappyCrypt)"

# ? Encrypt
ciphertext = cipher.encrypt(message)
print(ciphertext)

# ? Decrypt
d_cipher = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
print(d_cipher.decrypt(ciphertext))
