#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES

obj = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')

message = b"flag(HappyCrypt)"

ciphertext = obj.encrypt(message)
print(ciphertext)
