import sys
from azure.storage.blob import BlockBlobService, PublicAccess
from Cloud.upload import upload_blob
from Cloud.download import download_blob


def initialize():
    # account_name = input("Insert your azure account name: ")
    # account_key = input("Insert your azure account key: ")
    # return BlockBlobService(account_name, account_key)
    return BlockBlobService(account_name='engineeringproject',
                                              account_key='fr+DefQ1UvvZJBpYtb8kcLIfl8/ryLO2lGigl2WGbcezkESUmqDlUdG4e9MzQteT+soSaS2cIE4dr2l4kpgOBw==')


# Main method.
if __name__ == '__main__':

    block_blob_service_init = initialize()

    while True:
        sys.stdout.write("1 - upload, 2 - download, 3 - setup, 4 - exit\n")
        while True:
            try:
                option = int(input('Enter your choice: '))
                if option < 1 or option > 4:
                    raise ValueError
                break
            except ValueError:
                print("Wrong input")

        if option == 1:
            print('Upload selected...')
            upload_blob(block_blob_service_init)
        elif option == 2:
            print('Download selected...')
            download_blob(block_blob_service_init)
        elif option == 3:
            print('Setup selected...')
            block_blob_service = initialize()
        elif option == 4:
            print('Exit selected...')
            for name in dir():
                if not name.startswith('_'):
                    del globals()[name]
            for name in dir():
                if not name.startswith('_'):
                    del locals()[name]
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
