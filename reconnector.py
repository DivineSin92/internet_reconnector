import requests
import os
import time

#if don't know what's the network name
def internet_name():
    os.system('cmd /c "netsh wlan show networks"')

def internet_connection():
    try:
        requests.get("https://google.com")
        return True
    except requests.ConnectionError:
        return False    

if __name__ == '__main__':
    while True:
        if internet_connection():
            print("The internet is OK")
        else:
            os.system('cmd /c "netsh wlan connect name = dlink-6AED"')
        time.sleep(2)
