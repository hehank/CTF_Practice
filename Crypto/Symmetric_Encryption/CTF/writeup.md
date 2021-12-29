---
title: writeup
tags: Crypto
lang: zh-tw
---

{%hackmd theme-dark %}

# POODLE
### [Padding Oracle Attack](https://zh.wikipedia.org/wiki/%E5%AF%86%E6%96%87%E5%A1%AB%E5%A1%9E%E6%94%BB%E5%87%BB)
- 利用 CBC 會在要加密的字串的最後加上 Padding 和伺服器的回傳值來解出 Plaintext。
- 條件：
    - Server 接收到 User 輸入的值會回傳正確或錯誤。
    - User 要拿到 IV(才可以解開第一個 Block)。

### [CBC(Cipher-Block Chaining) encrypt](https://zh.wikipedia.org/wiki/%E5%88%86%E7%BB%84%E5%AF%86%E7%A0%81%E5%B7%A5%E4%BD%9C%E6%A8%A1%E5%BC%8F)
- 將 Plaintext 拆解成好幾個 Block(AES => 16Byte 一組，DES => 8Byte 一組)
- 第一個 Block 會跟 IV(Initialization Vector) 做 XOR
- 後面二、三、四、五.....個都會用前一個的 Ciphertext 來做 XOR
- 如果最後一個 Block 不夠 16 或 8 Byte，會 Padding 到足夠為止
- 如果 Plaintext 剛好夠，就會在最後加一個 Padding 的 Block(16 或 8 Byte)

### `Server.py`
```python=
#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from base64 import b64encode as b64e
from base64 import b64decode as b64d
from Crypto.Cipher import AES

# ? Get flag.txt content
flag = open('flag.txt', 'rb').read()

# ? Creat a random key
key = os.urandom(16)


def pad(msg):  # ? 判斷要加多長的 Pad

    # ? 看最後一個 Block 還要補多少 Byte 才會到 16 Byte
    pad_length = 16 - len(msg) % 16

    # ? 將 pad_length 長度的 pad 加回 msg
    return msg + bytearray([pad_length] * pad_length)


def unpad(msg):  # ? 移除 Pad
    byte = msg[-1]
    
    # ? 判斷 pad 的長度是否正確
    if msg[-byte] == bytearray([byte] * byte):
        return msg[:-byte]
    else:
        raise ValueError


def encrypt(data):  # ? 加密
    iv = os.urandom(16)
    aes = AES.new(key, AES.MODE_CBC, iv=iv)
    return iv + aes.encrypt(pad(data))


def decrypt(data):  # ? 解密
    
    # ? 將 iv 跟 data 分開
    iv, data = data[:16], data[16:]
    
    aes = AES.new(key, AES.MODE_CBC, iv=iv)
    return unpad(aes.decrypt(data))


print("Encrypt flag:", b64e(encrypt(flag)).decode())

while True:
    cipher = b64d(input("your cipher : ").strip())
    try:
        m = decrypt(cipher)
        print("OK")
    except ValueError:
        print("Padding Error")
    except Exception as e:
        print("Whoops...")
        break

```

### `solu.py`
```python=
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
```