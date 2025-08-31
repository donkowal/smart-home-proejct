from ppadb.client import Client as AdbClient

# Połączenie z serwerem ADB
client = AdbClient(host="127.0.0.1", port=5037)

# Wskaż urządzenie (TV)
device = client.device("192.168.1.11:5555")

# Wyślij Volume Up
device.shell("input keyevent 24")



#
keys= {"Głośniej": 24, 
       "Ciszej":25,
        "Włącz": 26, 
        "Wyłącz":27, 
        "Home":3,
        "Wstecz":4,
        "Menu":1}


def send_key(key_name):
    if key_name in keys:
        device.shell(f'input keyevent {keys[key_name]}')
    else:
        print("spróbuj innego klawisza")

def wlacz_aplikacje(package):
    device.shell(f'am start -n {package}')

wlacz_aplikacje()