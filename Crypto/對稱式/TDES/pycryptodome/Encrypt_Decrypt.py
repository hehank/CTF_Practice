#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import DES3
from Crypto import Random

key = b'I_want_to_sleep.'
iv = Random.new().read(DES3.block_size)

cipher = DES3.new(key, DES3.MODE_OFB, iv)
d_cipher = DES3.new(key, DES3.MODE_OFB, iv)
plaintext = b'This_is_the_ttttttttttttttest.'

# ? Encrypt
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

# ? Decrypt
plain = d_cipher.decrypt(ciphertext)
# plain = d_cipher.decrypt(ciphertext)
# plain = d_cipher.decrypt(ciphertext)
print(plain)
