import json
import sys
import os
import pandas as pd
import zipfile
import openpyxl
from functools import partial
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, QComboBox, QMessageBox, QColorDialog
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import QTimer, Qt
from ficheentree import FicheWindow as FicheEntreeWindow
from PyQt6.QtWidgets import QApplication
from openpyxl import Workbook
from datetime import datetime
from zipfile import BadZipFile
from openpyxl import load_workbook

# Créer une application Qt
app = QApplication(sys.argv)

class test(QDialog):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    # Fonction pour créer le popup d'après le fichier de configuration
    def creation_popup(self, titre, texte, largeur, hauteur, police, taille_police, delai, fullscreen=False, use_timer=True):
        #print(f"Appel fonction popup : {titre}, {texte}, {largeur}, {hauteur}, {police}, {taille_police}, {delai}") # Pour débugger
        global fenetre
        fenetre = QDialog()
        fenetre.setFixedSize(int(largeur), int(hauteur))
        fenetre.setWindowTitle(titre)
        fenetre.setStyleSheet("background-color: #5f5f5f;")
        fenetre.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        fenetre.setWindowFlags(fenetre.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
        layout = QVBoxLayout(fenetre)

        # Créer un nouveau layout pour le label
        layout_texte = QVBoxLayout()
        layout_texte.setContentsMargins(20, 0, 20, 0)  # Appliquer une marge de 10 pixels

        if fullscreen:
            # Ajouter un QSpacerItem en haut pour centrer le texte
            layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        label = QLabel(texte)
        label.setWordWrap(True)
        label.setStyleSheet("color : #f2f2f2;")
        font = QFont(police, taille_police)
        label.setFont(font)

        # Ajouter le label au layout_texte au lieu du layout principal
        layout_texte.addWidget(label)

        if fullscreen:
            fenetre.setStyleSheet("background-color: white;")
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Ajouter le layout_texte au layout principal
        layout.addLayout(layout_texte)

        if fullscreen:
            # Ajouter un QSpacerItem en bas pour centrer le texte
            layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        if use_timer:
            bouton = QPushButton("J'ai compris")
            bouton.setFont(font)  # Utiliser la même police que le label
            bouton.setStyleSheet(f"font-size: {taille_police}px;")  # Définir la taille de la police
            bouton.setStyleSheet("""
            QPushButton:enabled {
                background: linear-gradient(to bottom, #7892c2 5%, #476e9e 100%);
                background-color: #5472bd;
                border-radius: 4px;
                border: 1px solid #4e6096;
                color: #ffffff;
                font-family: Arial;
                font-size: 15px;
                font-weight: bold;
                padding: 9px 50px;
                text-decoration: none;
            }
            QPushButton:hover {
                background: linear-gradient(to bottom, #476e9e 5%, #7892c2 100%);
                background-color: #476e9e;
            }
            QPushButton:pressed {
                position: relative;
                top: 1px;
            }
            """)

            bouton.clicked.connect(fenetre.close)
            layout.addWidget(bouton)
        fenetre.setLayout(layout)
        if use_timer:
            QTimer.singleShot(delai * 1000, fenetre.close)
        if fullscreen:
            fenetre.showFullScreen()
        else:
            fenetre.show()
        #print("Popup créée.") # Pour débugger
        
        
def get_color():
    color = QColorDialog.getColor()
    if color.isValid():
        print(color.name())
        
window = test()
texte = "Bonjour, je suis un popup qui a beaucoup de choses à dire afin de tester la mise en page et les marges de la fenêtre !"
largeur = 500
hauteur = 300
window.creation_popup("Titre", texte, largeur, hauteur, "Arial", 14, 30)
get_color()
# Démarrer la boucle d'événements
sys.exit(app.exec())