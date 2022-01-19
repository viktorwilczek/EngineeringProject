from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode
import time


def aes_encrypt(file_path, key):

    key = key.encode('UTF-8')
    key = pad(key, AES.block_size)
    start = time.time()
    print("timer started")

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
    end = time.time()
    print('time finish: ' + str(end - start))
    print(file_path + '.enc')
    return file_path + '.enc'


def xor_encrypt(file_path):
    while True:
        try:
            key = int(input("Insert an integer from 0 to 255: "))
            if key < 0 or key > 255:
                raise ValueError
            break
        except ValueError:
            print("Wrong input")
    start = time.time()
    print("timer started")
    file = open(file_path, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
    end = time.time()
    print('time finish: '+str(end - start))

    with open(file_path + '.enc', "wb") as file:
        file.write(data)
    file.close()
    return file_path + '.enc'
