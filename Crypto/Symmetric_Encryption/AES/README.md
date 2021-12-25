---
title: AES
tags: Crypto
lang: zh-tw
---

{%hackmd theme-dark %}

# 概述
- 全名 => [Advanced Encryption Standard](https://zh.wikipedia.org/wiki/%E9%AB%98%E7%BA%A7%E5%8A%A0%E5%AF%86%E6%A0%87%E5%87%86)
- 用來取代DES加密法(DEC已被證實為不安全的加密方式)
- 為[FIPS 197](https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf)標準
- AES演算法 = Rijndael演算法
    - Rijndael演算法 : 
        - 由比利時學者Joan Daemen和Vincent Rijmen所提出

# 設計準則
- 混淆 (Confusion) 最大限度地複雜化密文、明文與金鑰之間的關係，通常用非線性變換演算法達到最大化的混淆。
- 擴散 (Diffusion) 明文或金鑰每變動一位將最大化地影響密文中的位數，通常採用線性變換演算法達到最大化的擴散。

# 要求
- 支援128 bit 分組大小
- 128/192/256 bit 金鑰
- 安全性不低於3DES，但實施與執行要比3DES的更高效
- 優化過的ANSI C的實現程式碼
- KAT(Known-Answer tests)及MCT(Monte Carlo Tests)測試及驗證
- 軟體及硬體實現的便捷
- 可抵禦已知攻擊

# 加密流程(簡單介紹)
- 主要就是把明文(Plaintext)轉成二進位(Binary)，再拆成一塊一塊(Block)，每塊長度跟加密金鑰相同 => 明文區塊
- 再透過AES演算法將每一Block加密(Encrypt) => 密文區塊

# 加密模式
|Mode|Explain|
|----|----|
|MODE_ECB|[Electronic Code Book (ECB)](https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#ecb-mode)|
|MODE_CBC|[Cipher-Block Chaining (CBC)](https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode)|
|MODE_CFB|[Cipher FeedBack (CFB)](https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cfb-mode)|
|MODE_OFB|[Output FeedBack (OFB)](https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#ofb-mode)|
|MODE_CTR|[CounTer Mode (CTR)](https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#ctr-mode)|
|MODE_OPENPGP|[OpenPGP Mode](https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#openpgp-mode)|
|MODE_CCM|[Counter with CBC-MAC (CCM) Mode](https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#ccm-mode)|
|MODE_EAX|[EAX Mode](https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#eax-mode)|
|MODE_GCM|[Galois Counter Mode (GCM)](https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#gcm-mode)|
|MODE_SIV|[Syntethic Initialization Vector (SIV)](https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#siv-mode)|
|MODE_OCB|[Offset Code Book (OCB)](https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#ocb-mode)|

# 參考網頁
### 想了解更多關於AES可參考以下連結
- [reference_1](https://ithelp.ithome.com.tw/articles/10249488)
- [reference_2](https://www.readfog.com/a/1638277099874783232)
- [reference_3](https://www.itread01.com/content/1541892089.html)