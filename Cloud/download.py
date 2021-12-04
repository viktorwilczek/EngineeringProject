import os
from azure.storage.blob import BlockBlobService, PublicAccess
from EncryptDecrypt.decrypt import decrypt


def download_blob(block_blob_service_init):
    block_blob_service = block_blob_service_init

    print('Available containers, chose one...')
    containers = block_blob_service.list_containers()
    for c in containers:
        print('- '+c.name)

    container = input("container: ")

    # List the blobs in the container
    print("Blobs in the container...")
    generator = block_blob_service.list_blobs(container)
    for blob in generator:
        print('- '+blob.name)

    # Download the blob(s).
    # Add '_DOWNLOADED' as prefix to '.txt' so you can see both files in Documents.
    download_folder = 'downloads'
    local_path = os.path.join(os.path.abspath(os.path.curdir), download_folder)
    file_name = input("Enter file name to download : ")
    #full_path_to_file2 = os.path.join(local_path, str.replace(local_file_name, '.txt', '_DOWNLOADED.txt'))
    local_path = os.path.join(local_path, file_name)
    block_blob_service.get_blob_to_path(container, file_name, local_path)
    decrypt(local_path)

