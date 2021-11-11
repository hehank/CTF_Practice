#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes

key = os.urandom(16)
# ? iv => initialization vector
iv = os.urandom(8)

cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv))

# ? Encrypt
encryptor = cipher.encryptor()
ciphertext = encryptor.update(b"This_is_TDES_ha.")
print(ciphertext)

# ? Decrypt
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext)
print(plaintext)
