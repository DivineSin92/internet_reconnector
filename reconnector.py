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
            #os.system('cmd /c "ping www.google.com"')
            pass
        else:
            os.system('cmd /c "netsh wlan disconnect"')
            os.system('cmd /c "netsh wlan connect name = "') #add name of network
        time.sleep(1)
