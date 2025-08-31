
from ppadb.client import Client as AdbClient
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("192.168.1.11:5555")

def func1():
    global device
    device.shell("input keyevent 3")
    return "Wywołano funkcję 1!"

def func2():
    global device
    device.shell("input keyevent 24")
    return "Wywołano funkcję 2!"

def func3():
    global device
    device.shell("input keyevent 25")
    return "Wywołano funkcję 3!"

def func4():
    return "Wywołano funkcję 4!"
