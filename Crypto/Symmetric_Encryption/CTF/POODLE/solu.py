#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pwn
from base64 import b64encode as b64e
from base64 import b64decode as b64d


# cunuk = lambda x : [x[i:i+16] for i in range(0, len(x), 16)]
# ? 如上程式碼等於如下
# ? x = ciphertext
def chunk(ciphertext):
    cipher_block = []
    for i in range(0, len(ciphertext), 16):

        # ? 每一組 Block 16 Byte => AES_CBC
        cipher_block.append(ciphertext[i:i+16])

    return cipher_block


# xor = lambda a, b : bytes(ai ^ bi for ai, bi in zip(a, b))
# ? 如上程式碼等於如下
# ? a = previous_block, b = block, ai = i, bi = j
def xor(previous_block, block):

    # ? 如果 previous_block = "123"，block = 456，zip(previous_block, block) = ["14","25","36"]
    zip_block = zip(previous_block, block)

    xor_block = []
    for i, j in zip_block:
        xor_block.append(i ^ j)
    return bytes(xor_block)
