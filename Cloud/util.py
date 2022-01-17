from azure.storage.blob import BlockBlobService, PublicAccess


def initialize(account_name, account_key):
    return BlockBlobService(account_name, account_key);