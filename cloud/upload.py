import os
from azure.storage.blob import BlockBlobService, PublicAccess
from pathlib import Path
from encrypt_decrypt.encrypt import aes_encrypt, xor_encrypt


def upload_blob(block_blob_service_init, container, full_path_to_file, key):
    # Create the BlockBlockService that is used to call the Blob service for the storage account
    block_blob_service = block_blob_service_init
    full_path_to_file = aes_encrypt(full_path_to_file, key)
    # Upload the created file, use local_file_name for the blob name
    file_name = Path(full_path_to_file).name
    file_name = os.path.splitext(file_name)[0]
    print(file_name)
    block_blob_service.create_blob_from_path(container, file_name, full_path_to_file)
    os.remove(full_path_to_file)
    print('Upload and encryption successful')
    # full_path_to_file = xor_encrypt(full_path_to_file)
