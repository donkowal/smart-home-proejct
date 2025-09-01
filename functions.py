import IRcontroll as IR
import TVcontroll as TV


from ppadb.client import Client as AdbClient
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("192.168.1.11:5555")

#   TV controller

def TVon_off(): 
    TV.on
    return "Wywołano funkcję 1!"

def TVvol_UP():
    TV.vol_UP
    return "Wywołano funkcję 2!"

def TVvol_Down():
    TV.vol_Down
    return "Wywołano funkcję 3!"

def TVnetflix():
    TV.netflix
    return "Wywołano funkcję 4!"

#   IR controller

def SOUND_on_off():
    return "Wywołano SOUND_on"

def SOUND_input_TV():
    return "SOUND_input_TV"

def SOUND_input_PC():
    return "SOUND_input_PC"

def SOUND_input_AUX():
    return "SOUND_input_AUX"

#   PC controller