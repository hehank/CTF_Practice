#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from pwn import *
from base64 import b64encode, b64decode

conn = remote("120.114.62.209", 4121)

conn.recvuntil(b">")
conn.sendline(b"1")

# username:admin
# =>
# username:aaaaaa; password:aaaaaaa username:admin;;
# XXXXXXXXXXXXXXXX XXXXXXXXXXXXXXXX XXXXXXXXXXXXXXXX XXXXXXXXXXXXXXXX

username = b"aaaaaa"
password = b"aaaaaaausername:admin;"

conn.recvuntil(b":")
conn.sendline(username)

conn.recvuntil(b":")
conn.sendline(password)

token = b64decode(conn.recvline())[32:]

conn.recvuntil(b">")
conn.sendline(b"2")

print(conn.recvuntil(b":"))

conn.sendline(b64encode(token))
print(conn.recvline())
