import os
import time

from azure.common import AzureMissingResourceHttpError
from azure.storage.blob import BlockBlobService, PublicAccess
from EncryptDecrypt.decrypt import aes_decrypt, xor_decrypt


def download_blob(block_blob_service_init):
    block_blob_service = block_blob_service_init
    while True:
        try:
            print('Available containers, chose one...')
            containers = block_blob_service.list_containers()
            for c in containers:
                print('- ' + c.name)
            container = input("container: ")

            # List the blobs in the container
            print("Blobs in the container...")
            generator = block_blob_service.list_blobs(container)
            for blob in generator:
                print('- ' + blob.name)
            break
        except AzureMissingResourceHttpError:
            print(container + ' does not exist')
            time.sleep(1)

    # Download the blob(s).
    # Add '_DOWNLOADED' as prefix to '.txt' so you can see both files in Documents.
    download_folder = 'downloads'
    local_path = os.path.join(os.path.abspath(os.path.curdir), download_folder)
    while True:
        try:
            file_name = input("Enter file name to download : ")
            local_path = os.path.join(local_path, file_name)
            block_blob_service.get_blob_to_path(container, file_name, local_path)
            time.sleep(1)
            break
        except AzureMissingResourceHttpError:
            print(file_name + ' does not exist')

    while True:
        try:
            mode = int(input('Select encryption: 1 - AES, 2 - XOR: '))
            if mode < 0 or mode > 3:
                raise ValueError
            break
        except ValueError:
            print("Wrong input")

    if mode == 1:
        aes_decrypt(local_path)
    else:
        xor_decrypt(local_path)

