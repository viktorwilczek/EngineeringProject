from azure.storage.blob import BlockBlobService, PublicAccess


def initialize(account_name, account_key):
    return BlockBlobService(account_name='engineeringproject',
                                              account_key='fr+DefQ1UvvZJBpYtb8kcLIfl8/ryLO2lGigl2WGbcezkESUmqDlUdG4e9MzQteT+soSaS2cIE4dr2l4kpgOBw==')