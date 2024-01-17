import json
import threading
import time
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtGui import QFont
from ficheentree import FicheWindow as FicheEntreeWindow

# Charger les données de configuration
with open('config.json', 'r') as f:
    config = json.load(f)

# Créer une application Qt
app = QApplication([])

# Fonction pour créer une fenêtre popup
def create_popup(title, text, width, height, font_name, font_size):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setFixedSize(width, height)
    font = QFont(font_name, font_size)
    msg.setFont(font)
    return msg

# Fonction pour fermer une fenêtre popup après un certain délai
def close_popup_after_delay(popup, delay):
    time.sleep(delay)
    popup.close()

# Ouvrir la fenêtre de ficheentree.py
window = FicheEntreeWindow()
window.showFullScreen()

# Attendre que la fenêtre soit fermée
app.exec()

# Une fois la fenêtre de ficheentree.py fermée, démarrer le compte à rebours
time.sleep(int(config['timer']['duree_session']))

# Ouvrir les fenêtres popup à des intervalles déterminés
# Liste des clés de timer
timer_keys = ['timer_popup_1', 'timer_popup_2', 'timer_popup_3']

# Ouvrir les fenêtres popup à des intervalles déterminés
for key in timer_keys:
    title = config['titre'][f'titre_popup_{i}']
    text = config['text'][f'text_popup_{i}']
    width = int(config['style']['largeur_popup'])
    height = int(config['style']['hauteur_popup'])
    font_name = config['style']['police']
    font_size = int(config['style']['taille_police'])
    msg = create_popup(title, text, width, height, font_name, font_size)
    msg.show()

    # Fermer la fenêtre popup après un certain délai
    threading.Thread(target=close_popup_after_delay, args=(msg, int(config['timer']['delai_fermeture']))).start()

    # Attendre avant d'ouvrir la prochaine fenêtre popup
    time.sleep(int(config['timer'][f'timer_{i}']))

# Fermer la session
if config['fermeture']['fermeture_session'] == 'Déconnecter':
    # Déconnecter l'utilisateur
    pass
else:
    # Verrouiller la session
    pass
