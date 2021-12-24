#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Cipher import DES

# ? 密鑰為 8byte or 16byte
key = b'not_good'

cipher = DES.new(key, DES.MODE_OFB)
d_cipher = DES.new(key, DES.MODE_OFB)

# ? 明文要為8的倍數
plaintext = b'This_is_tttttest'

# ? Eecrypt
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

# ? Decrypt
plain = d_cipher.decrypt(ciphertext)
print(plaintext)
