import sys
from PyQt6.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, QComboBox, QMessageBox, QColorDialog
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import QTimer, Qt, QTranslator, QLocale, QLibraryInfo
from PyQt6.QtWidgets import QApplication
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
            bouton.setFixedSize(300, 50)
            bouton.setStyleSheet(f"""
            QPushButton:enabled {{
                background: linear-gradient(to bottom, #7892c2 50%, #ffffff 100%);
                background-color: #5472bd;
                border-radius: 15px;
                border: 1px solid #4e6096;
                color: #ffffff;
                font-family: Arial;
                font-size: {taille_police}px;
                font-weight: bold;
                padding: 9px 50px;
                text-decoration: none;
            }}
            QPushButton:hover {{
                background: linear-gradient(to bottom, #476e9e 50%, #7892c2 100%);
                background-color: #476e9e;
            }}
            QPushButton:pressed {{
                position: relative;
                top: 1px;
            }}
            """)
            #bouton.setFont(font)
            bouton.clicked.connect(fenetre.close)
            layout.addWidget(bouton)
            # Créer un QHBoxLayout
            layout_bouton = QHBoxLayout()
            # Ajouter un QSpacerItem à gauche
            layout_bouton.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
            # Ajouter le bouton au layout
            layout_bouton.addWidget(bouton)
            # Ajouter un QSpacerItem à droite
            layout_bouton.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
            # Ajouter le layout_bouton au layout principal
            layout.addLayout(layout_bouton)
        fenetre.setLayout(layout)
        if use_timer:
            QTimer.singleShot(delai * 1000, fenetre.close)
        if fullscreen:
            fenetre.showFullScreen()
        else:
            fenetre.show()
        #print("Popup créée.") # Pour débugger
        
        
def get_color(app):
    translator = QTranslator(app)
    locale = QLocale.system().name()
    path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    translator.load("qt_" + locale, path)
    app.installTranslator(translator)

    color = QColorDialog.getColor()
    if color.isValid():
        print(color.name())

        
window = test()
texte = "Bonjour, je suis un popup qui a beaucoup de choses à dire afin de tester la mise en page et les marges de la fenêtre !"
largeur = 500
hauteur = 300
window.creation_popup("Titre", texte, largeur, hauteur, "Arial", 14, 30)
#get_color(app)
# Démarrer la boucle d'événements
sys.exit(app.exec())