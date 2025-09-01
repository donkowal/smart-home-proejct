import functions as fx
import time

TV_status = 0
Sound_status = 0
Projektor_status = 0
Screen_status = 0
#PC_status


def TV():
    global TV_status
    global Sound_status
    global Projektor_status
    global Screen_status
    if TV_status == 0:
        fx.TVon_off()
        TV_status = 1
    if Sound_status == 0:
        fx.SOUND_on_off()
        Sound_status = 1
    fx.SOUND_input_TV()
    if Projektor_status == 1:
        fx.Projektor_on_off()
        Projektor_status  = 0
    if Screen_status == 1:
        fx.Screen_off()
        Screen_status = 0
    return "Tryb Kino TV aktywny"

def Projektor():
    global TV_status
    global Sound_status
    global Screen_status
    global Projektor_status
    fx.PC_on()
    if TV_status == 1:
        fx.TVon_off()
        TV_status = 0
    if Sound_status == 0:
        fx.SOUND_on_off()
        Sound_status = 1
    fx.SOUND_input_PC()
    if Screen_status == 0:
        fx.Screen_on()
        Screen_status = 1
    if Projektor_status == 0:
        fx.Projektor_on_off()
        Projektor_status = 1
    return "Tryb Kino TV aktywny"

def All_off():
    global Screen_status
    global Sound_status
    global Projektor_status
    global TV_status
    if Screen_status == 1:
        fx.Screen_off()
        Screen_status = 0
    if TV_status ==  1:
        fx.TVon_off()
        TV_status = 0
    if Sound_status == 1:
        fx.SOUND_on_off()
        Sound_status = 0
    if Projektor_status == 1:
        fx.Projektor_on_off()
        Projektor_status = 0
    return "All off"