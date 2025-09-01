import functions as fx
import time

TV_status = 0
Sound_status = 0
Projektor_status = 0
Screen_status = 0


def TV(): 
    fx.TVon_off
    time.sleep(5)
    fx.SOUND_on_off
    time.sleep(5)
    fx.SOUND_input_TV
    return "Wywołano funkcję 1!"

def All_off():
    global Screen_status
    if Screen_status == 1:
        Screen_status = 0


    return "All off"