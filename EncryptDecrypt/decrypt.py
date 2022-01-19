from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode
import os
import getpass


def aes_decrypt(file_path, key):

    key = key.encode('UTF-8')
    key = pad(key, AES.block_size)
    with open(file_path, 'r') as entry:
        try:
            data = entry.read()
            length = len(data)
            iv = data[:24]
            iv = b64decode(iv)
            ciphertext = data[24:length]
            ciphertext = b64decode(ciphertext)
            cipher = AES.new(key, AES.MODE_CFB, iv)
            decrypted = cipher.decrypt(ciphertext)
            decrypted = unpad(decrypted, AES.block_size)
            with open(file_path, 'wb') as data:
                data.write(decrypted)
            data.close()
            #file_path = os.path.splitext(file_path)[0]
            #print("result path: "+file_path)
        except(ValueError, KeyError):
            pass


def xor_decrypt(file_path):
    while True:
        try:
            key = int(input("Insert an integer from 0 to 255: "))
            if key < 0 or key > 255:
                raise ValueError
            break
        except ValueError:
            print("Wrong input")

    file = open(file_path, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key

    file = open(file_path, "wb")
    file.write(data)
    file.close()

