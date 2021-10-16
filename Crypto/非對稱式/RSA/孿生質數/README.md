# 孿生質數(Twin Prime)
## 概念
- 指一對相差 2 的質數
- Example：
    - (3, 5)
    - (5, 7)
    - (11, 13)
    - (17, 19)

## 分析(如何破解)
- n1、n2 分解
    - n1 = p*q
    - n2 = (p+2) * (q+2)
- 如何得到 p + q
    ```
    n2 = (p+2)*(q+2)
       = p*q + 2( p+q ) + 4
       = n1+ 2( p+q ) + 4

    p+q = ( n2 - n1 - 4 )/2
    ```
- n1、n2 phi(尤拉函數)
    ```
    n1_phi = (p-1)*(q-1)
           = pq - (p+q) + 1
           = n1 - (p+q) +1
    
    n2_phi = (p+1)*(q+1)
           = pq + (p+q) + 1
           = n1 + (p+q) +1
    ```
> 題目會給 n1 & n2

## Encrypt Test
- [Python Code](./Encrypt/create.py)
- [flag.txt](./Encrypt/flag.txt)
- [output.txt](./Encrypt/output.txt)

## Decrypt Test
- [Python Code](./Decrypt/solu.py)
- [encrypt.txt](./Decrypt/encrypt.txt)
- output
    ```
    Flag{Hello_This_Is_Test
    ```