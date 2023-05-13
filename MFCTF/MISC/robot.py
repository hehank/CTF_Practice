from pwn import *
import time

r = remote('chals1.ais3.org', 12348)
# r = remote('localhost', 1234)

print(r.recvuntil(b'Let\'s go!\n'))

# for i in range(5):
#     s = r.recvline().decode()
#     print(s)
#     total = str(eval(s)).encode()
#     r.sendline(total)

# r.interactive()

try:
    for i in range(100):
        s = r.recvline().decode()
        print(s)
        total = str(eval(s)).encode()
        r.sendline(total)
        time.sleep(0.5)
except:
    # print(r.recvline())
    r.interactive()