from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode


def aes_decrypt(to_decrypt, password):
    password = password.encode('UTF-8')
    password = pad(password, AES.block_size)
    with open(to_decrypt, 'r') as content:
        try:
            file = content.read()
            length = len(file)
            init_vector = file[:24]
            init_vector = b64decode(init_vector)
            coded_text = file[24:length]
            coded_text = b64decode(coded_text)
            code = AES.new(password, AES.MODE_CFB, init_vector)
            clear = code.decrypt(coded_text)
            clear = unpad(clear, AES.block_size)
            with open(to_decrypt, 'wb') as file:
                file.write(clear)
            file.close()
        except(ValueError, KeyError):
            pass
