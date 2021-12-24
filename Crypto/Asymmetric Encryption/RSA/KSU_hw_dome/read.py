from Crypto.PublicKey import RSA

# 讀取 RSA 金鑰
encodedKey = open("./Crypto/非對稱式/RSA/KSU_hw_dome/private.pem", "rb").read()

# 解析 RSA 金鑰
key = RSA.import_key(encodedKey)

# 輸出 RSA 私鑰
print(key.export_key().decode('utf-8'))
