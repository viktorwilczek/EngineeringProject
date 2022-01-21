import os
import time

from azure.common import AzureMissingResourceHttpError
from azure.storage.blob import BlockBlobService, PublicAccess
from encrypt_decrypt.decrypt import aes_decrypt, xor_decrypt


def download_blob(block_blob_service_init, container, file_name, key):
    block_blob_service = block_blob_service_init
    # Download the blob(s).
    # Add '_DOWNLOADED' as prefix to '.txt' so you can see both files in Documents.
    download_folder = 'downloads'
    local_path = os.path.join(os.path.abspath('/Users/Viktor/PycharmProjects/EngineeringProject'), download_folder)
    local_path = os.path.join(local_path, file_name)
    #local_path = os.path.abspath(os.path.curdir)
    block_blob_service.get_blob_to_path(container, file_name, local_path)
    aes_decrypt(local_path, key)


