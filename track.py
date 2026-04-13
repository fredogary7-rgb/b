import requests
import json
import time
import subprocess

# --- CONFIGURATION ---
SERVER_URL = "https://nova-trade.cc/api/track"
DEVICE_ID = "Phone_02_Pro"
INTERVAL = 300  # 5 minutes entre chaque envoi

def get_gps_location():
    """Récupère la position réelle via l'API Termux"""
    try:
        # Exécute la commande système termux-location
        result = subprocess.check_output(["termux-location"], stderr=subprocess.STDOUT)
        data = json.loads(result)
        return data.get('latitude'), data.get('longitude')
    except Exception as e:
        print(f"Erreur GPS : {e}")
        # En cas d'erreur (GPS désactivé), on envoie une valeur par défaut
        return 0.0, 0.0

def start_tracking():
    print(f"🚀 Démarrage du tracking pour {DEVICE_ID}...")
    
    while True:
        lat, lon = get_gps_location()
        
        payload = {
            "device_id": DEVICE_ID,
            "lat": lat,
            "lon": lon,
            "status": "online",
            "battery": "checked"
        }

        try:
            response = requests.post(SERVER_URL, json=payload, timeout=10)
            if response.status_code == 200:
                print(f"✅ [{time.strftime('%H:%M:%S')}] Position envoyée : {lat}, {lon}")
            else:
                print(f"⚠️ Erreur serveur : {response.status_code}")
        except Exception as e:
            print(f"❌ Erreur de connexion : {e}")

        time.sleep(INTERVAL)

if __name__ == "__main__":
    start_tracking()

