import os
import uuid
import sys
from azure.storage.blob import BlockBlobService, PublicAccess

from Cloud.upload import upload_blob
from Cloud.download import download_blob
from EncryptDecrypt import decrypt, encrypt


# TODO
#  


def initialize():
    # account_name = input("Insert your azure account name: ")
    # account_key = input("Insert your azure account key: ")
    # return BlockBlobService(account_name, account_key)
    return BlockBlobService(account_name='engineeringproject',
                                              account_key='fr+DefQ1UvvZJBpYtb8kcLIfl8/ryLO2lGigl2WGbcezkESUmqDlUdG4e9MzQteT+soSaS2cIE4dr2l4kpgOBw==')


# def upload(block_blob_service_init):
#     # Create the BlockBlockService that is used to call the Blob service for the storage account
#     block_blob_service = block_blob_service_init
#
#     print('Available containers, chose one or create a new one...')
#     containers = block_blob_service.list_containers()
#     for c in containers:
#         print('- ' + c.name)
#
#     container = input("container: ")
#
#     block_blob_service.create_container(container)
#
#     # Set the permission so the blobs are public.
#     block_blob_service.set_container_acl(container, public_access=PublicAccess.Container)
#
#     # Create a file in Documents to test the uploads and download.
#     local_path = os.path.abspath(os.path.curdir)
#     local_file_name = input("Enter file name to uploads : ")
#     full_path_to_file = os.path.join(local_path, local_file_name)
#
#     print("Temp file = " + full_path_to_file)
#     print("\nUploading to Blob storage as blob" + local_file_name)
#
#     # Upload the created file, use local_file_name for the blob name
#     block_blob_service.create_blob_from_path(container, local_file_name, full_path_to_file)


# def download(block_blob_service_init):
#     block_blob_service = block_blob_service_init
#
#     print('Available containers, chose one...')
#     containers = block_blob_service.list_containers()
#     for c in containers:
#         print('- '+c.name)
#
#     container = input("container: ")
#
#     # List the blobs in the container
#     print("Blobs in the container...")
#     generator = block_blob_service.list_blobs(container)
#     for blob in generator:
#         print('- '+blob.name)
#
#     # Download the blob(s).
#     # Add '_DOWNLOADED' as prefix to '.txt' so you can see both files in Documents.
#     local_path = os.path.abspath(os.path.curdir)
#     local_file_name = input("Enter file name to download : ")
#     full_path_to_file2 = os.path.join(local_path, str.replace(local_file_name, '.txt', '_DOWNLOADED.txt'))
#     print("\nDownloading blob to " + full_path_to_file2)
#     block_blob_service.get_blob_to_path(container, local_file_name, full_path_to_file2)


def list_blobs():
    return 4


# Main method.
if __name__ == '__main__':

    global block_blob_service
    menu_options = {
        1: '1 - uploads ',
        2: '2 - download',
        3: '3 - setup',
        4: '4 - exit',
    }

    block_blob_service_init = initialize()

    while True:
        sys.stdout.write("1 - upload, 2 - download, 3 - setup, 4 - exit\n")
        option = int(input('Enter your choice: '))
        if option == 1:
            print('Upload selected...')
            upload_blob(block_blob_service_init)
        elif option == 2:
            print('Download selected...')
            download_blob(block_blob_service_init)
        elif option == 3:
            print('Setup selected...')
            block_blob_service = initialize()
        elif option == 4:
            print('Exit selected...')
            for name in dir():
                if not name.startswith('_'):
                    del globals()[name]
            for name in dir():
                if not name.startswith('_'):
                    del locals()[name]
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')


