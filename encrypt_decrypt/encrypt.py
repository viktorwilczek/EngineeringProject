from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode
import time


def aes_encrypt(to_encrypt, password):
    password = password.encode('UTF-8')
    password = pad(password, AES.block_size)
    with open(to_encrypt, 'rb') as content:
        file = content.read()
        code = AES.new(password, AES.MODE_CFB)
        coded_text = code.encrypt(pad(file, AES.block_size))
        init_vector = b64encode(code.iv).decode('UTF-8')
        coded_text = b64encode(coded_text).decode('UTF-8')
        encoded = init_vector + coded_text
    content.close()

    with open(to_encrypt + '.enc', 'w') as file:
        file.write(encoded)
    file.close()
    return to_encrypt + '.enc'
