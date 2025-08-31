import sys
print(sys.executable)
from ppadb.client import Client as AdbClient

client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("192.168.1.11:5555")

print("Połączono z:", device.serial)

device.shell("input keyevent 26")  
