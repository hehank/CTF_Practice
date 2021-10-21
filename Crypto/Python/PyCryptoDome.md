---
title: PyCryptoDome_Usage
tags: Crypto
lang: zh-tw
---

{%hackmd theme-dark %}

# AES
## Encrypt & Decrypt
- code : 
	```python=
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
    ```

- output : 
    ```shell=
    b'J\xae\xd1J\xbdS\x8d\x99\xaf\xc3N\xba\xde\xeb>['
    b'flag(HappyCrypt)'
    ```
    
# RSA