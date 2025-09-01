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
PORT = "COM3"
BAUDRATE = 9600

def Sound_on_off():
    return  "Sound on/off"

def main():
    try:
        # otwieramy port
        arduino = serial.Serial(PORT, BAUDRATE, timeout=1)
        time.sleep(2)  # chwila na inicjalizację Arduino

        print("Połączono z Arduino. Wpisz numer funkcji (1-10), lub 'q' aby zakończyć.")

        while True:
            cmd = input("Komenda: ")
            if cmd.lower() == "q":
                print("Zamykanie...")
                break
            if cmd.isdigit() and 1 <= int(cmd) <= 10:
                arduino.write((cmd + "\n").encode())  # wysyłamy numer funkcji
                print(f"Wysłano komendę: {cmd}")
            else:
                print("Podaj liczbę od 1 do 10 lub 'q'.")

        arduino.close()

    except serial.SerialException as e:
        print(f"Błąd portu szeregowego: {e}")

if __name__ == "__main__":
    main()
