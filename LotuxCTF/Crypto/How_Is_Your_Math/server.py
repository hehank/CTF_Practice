from Crypto.Cipher import AES
import sys
import os

from secret import FLAG

aes_cbcmode_info = '''
##################################################################
#                     AES CBC Mode (Decrypt)                     #
##################################################################
#                                                                #
#          -----------         -----------         -----------   #
#         |  cipher1  |---*   |  cipher2  |---*   |  cipher3  |  #
#          -----------    |    -----------    |    -----------   #
#               |         |         |         |         |        #
#          -----------    |    -----------    |    -----------   #
#         |           |   |   |           |   |   |           |  #
#         |  Decrypt  |   |   |  Decrypt  |   |   |  Decrypt  |  #
#         |           |   |   |           |   |   |           |  #
#          -----------    |    -----------    |    -----------   #
#   ------      |         |         |         |         |        #
#  |  IV  | --> ⊕         *-------> ⊕         *-------> ⊕        #
#   ------      |                   |                   |        #
#          -----------         -----------         -----------   #
#         |  plain1   |       |  plain2   |       |  plain3   |  #
#          -----------         -----------         -----------   #
#                                                                #
##################################################################
'''.strip()


def encrypt(plain: bytes, key: bytes, iv: bytes):
    assert (len(plain) % 16) == 0

    aes = AES.new(key, AES.MODE_CBC, iv=iv)
    return aes.encrypt(plain)


def decrypt(cipher: bytes, key: bytes, iv: bytes):
    assert (len(cipher) % 16) == 0

    aes = AES.new(key, AES.MODE_CBC, iv=iv)
    return aes.decrypt(cipher)


def main():
    print(aes_cbcmode_info, end='\n\n')

    iv = os.urandom(16)
    key = os.urandom(16)
    plain = os.urandom(48)
    cipher = encrypt(plain, key, iv)
    new_plain_block = os.urandom(16)

    print(f'cipher : {cipher.hex()}')
    print(f'last block of plain : {plain[-16:].hex()}')
    print(f'let the last block of plain change to :  {new_plain_block.hex()}')
    print()

    new_cipher = bytes.fromhex(input('new cipher > '))
    assert len(new_cipher) == len(cipher)
    if decrypt(new_cipher, key, iv)[-16:] == new_plain_block:
        print(f'Flag : {FLAG}')
    else:
        print('Wrong!')


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit()