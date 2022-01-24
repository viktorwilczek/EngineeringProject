import os
from encrypt_decrypt.decrypt import aes_decrypt


def download_blob(azure_connection, container, file_name, key):
    download_folder = 'downloads'
    local_path = os.path.join(os.path.dirname(os.path.abspath(os.getcwd())), download_folder)
    local_path = os.path.join(local_path, file_name)
    azure_connection.get_blob_to_path(container, file_name, local_path)
    aes_decrypt(local_path, key)


