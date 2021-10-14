---
title: RSA
tags: Crypto
lang: zh-tw
---


{%hackmd theme-dark %}


# RSA
- 基於數學難題所設計出來的演算法，對極大整數無法進行因數分解的難題，證實 RSA 演算法的可靠性。

## 產生金鑰對(Key Pairs Generation)
1. 找出兩個超⼤質數 p,q
2. N = p * q
3. φ(N) = (p-1) * (q-1)
4. e = 任意質數(要滿足 gcd(e ,φ(N) ) = 1)
5. d = inverse(e, φ(N))
    - inverse() => 求模反元素(Modular multiplicative inverse)
        - 兩個數字相乘後，除以模數的餘數= 1
    - d = e 在模數 φ(n) 下的模反元素
        - e * d mod φ(n) = 1
6. 把 p, q 丟掉

### Encrypt
- M(明文)^e mod N = C(密文)

![](https://i.imgur.com/xILmBqW.png)

### Decrypt
- C(密文)^d mod N = M(明文)

![](https://i.imgur.com/gTlqgy2.png)

### Public Key
- (N, e)

### Private Key
- (N, d)

## Reference Link
- [Day 23. 非對稱式加密演算法 - RSA (觀念篇)](https://ithelp.ithome.com.tw/articles/10250721)
- [RSA公開金鑰.md](https://github.com/MyFirstSecurity2020/MyfirstCryptoX/blob/main/%E7%8F%BE%E4%BB%A3%E5%AF%86%E7%A2%BC/%E5%85%AC%E9%96%8B%E9%87%91%E9%91%B0/RSA%E5%85%AC%E9%96%8B%E9%87%91%E9%91%B0.md)