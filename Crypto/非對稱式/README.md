---
title: 非對稱式加密
tags: Crypto
lang: zh-tw
---

{%hackmd theme-dark %}

# 概述
- 使用兩個不同但相關聯的密鑰，分別為公鑰(Public Key)和私鑰(Private Key)
    - 公鑰(可與他人分享) => 通常用來加密明文(Plaintext) => 密文(Ciphertext)

        ![](https://i.imgur.com/wZT6lVZ.png)

    - 私鑰(應保密) => 通常用來解開密文(Ciphertext) => 明文(Plaintext)
        
        ![](https://i.imgur.com/YzfB8NQ.png)
    
    - 也可以把公鑰跟私鑰的用法交換
- 每個使用者都會有一對金鑰

# 長度
- 愈長愈好(太短容易被解開)

# 優點
- 利用公鑰和私鑰解決了密鑰被截取的問題，因為就算拿到用來加密的key也沒辦法解開密文

# 缺點
- 與對稱式相比，非對稱式運行較緩慢，因為長度非常長
- 需要更多計算資源

# 種類
- [RSA](https://github.com/hehank/CTF_Practice/tree/main/Crypto/%E9%9D%9E%E5%B0%8D%E7%A8%B1%E5%BC%8F/RSA)
- [DSA (Digital Signature Algorithm)]()
- [ECC (Elliptic Curves Cryptography)]()

# 參考網頁
- [reference_1](https://academy.binance.com/zt/articles/symmetric-vs-asymmetric-encryption)
- [reference_2](https://medium.com/@RiverChan/%E5%9F%BA%E7%A4%8E%E5%AF%86%E7%A2%BC%E5%AD%B8-%E5%B0%8D%E7%A8%B1%E5%BC%8F%E8%88%87%E9%9D%9E%E5%B0%8D%E7%A8%B1%E5%BC%8F%E5%8A%A0%E5%AF%86%E6%8A%80%E8%A1%93-de25fd5fa537)
- [reference_3](https://www.itread01.com/content/1544153222.html)
