from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode
import time


def aes_encrypt(file_path, key):
    key = key.encode('UTF-8')
    key = pad(key, AES.block_size)
    with open(file_path, 'rb') as entry:
        data = entry.read()
        cipher = AES.new(key, AES.MODE_CFB)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))
        iv = b64encode(cipher.iv).decode('UTF-8')
        ciphertext = b64encode(ciphertext).decode('UTF-8')
        to_write = iv + ciphertext
    entry.close()

    with open(file_path + '.enc', 'w') as data:
        data.write(to_write)
    data.close()
    return file_path + '.enc'
