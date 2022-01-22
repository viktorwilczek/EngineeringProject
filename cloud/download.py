import os
from encrypt_decrypt.decrypt import aes_decrypt


def download_blob(block_blob_service_init, container, file_name, key):
    block_blob_service = block_blob_service_init
    download_folder = 'downloads'
    local_path = os.path.join(os.path.dirname(os.path.abspath(os.getcwd())), download_folder)
    local_path = os.path.join(local_path, file_name)
    block_blob_service.get_blob_to_path(container, file_name, local_path)
    aes_decrypt(local_path, key)


