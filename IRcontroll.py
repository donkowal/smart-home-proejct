import serial
import time

# list of aviable codes
#To be send by IrSender.()

#Sony: (sendSony)
#    VOL up: (0x10, 0x12, 2, 12)
#    VOL down: (0x10, 0x13, 2, 12)
#    power: (0x10, 0x15, 2, 12)
#    PC: (0x10, 0x69, 2, 12)
#    TV: (0x10, 0x7D, 2, 12)
#    AUX: (0x10, 0x25, 2, 12)

#Epson: (sendNEC/ sednNEC2)
#    power: (0x5583, 0x90, <numberOfRepeats>)

#Klima: (sendNEC)
#    power: (0xE710, 0x0, <numberOfRepeats>)

# Ustaw odpowiedni port COM (Windows: "COM3", Linux/Mac: "/dev/ttyUSB0")
PORT = "COM4"
BAUDRATE = 9600

# otwieramy port
arduino = serial.Serial(PORT, BAUDRATE, timeout=1)
time.sleep(2)  # chwila na inicjalizację Arduino

print("Połączono z Arduino")

def Sound_on_off():
    arduino.write((1 + "\n").encode())  # wysyłamy numer funkcji
    print("Wywołano Sound on in IRcontroll")
    return  "Sound on/off"

def COM_close():
    arduino.close()
    print("zamknieto")
    return("COM closed")