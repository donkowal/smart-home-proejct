from ppadb.client import Client as AdbClient

# Połączenie z serwerem ADB
client = AdbClient(host="127.0.0.1", port=5037)

# Wskaż urządzenie (TV)
device = client.device("192.168.1.11:5555")

# Wyślij przycisk HOME
device.shell("input keyevent 3")

# Wyślij Volume Up
device.shell("input keyevent 24")