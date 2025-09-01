import IRcontroll as IR
import TVcontroll as TV
#--------------------------------------------#
#   TV controller
#--------------------------------------------#
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

#--------------------------------------------#
#   IR controller
#--------------------------------------------#

def SOUND_on_off():
    IR.Sound_on_off()
    return "Sound_on_off"

def SOUND_input_TV():
    IR.Sound_input_TV()
    return "SOUND_input_TV"

def SOUND_input_PC():
    IR.Sound_input_PC()
    return "SOUND_input_PC"

def SOUND_input_AUX():
    IR.Sound_input_AUX()
    return "SOUND_input_AUX"

def SOUND_vol_up():
    IR.Sound_VOL_up()
    return "Sound_VOL_up"

def Projektor_on_off():
    IR.Projektor_on_off()
    return "Projektor_on_off"

def Klima_on_off():
    IR.Klima_on_off()
    return "Klima on off"

#--------------------------------------------#
#   PC controller
#--------------------------------------------#

def PC_on():
    return  "PC  turned  on"

#--------------------------------------------#
#   Analog controller
#--------------------------------------------#

def Screen_on():
    return "Screen turned on"

def Screen_off():
    return "Screen turned off"