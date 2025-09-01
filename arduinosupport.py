import serial
import time

# Ustaw odpowiedni port COM (Windows: "COM3", Linux/Mac: "/dev/ttyUSB0")
PORT = "COM3"
BAUDRATE = 9600

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
