---
title: Openssl usage
tags: 崑山科大
lang: zh-tw
---

{%hackmd theme-dark %}

# openssl
- 介紹
    - OpenSSL 是一個加密工具包，實現了SSL v2/v3 和TLS v1 網絡協議以及它們所需的相關加密標準。
        - SSL：
            - Secure Sockets Layer(安全通訊層)
            - 用於保持網際網路連線安全以及防止在兩個系統之間發送的所有敏感資料被罪犯讀取及修改任何傳輸的資訊，包括潛在的個人詳細資料
        - TLS：
            - Transport Layer Security(傳輸層安全)
            - 是更新、更安全的 SSL 版本，通常也會稱為SSL
        - [參考網站](https://www.websecurity.digicert.com/zh/hk/security-topics/what-is-ssl-tls-https)
- 可用於：
    - 建立和管理私鑰(private keys)、公鑰(public keys)和參數(parameters)
    - 公鑰加密操作
    - 生成x.509證書、CSRs和CRLs
    - 計算Message Digests
        - Message Digests：
            - 訊息摘要
            - 從你要傳輸的訊息中，利用Hash Function加密所產生出來的
                - Hash Function：
                    - 常見的有：
                        - [MD5(Message-Digest algorithm 5)](https://zh.wikipedia.org/wiki/MD5)
                        - [SHA(Secure Hash Algorithm)](https://zh.wikipedia.org/wiki/SHA%E5%AE%B6%E6%97%8F)
                        - [MAC(Message Authentication Code)](https://zh.wikipedia.org/wiki/%E8%A8%8A%E6%81%AF%E9%91%91%E5%88%A5%E7%A2%BC)
                        - [HMAC(Hash-based Message Authentication Code)](https://zh.wikipedia.org/wiki/HMAC)
                    - 特性：
                        - 計算出Message Digests不須花太多時間
                        - 不可逆
                        - 不同訊息所算出來的Message Digests必須是不同的
            - 用來驗證訊息的完整性
            - [參考網站](https://david50.pixnet.net/blog/post/28798505)
    - 使用密碼(Ciphers)加密(Encryption)或解密(Decryption)
    - SSL / TLS 客戶端(Client)和伺服端(Server)測試
    - 處理[S / MIME](https://zh.wikipedia.org/wiki/S/MIME)的簽章(signed)或加密郵件
    - [時間戳](https://zh.wikipedia.org/wiki/%E6%99%82%E9%96%93%E6%88%B3)請求(requests)、生成(generation)和驗證(verification)
- [官方網站](https://www.openssl.org)
- [Github](https://github.com/openssl/openssl.git)

# openssl 下載
- [Kali Linux](https://www.kali.org/get-kali/#kali-platforms)
    - kali linux 已經幫你下載好openssl了
- [Ubuntu 20.04](https://ubuntu.com/download/desktop)
    ```shell=
    sudo apt install openssl
    ```
# openssl -help
- [官方man page](https://www.openssl.org/docs/manmaster/man1/openssl.html)
```shell=
Standard commands
asn1parse         ca                ciphers           cms               
crl               crl2pkcs7         dgst              dhparam           
dsa               dsaparam          ec                ecparam           
enc               engine            errstr            gendsa            
genpkey           genrsa            help              list              
nseq              ocsp              passwd            pkcs12            
pkcs7             pkcs8             pkey              pkeyparam         
pkeyutl           prime             rand              rehash            
req               rsa               rsautl            s_client          
s_server          s_time            sess_id           smime             
speed             spkac             srp               storeutl          
ts                verify            version           x509              

Message Digest commands (see the 'dgst' command for more details)
blake2b512        blake2s256        gost              md4               
md5               rmd160            sha1              sha224            
sha256            sha3-224          sha3-256          sha3-384          
sha3-512          sha384            sha512            sha512-224        
sha512-256        shake128          shake256          sm3               

Cipher commands (see the 'enc' command for more details)
aes-128-cbc       aes-128-ecb       aes-192-cbc       aes-192-ecb       
aes-256-cbc       aes-256-ecb       aria-128-cbc      aria-128-cfb      
aria-128-cfb1     aria-128-cfb8     aria-128-ctr      aria-128-ecb      
aria-128-ofb      aria-192-cbc      aria-192-cfb      aria-192-cfb1     
aria-192-cfb8     aria-192-ctr      aria-192-ecb      aria-192-ofb      
aria-256-cbc      aria-256-cfb      aria-256-cfb1     aria-256-cfb8     
aria-256-ctr      aria-256-ecb      aria-256-ofb      base64            
bf                bf-cbc            bf-cfb            bf-ecb            
bf-ofb            camellia-128-cbc  camellia-128-ecb  camellia-192-cbc  
camellia-192-ecb  camellia-256-cbc  camellia-256-ecb  cast              
cast-cbc          cast5-cbc         cast5-cfb         cast5-ecb         
cast5-ofb         des               des-cbc           des-cfb           
des-ecb           des-ede           des-ede-cbc       des-ede-cfb       
des-ede-ofb       des-ede3          des-ede3-cbc      des-ede3-cfb      
des-ede3-ofb      des-ofb           des3              desx              
rc2               rc2-40-cbc        rc2-64-cbc        rc2-cbc           
rc2-cfb           rc2-ecb           rc2-ofb           rc4               
rc4-40            seed              seed-cbc          seed-cfb          
seed-ecb          seed-ofb          sm4-cbc           sm4-cfb           
sm4-ctr           sm4-ecb           sm4-ofb
```

## asn1parse
- 解析 ASN.1 序列
## 

# openssl enc -help
```shell=
Usage: enc [options]
Valid options are:
 -help               Display this summary
 -list               List ciphers
 -ciphers            Alias for -list
 -in infile          Input file
 -out outfile        Output file
 -pass val           Passphrase source
 -e                  Encrypt
 -d                  Decrypt
 -p                  Print the iv/key
 -P                  Print the iv/key and exit
 -v                  Verbose output
 -nopad              Disable standard block padding
 -salt               Use salt in the KDF (default)
 -nosalt             Do not use salt in the KDF
 -debug              Print debug info
 -a                  Base64 encode/decode, depending on encryption flag
 -base64             Same as option -a
 -A                  Used with -[base64|a] to specify base64 buffer as a single line
 -bufsize val        Buffer size
 -k val              Passphrase
 -kfile infile       Read passphrase from file
 -K val              Raw key, in hex
 -S val              Salt, in hex
 -iv val             IV in hex
 -md val             Use specified digest to create a key from the passphrase
 -iter +int          Specify the iteration count and force use of PBKDF2
 -pbkdf2             Use password-based key derivation function 2
 -none               Don't encrypt
 -*                  Any supported cipher
 -rand val           Load the file(s) into the random number generator
 -writerand outfile  Write random data to the specified file
 -engine val         Use engine, possibly a hardware device
```

# openssl 用法