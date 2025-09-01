from ppadb.client import Client as AdbClient
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("192.168.1.11:5555")

def on(): 
    global device
    device.shell("input keyevent 3")
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