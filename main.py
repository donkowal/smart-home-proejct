import requests
import json


# Adres API telewizora (zmień na właściwy)
url = "http://192.168.1.11:1925/1/input/key"

# Wczytanie pliku JSON
with open("dane.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Nagłówki HTTP (często wymagane przez API)
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
    # "Authorization": "Bearer TWÓJ_TOKEN"   # jeśli API wymaga autoryzacji
}

# Wysyłanie żądania POST
response = requests.post(url, headers=headers, json=data)

# Sprawdzenie odpowiedzi
if response.status_code == 200:
    print("Plik JSON wysłany poprawnie!")
    print("Odpowiedź telewizora:", response.json())
else:
    print("Błąd podczas wysyłania:", response.status_code, response.text)
