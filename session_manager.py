import json
import threading
import time
import sys
from functools import partial
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow, QDialog, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QTimer, QCoreApplication, QTime, Qt
from ficheentree import FicheWindow as FicheEntreeWindow
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication
import json
import sys
from openpyxl import Workbook
from PyQt6.QtCore import Qt


# Charger le fichier de configuration
with open('config.json') as f:
    config = json.load(f)
    
    
    
    
    
class FicheEntreeWindow(FicheEntreeWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = {}  # Initialisez self.data dans le constructeur
        self.fields = []
        
    def update_data(self):
        fields = self.findChildren(QLineEdit)
        for field in fields:
            self.data[field.objectName()] = field.text()
    
    def get_data(self):
        return self.data
    
    def save_to_excel(self, data):
        # Créer un nouveau classeur
        wb = Workbook()
        # Sélectionner la feuille active
        ws = wb.active
        # Ajouter les données dans la feuille
        for row in data:
            ws.append(row)
        # Enregistrer le classeur
        wb.save("data.xlsx")
    
    def closeEvent(self, event):
        super().closeEvent(event)
        timer_duree_session()
        timer_popup_2()
        timer_fermeture()
        self.update_data()
        print(self.fields)
        #self.save_to_excel(self.get_data())
        
        





def creation_popup(titre, texte, largeur, hauteur, police, taille_police, delai, fullscreen=False,use_timer=True):
    print(f"Appel fonction popup : {titre}, {texte}, {largeur}, {hauteur}, {police}, {taille_police}, {delai}")
    global fenetre
    fenetre = QDialog()
    fenetre.resize(largeur, hauteur)
    fenetre.setWindowTitle(titre)
    layout = QVBoxLayout(fenetre)
    
    if fullscreen:
        # Ajouter un QSpacerItem en haut pour centrer le texte
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
    
    label = QLabel(texte)
    font = QFont(police, taille_police)
    label.setFont(font)

    if fullscreen:
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    layout.addWidget(label)

    if fullscreen:
        # Ajouter un QSpacerItem en bas pour centrer le texte
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
    
    if use_timer:
        bouton = QPushButton("J'ai compris")
        bouton.clicked.connect(fenetre.close)
        layout.addWidget(bouton)
        
    fenetre.setLayout(layout)
    fenetre.show()
    if use_timer:
        QTimer.singleShot(delai * 1000, fenetre.close)
    if fullscreen:
        fenetre.showFullScreen()
    else:
        fenetre.show()
    print("Popup créée.")



def timer_duree_session():
    # Convertir la durée de la session en secondes
    duree_session = int(config['timer']['duree_session']) * 60
    print(f"Durée session : {duree_session}")
    # Créer un timer
    global timer
    timer = QTimer()
    # Connecter le signal timeout du timer à la fonction de fermeture de session
    timer.timeout.connect(end_session)
    # Démarrer le timer
    timer.start(duree_session * 1000)  # Convertir les secondes en millisecondes
    # Imprimer un message pour indiquer que le timer est actif
    print("Le timer durée session est actif.")
    timer_popup_1()


    
def timer_popup_1():
    timer_1 = int(config['timer']['timer_popup_1'])
    global timer1
    print(f"Timer popup 1 : {timer_1}")
    timer1 = QTimer(app)
    timer1.stop()  # Arrêter le timer avant de le configurer
    creation_popup_1 = partial(creation_popup, config['titre']['titre_popup_1'], config['text']['text_popup_1'], int(config['style']['largeur_popup']), int(config['style']['hauteur_popup']), config['style']['police'], int(config['style']['taille_police']), int(config['timer']['delai_fermeture']))
    timer1.timeout.connect(creation_popup_1)
    #timer1.timeout.connect(timer_popup_2)
    timer1.timeout.connect(timer1.stop)
    #timer1.start(timer_1 * 60 * 1000) # Convertir les minutes en millisecondes
    timer1.start(timer_1 * 1000) # DEBUG
    print("Le timer popup 1 est actif.")



def timer_popup_2():
    global timer_2
    timer_2 = (int(config['timer']['duree_session']) * 60) - int(config['timer']['timer_popup_2'])
    print(f"Timer popup 2 : {timer_2}")
    global timer2
    timer2 = QTimer(app)
    timer2.stop()  # Arrêter le timer avant de le configurer
    creation_popup_2 = partial(creation_popup, config['titre']['titre_popup_2'], config['text']['text_popup_2'], int(config['style']['largeur_popup']), int(config['style']['hauteur_popup']), config['style']['police'], int(config['style']['taille_police']), int(config['timer']['delai_fermeture']))
    timer2.timeout.connect(creation_popup_2)
    #timer2.timeout.connect(timer_fermeture)
    timer2.timeout.connect(timer2.stop)
    timer2.start(timer_2 * 1000) # Convertir les secondes en millisecondes
    print("Le timer popup 2 est actif.")
    
def timer_fermeture():
    timerfermeture = (int(config['timer']['duree_session']) * 60) - int(config['timer']['timer_popup_3'])
    print(f"Timer fermeture : {timerfermeture}")
    global timerfin
    timerfin = QTimer(app)
    timerfin.stop()  # Arrêter le timer avant de le configurer
    creation_fin = partial(creation_popup, config['titre']['titre_popup_3'], config['text']['text_popup_3'], int(config['style']['largeur_popup']), int(config['style']['hauteur_popup']), config['style']['police'], int(config['style']['taille_police']), int(config['timer']['delai_fermeture']), fullscreen=True, use_timer=False)
    timerfin.timeout.connect(creation_fin)
    timerfin.timeout.connect(timerfin.stop)
    timerfin.start(timerfermeture * 1000)
    
    
def end_session():
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