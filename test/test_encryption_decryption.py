import os
import unittest
import filecmp
from encrypt_decrypt import decrypt, encrypt
from shutil import copyfile


def clean_up_files(file_path_to_enc, file_path_not_to_enc):
    os.remove(file_path_to_enc + ".enc")
    os.remove(file_path_not_to_enc)


def prepare_file(file_name):
    current_path = os.path.abspath(os.path.curdir)
    test_file_location = os.path.join(current_path, "test_files")
    file_path_to_enc = os.path.join(test_file_location, file_name)
    file_path_not_to_enc = file_path_to_enc+".copy"
    copyfile(file_path_to_enc, file_path_not_to_enc)
    return file_path_to_enc, file_path_not_to_enc


class TestEncryptionDecryption(unittest.TestCase):

    def check_encryption_decryption(self, file_name, assert_type, pass_one, pass_two):
        file_path_to_enc, file_path_not_to_enc = prepare_file(file_name)
        encrypt.aes_encrypt(file_path_to_enc, pass_one)
        decrypt.aes_decrypt(file_path_to_enc + ".enc", pass_two)
        if assert_type:
            self.assertTrue(filecmp.cmp(file_path_to_enc + ".enc", file_path_not_to_enc))
        else:
            self.assertFalse(filecmp.cmp(file_path_to_enc + ".enc", file_path_not_to_enc))
        clean_up_files(file_path_to_enc, file_path_not_to_enc)

    def test_enc_dec(self):
        self.check_encryption_decryption("test1.png", True, "password", "password")
        self.check_encryption_decryption("test1.png", False, "password", "not_password")
        self.check_encryption_decryption("11_Pentium_Pro.pdf", True, "password", "password")
        self.check_encryption_decryption("11_Pentium_Pro.pdf", False, "password", "not_password")


if __name__ == '__main__':
    unittest.main()
