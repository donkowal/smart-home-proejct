from ppadb.client import Client as AdbClient
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("192.168.1.11:5555")

#Funkcja	Keyevent
#HOME	        3
#BACK	        4
#MENU	        82
#VOLUME UP	    24
#VOLUME DOWN	25
#MUTE	        164
#POWER	        26
#DPAD_UP	    19
#DPAD_DOWN	    20
#PAD_LEFT	    21
#DPAD_RIGHT	    22
#DPAD_CENTER	23

def on(): 
    global device
    device.shell("input keyevent 26")
    return "Wywołano funkcję 1!"

def vol_UP():
    global device
    device.shell("input keyevent 24")
    return "Wywołano funkcję 2!"

def vol_Down():
    global device
    device.shell("input keyevent 25")
    return "Wywołano funkcję 3!"

def netflix():
    return "Wywołano funkcję 4!"