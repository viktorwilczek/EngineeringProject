from azure.storage.blob import BlockBlobService, PublicAccess


def initialize(account_name, account_key):
    return BlockBlobService(account_name, account_key)


def list_files(container, azure_connection):
    generator = azure_connection.list_blobs(container)
    return generator


def print_containers(azure_connection):
    containers = azure_connection.list_containers()
    return containers


def delete_blob(azure_connection, container, blob_name):
    azure_connection.delete_blob(container, blob_name)


def delete_container(azure_connection, container):
    azure_connection.delete_container(container)


def create_container(azure_connection, container):
    azure_connection.create_container(container)
    azure_connection.set_container_acl(container, public_access=PublicAccess.Container)
