import IRcontroll as IR
import TVcontroll as TV

#   TV controller

def TVon_off(): 
    TV.on()
    return "Wywołano funkcję 1!"

def TVvol_UP():
    x = TV.vol_UP()
    print(x)
    return "Wywołano funkcję 2!"

def TVvol_Down():
    TV.vol_Down()
    return "Wywołano funkcję 3!"

def TVnetflix():
    TV.netflix()
    return "Wywołano funkcję 4!"

#   IR controller

def SOUND_on_off():
    x = IR.Sound_on_off()
    print(x)
    return "Wywołano SOUND_on"

def SOUND_input_TV():
    return "SOUND_input_TV"

def SOUND_input_PC():
    return "SOUND_input_PC"

def SOUND_input_AUX():
    return "SOUND_input_AUX"

#   PC controller