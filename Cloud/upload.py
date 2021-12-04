import os
from azure.storage.blob import BlockBlobService, PublicAccess
from EncryptDecrypt.encrypt import encrypt


def upload_blob(block_blob_service_init):
    # Create the BlockBlockService that is used to call the Blob service for the storage account
    block_blob_service = block_blob_service_init

    print('Available containers, chose one or create a new one...')
    containers = block_blob_service.list_containers()
    for c in containers:
        print('- ' + c.name)

    container = input("container: ")

    block_blob_service.create_container(container)

    # Set the permission so the blobs are public.
    block_blob_service.set_container_acl(container, public_access=PublicAccess.Container)

    # Create a file in Documents to test the uploads and download.
    upload_folder = 'uploads'
    local_path = os.path.join(os.path.abspath(os.path.curdir), upload_folder)
    local_file_name = input("Enter file name to upload : ")
    full_path_to_file = os.path.join(local_path, local_file_name)
    full_path_to_file = encrypt(full_path_to_file)

    # Upload the created file, use local_file_name for the blob name
    block_blob_service.create_blob_from_path(container, local_file_name, full_path_to_file)
    os.remove(full_path_to_file)
    print('Upload and encryption successful')

