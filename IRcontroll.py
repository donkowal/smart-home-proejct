import serial
import time

# list of aviable codes
#To be send by IrSender.()

#Sony: (sendSony)
#2    VOL up: (0x10, 0x12, 2, 12)
#3    VOL down: (0x10, 0x13, 2, 12)
#1    power: (0x10, 0x15, 2, 12)
#4    PC: (0x10, 0x69, 2, 12)
#5    TV: (0x10, 0x7D, 2, 12)
#6    AUX: (0x10, 0x25, 2, 12)

#Epson: (sendNEC/ sednNEC2)
#7    power: (0x5583, 0x90, <numberOfRepeats>)

#Klima: (sendNEC)
#8    power: (0xE710, 0x0, <numberOfRepeats>)

#--------------------------------------------#
#   Sound controller
#--------------------------------------------#

def Sound_on_off():
    send_msg("1")
    return 0

def Sound_VOL_up():
    send_msg("2")
    return 0

def Sound_VOL_down():
    send_msg("3")
    return 0

def Sound_input_PC():
    send_msg("4")
    return 0

def Sound_input_TV():
    send_msg("5")
    return 0

def Sound_input_AUX():
    send_msg("6")
    return 0

#--------------------------------------------#
#   Projektor controller
#--------------------------------------------#

def Projektor_on_off():
    send_msg("7")
    return 0

#--------------------------------------------#
#   Klima controller
#--------------------------------------------#

def Klima_on_off():
    send_msg("8")
    return 0

#--------------------------------------------#
#   Communication system
#--------------------------------------------#

def send_msg(cmd):
    PORT = "COM4"
    BAUDRATE = 9600
    arduino = serial.Serial(PORT, BAUDRATE, timeout=1)
    print("Połączono z Arduino")
    time.sleep(1)  # chwila na inicjalizację Arduino
    arduino.write((cmd + "\n").encode())
    print("IR cmd send")
    arduino.close()
    return  "IR cmd send"
