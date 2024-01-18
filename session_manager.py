import json
import threading
import time
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QDialog, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer, QCoreApplication, QTime
from ficheentree import FicheWindow as FicheEntreeWindow


# Charger le fichier de configuration
with open('config.json') as f:
    config = json.load(f)
    
    
class FicheEntreeWindow(FicheEntreeWindow):
    def closeEvent(self, event):
        timer_duree_session()
        timer_popup_1()
        super().closeEvent(event)



def creation_popup(titre, texte, largeur, hauteur, police, taille_police, delai):
    global fenetre
    fenetre = QDialog()
    fenetre.resize(largeur, hauteur)
    fenetre.setWindowTitle(titre)
    layout = QVBoxLayout(fenetre)
    label = QLabel(texte)
    font = QFont(police, taille_police)
    label.setFont(font)
    layout.addWidget(label)
    bouton = QPushButton("J'ai compris")
    bouton.clicked.connect(fenetre.close)
    layout.addWidget(bouton)
    fenetre.setLayout(layout)
    fenetre.show()
    QTimer.singleShot(delai * 1000, fenetre.close)
    print("Popup créée.")


def timer_duree_session():
    # Convertir la durée de la session en minutes
    duree_session = int(config['timer']['duree_session'])
    # Créer un timer
    global timer
    timer = QTimer()
    # Connecter le signal timeout du timer à la fonction de fermeture de session
    timer.timeout.connect(end_session)
    # Démarrer le timer
    timer.start(duree_session * 60 * 1000)  # Convertir les minutes en millisecondes
    # Imprimer un message pour indiquer que le timer est actif
    print("Le timer durée session est actif.")



def timer_popup_1():
    timer_1 = int(config['timer']['timer_popup_1'])
    global timer1 
    timer1 = QTimer(app)
    timer1.timeout.connect(lambda: creation_popup(config['titre']['titre_popup_1'], config['text']['text_popup_1'], int(config['style']['largeur_popup']), int(config['style']['hauteur_popup']), config['style']['police'], int(config['style']['taille_police']), int(config['timer']['delai_fermeture'])))
    timer1.start(timer_1 * 60 * 1000)
    print("Le timer popup 1 est actif.")



def end_session():
    timer.stop()
    timer1.stop()
    # Fermer la session en fonction de la valeur de session_fermeture
    if config['fermeture']['fermeture_session'] == 'Déconnecter':
        # Déconnecter l'utilisateur
        print("Fin de session. Déconnexion.")
    else:
        # Verrouiller la session
        print("Fin de session. Verrouillage.")
        
    app.quit() # Terminer l'application Qt



# Créer une application Qt
app = QApplication(sys.argv)

# Ne pas quitter l'application lorsque la dernière fenêtre est fermée
app.setQuitOnLastWindowClosed(False)

# Créer et afficher la fenêtre FicheEntreeWindow
window = FicheEntreeWindow()
window.showFullScreen()

# Démarrer la boucle d'événements
sys.exit(app.exec())