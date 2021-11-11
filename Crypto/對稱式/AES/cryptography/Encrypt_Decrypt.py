#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = os.urandom(32)
# ? iv => initialization vector
iv = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

# ? Encrypt
encryptor = cipher.encryptor()
# ciphertext = encryptor.update(b"This_is_test_hi.") + encryptor.finalize()
ciphertext = encryptor.update(b"This_is_test_hi.")
print(ciphertext)

# ? Decrypt
decryptor = cipher.decryptor()
# plaintext = decryptor.update(ciphertext) + decryptor.finalize()
plaintext = decryptor.update(ciphertext)
print(plaintext)
