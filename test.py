import requests
from requests.auth import HTTPDigestAuth
import time

# --- KONFIGURACJA ---
TV_IP = "192.168.1.11"  # IP Twojego TV
POSSIBLE_ENDPOINTS = [
    "http://{ip}:1925/1/input/key",
    "http://{ip}:1925/6/input/key",
    "http://{ip}:1925/input/key",
    "https://{ip}:1926/1/input/key",
    "https://{ip}:1926/6/input/key",
    "https://{ip}:1926/input/key"
]

# Wyłącz ostrzeżenia certyfikatu HTTPS
requests.packages.urllib3.disable_warnings()

# --- FUNKCJE ---
def detect_endpoint():
    """
    Wykrywa działający endpoint input/key.
    Zwraca URL i metodę auth (None lub DigestAuth).
    """
    print("Wykrywanie działającego endpointu...")
    for url in POSSIBLE_ENDPOINTS:
        try:
            if url.startswith("https"):
                r = requests.get(url.replace("input/key", "system"), verify=False, timeout=3)
            else:
                r = requests.get(url.replace("input/key", "system"), timeout=3)
            if r.status_code == 200:
                print("Znaleziono działający endpoint:", url)
                auth_required = url.startswith("https")
                return url, auth_required
        except requests.exceptions.RequestException:
            continue
    print("Nie znaleziono działającego endpointu.")
    return None, None

def pair_tv():
    """
    Proste parowanie do TV (HTTPS Digest Auth).
    Zwraca username i password.
    """
    print("Rozpoczynam parowanie TV...")
    print("Na ekranie TV pojawi się kod. Wpisz go poniżej.")
    username = input("Wprowadź username z TV: ")
    password = input("Wprowadź password z TV: ")
    return username, password

def send_key(url, key, username=None, password=None):
    payload = {"key": key}
    auth = HTTPDigestAuth(username, password) if username and password else None
    try:
        response = requests.post(url, json=payload, auth=auth, verify=False, timeout=5)
        if response.status_code == 200:
            print(f"Komenda '{key}' wysłana ✅")
        else:
            print(f"Błąd przy '{key}' ❌", response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print("Błąd połączenia:", e)

# --- GŁÓWNY PROGRAM ---
if __name__ == "__main__":
    endpoint, needs_auth = detect_endpoint()
    if not endpoint:
        exit("Nie udało się znaleźć działającego endpointu!")

    username = password = None
    if needs_auth:
        username, password = pair_tv()
        time.sleep(5)  # czas na wpisanie kodu na TV

    # Wysyłanie przykładowego klawisza
    send_key(endpoint, "Home", username, password)

    # Przykład wysyłania kilku klawiszy
    # keys = ["Home", "Standby", "VolumeUp"]
    # for k in keys:
    #     send_key(endpoint, k, username, password)
    #     time.sleep(1)
