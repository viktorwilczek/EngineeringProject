import os
import unittest
import filecmp
from encrypt_decrypt import decrypt, encrypt
from cloud.util import initialize
from shutil import copyfile
import warnings


def clean_up_files(file_path_to_enc, file_path_not_to_enc):
    os.remove(file_path_to_enc + ".enc")
    os.remove(file_path_not_to_enc)


def prepare_copy(file_name):
    current_path = os.path.abspath(os.path.curdir)
    test_file_location = os.path.join(current_path, "test_files")
    file_path_to_enc = os.path.join(test_file_location, file_name)
    file_path_not_to_enc = file_path_to_enc+".copy"
    copyfile(file_path_to_enc, file_path_not_to_enc)
    return file_path_to_enc, file_path_not_to_enc


class TestEncryptionDecryption(unittest.TestCase):

    def check_encryption_decryption(self, file_name, assert_type, pass_one, pass_two):
        file_path_to_enc, file_path_not_to_enc = prepare_copy(file_name)
        encrypt.aes_encrypt(file_path_to_enc, pass_one)
        decrypt.aes_decrypt(file_path_to_enc + ".enc", pass_two)
        if assert_type:
            self.assertTrue(filecmp.cmp(file_path_to_enc + ".enc", file_path_not_to_enc))
        else:
            self.assertFalse(filecmp.cmp(file_path_to_enc + ".enc", file_path_not_to_enc))
        clean_up_files(file_path_to_enc, file_path_not_to_enc)

    def test_encryption_decryption(self):
        self.check_encryption_decryption("test1.png", True, "password", "password")
        self.check_encryption_decryption("test1.png", False, "password", "not_password")

        self.check_encryption_decryption("test2.pdf", True, "password", "password")
        self.check_encryption_decryption("test2.pdf", False, "password", "not_password")

        self.check_encryption_decryption("test3.json", True, "password", "password")
        self.check_encryption_decryption("test3.json", False, "password", "not_password")

        self.check_encryption_decryption("test4.sol", True, "password", "password")
        self.check_encryption_decryption("test4.sol", False, "password", "not_password")

        self.check_encryption_decryption("test6.mp3", True, "password", "password")
        self.check_encryption_decryption("test6.mp3", False, "password", "not_password")

        self.check_encryption_decryption("test7.wav", True, "password", "password")
        self.check_encryption_decryption("test7.wav", False, "password", "not_password")

        self.check_encryption_decryption("test8.ogg", True, "password", "password")
        self.check_encryption_decryption("test8.ogg", False, "password", "not_password")

        self.check_encryption_decryption("test9.avi", True, "password", "password")
        self.check_encryption_decryption("test9.avi", False, "password", "not_password")

        self.check_encryption_decryption("test10.mov", True, "password", "password")
        self.check_encryption_decryption("test10.mov", False, "password", "not_password")

        self.check_encryption_decryption("test11.mp4", True, "password", "password")
        self.check_encryption_decryption("test11.mp4", False, "password", "not_password")

        self.check_encryption_decryption("test12.wmv", True, "password", "password")
        self.check_encryption_decryption("test12.wmv", False, "password", "not_password")

        self.check_encryption_decryption("test13.doc", True, "password", "password")
        self.check_encryption_decryption("test13.doc", False, "password", "not_password")

        self.check_encryption_decryption("test14.xls", True, "password", "password")
        self.check_encryption_decryption("test14.xls", False, "password", "not_password")

        self.check_encryption_decryption("test15.ppt", True, "password", "password")
        self.check_encryption_decryption("test15.ppt", False, "password", "not_password")

        self.check_encryption_decryption("test16.odt", True, "password", "password")
        self.check_encryption_decryption("test16.odt", False, "password", "not_password")

        self.check_encryption_decryption("test17.ods", True, "password", "password")
        self.check_encryption_decryption("test17.ods", False, "password", "not_password")

        self.check_encryption_decryption("test18.odp", True, "password", "password")
        self.check_encryption_decryption("test18.odp", False, "password", "not_password")

        self.check_encryption_decryption("test19.rtf", True, "password", "password")
        self.check_encryption_decryption("test19.rtf", False, "password", "not_password")

        self.check_encryption_decryption("test20.webp", True, "password", "password")
        self.check_encryption_decryption("test20.webp", False, "password", "not_password")

        self.check_encryption_decryption("test21.gif", True, "password", "password")
        self.check_encryption_decryption("test21.gif", False, "password", "not_password")

        self.check_encryption_decryption("test23.html", True, "password", "password")
        self.check_encryption_decryption("test23.html", False, "password", "not_password")

        self.check_encryption_decryption("test24.csv", True, "password", "password")
        self.check_encryption_decryption("test24.csv", False, "password", "not_password")

        self.check_encryption_decryption("test25.zip", True, "password", "password")
        self.check_encryption_decryption("test25.zip", False, "password", "not_password")

        self.check_encryption_decryption("test26.swift", True, "password", "password")
        self.check_encryption_decryption("test26.swift", False, "password", "not_password")

        self.check_encryption_decryption("test27.plist", True, "password", "password")
        self.check_encryption_decryption("test27.plist", False, "password", "not_password")

        self.check_encryption_decryption("test28.djvu", True, "password", "password")
        self.check_encryption_decryption("test28.djvu", False, "password", "not_password")

        self.check_encryption_decryption("test29.ott", True, "password", "password")
        self.check_encryption_decryption("test29.ott", False, "password", "not_password")

        self.check_encryption_decryption("test30.xlsx", True, "password", "password")
        self.check_encryption_decryption("test30.xlsx", False, "password", "not_password")

        self.check_encryption_decryption("test31.lrf", True, "password", "password")
        self.check_encryption_decryption("test31.lrf", False, "password", "not_password")

        self.check_encryption_decryption("test32.fb2", True, "password", "password")
        self.check_encryption_decryption("test32.fb2", False, "password", "not_password")

        self.check_encryption_decryption("test9.avi", True, "password", "password")
        self.check_encryption_decryption("test9.avi", False, "password", "not_password")

        self.check_encryption_decryption("test33.epub", True, "password", "password")
        self.check_encryption_decryption("test33.epub", False, "password", "not_password")

        self.check_encryption_decryption("test34.azw3", True, "password", "password")
        self.check_encryption_decryption("test34.azw3", False, "password", "not_password")

        self.check_encryption_decryption("test12.wmv", True, "password", "password")
        self.check_encryption_decryption("test12.wmv", False, "password", "not_password")

        self.check_encryption_decryption("test35.erf", True, "password", "password")
        self.check_encryption_decryption("test35.erf", False, "password", "not_password")

        self.check_encryption_decryption("test36.hdr", True, "password", "password")
        self.check_encryption_decryption("test36.hdr", False, "password", "not_password")

        self.check_encryption_decryption("test37.nef", True, "password", "password")
        self.check_encryption_decryption("test37.nef", False, "password", "not_password")

        self.check_encryption_decryption("test38.vob", True, "password", "password")
        self.check_encryption_decryption("test38.vob", False, "password", "not_password")

        self.check_encryption_decryption("test39.rm", True, "password", "password")
        self.check_encryption_decryption("test39.rm", False, "password", "not_password")

        self.check_encryption_decryption("test40.8svx", True, "password", "password")
        self.check_encryption_decryption("test40.8svx", False, "password", "not_password")

    def check_upload_download(self, file_name, azure_connection):
        file_path_to_upload, file_path_copy = prepare_copy(file_name)
        azure_connection.create_blob_from_path("testing", file_name, file_path_to_upload)
        azure_connection.get_blob_to_path("testing", file_name, file_path_copy)
        self.assertTrue(filecmp.cmp(file_path_to_upload, file_path_copy))
        os.remove(file_path_copy)

    def test_upload_download(self):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        azure_connection = initialize('engineeringproject', 'fr+DefQ1UvvZJBpYtb8kcLIfl8'
                                                                   '/ryLO2lGigl2WGbcezkESUmqDlUdG4e9MzQteT'
                                                                   '+soSaS2cIE4dr2l4kpgOBw==')
        self.check_upload_download("test1.png", azure_connection)
        self.check_upload_download("test2.pdf", azure_connection)
        self.check_upload_download("test3.json", azure_connection)
        self.check_upload_download("test4.sol", azure_connection)
        self.check_upload_download("test5.jpg", azure_connection)
        self.check_upload_download("test6.mp3", azure_connection)
        self.check_upload_download("test7.wav", azure_connection)
        self.check_upload_download("test8.ogg", azure_connection)
        self.check_upload_download("test9.avi", azure_connection)
        self.check_upload_download("test10.mov", azure_connection)
        self.check_upload_download("test11.mp4", azure_connection)
        self.check_upload_download("test12.wmv", azure_connection)
        self.check_upload_download("test13.doc", azure_connection)
        self.check_upload_download("test14.xls", azure_connection)
        self.check_upload_download("test15.ppt", azure_connection)
        self.check_upload_download("test16.odt", azure_connection)
        self.check_upload_download("test17.ods", azure_connection)
        self.check_upload_download("test18.odp", azure_connection)
        self.check_upload_download("test19.rtf", azure_connection)
        self.check_upload_download("test20.webp", azure_connection)
        self.check_upload_download("test21.gif", azure_connection)
        self.check_upload_download("test22.ico", azure_connection)
        self.check_upload_download("test23.html", azure_connection)
        self.check_upload_download("test24.csv", azure_connection)
        self.check_upload_download("test25.zip", azure_connection)
        self.check_upload_download("test26.swift", azure_connection)
        self.check_upload_download("test27.plist", azure_connection)
        self.check_upload_download("test28.djvu", azure_connection)
        self.check_upload_download("test29.ott", azure_connection)
        self.check_upload_download("test30.xlsx", azure_connection)
        self.check_upload_download("test31.lrf", azure_connection)
        self.check_upload_download("test32.fb2", azure_connection)
        self.check_upload_download("test33.epub", azure_connection)
        self.check_upload_download("test34.azw3", azure_connection)
        self.check_upload_download("test35.erf", azure_connection)
        self.check_upload_download("test36.hdr", azure_connection)
        self.check_upload_download("test37.nef", azure_connection)
        self.check_upload_download("test38.vob", azure_connection)
        self.check_upload_download("test39.rm", azure_connection)
        self.check_upload_download("test40.8svx", azure_connection)


if __name__ == '__main__':
    unittest.main()
