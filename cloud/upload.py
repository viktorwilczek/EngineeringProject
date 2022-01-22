import os
from pathlib import Path
from encrypt_decrypt.encrypt import aes_encrypt


def upload_blob(block_blob_service_init, container, full_path_to_file, key):
    block_blob_service = block_blob_service_init
    full_path_to_file = aes_encrypt(full_path_to_file, key)
    file_name = Path(full_path_to_file).name
    file_name = os.path.splitext(file_name)[0]
    block_blob_service.create_blob_from_path(container, file_name, full_path_to_file)
    os.remove(full_path_to_file)
