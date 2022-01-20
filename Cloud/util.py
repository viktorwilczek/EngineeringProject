from azure.storage.blob import BlockBlobService, PublicAccess


def initialize(account_name, account_key):
    return BlockBlobService(account_name='engineeringproject',
                                              account_key='fr+DefQ1UvvZJBpYtb8kcLIfl8/ryLO2lGigl2WGbcezkESUmqDlUdG4e9MzQteT+soSaS2cIE4dr2l4kpgOBw==')
    #return BlockBlobService(account_name, account_key)


def list_files(container, block_blob_service):
    generator = block_blob_service.list_blobs(container)
    return generator


def print_containers(block_blob_service_init):
    block_blob_service = block_blob_service_init
    containers = block_blob_service.list_containers()
    return containers


def delete_blob(block_blob_service_init, container, blob_name):
    block_blob_service = block_blob_service_init
    block_blob_service.delete_blob(container, blob_name)


def delete_container(block_blob_service_init, container):
    block_blob_service = block_blob_service_init
    block_blob_service.delete_container(container)


def create_container(block_blob_service_init, container):
    block_blob_service = block_blob_service_init
    block_blob_service.create_container(container)
    block_blob_service.set_container_acl(container, public_access=PublicAccess.Container)