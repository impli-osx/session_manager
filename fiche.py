from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QCheckBox, QPushButton, QScrollArea, QFrame, QWidget,
                             QSpacerItem, QSizePolicy, QFormLayout, QGridLayout, QMessageBox, QComboBox,
                             QMessageBox, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem)
from PyQt6.QtGui import QPixmap, QFont, QPalette, QColor, QImage, QImageReader
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
import os
import sys
import json
import fitz
from PyQt6.QtCore import QUrl

class FicheWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.session_duration_label = QLabel("Choix de la durée de votre session")
        self.session_duration_combo = QComboBox()
        self.session_duration_combo.setObjectName("session_duration_combo")


        self.pdf_scroll_area = QScrollArea(self)
        
        
        # Créer un widget central pour la fenêtre
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.setStyleSheet("background-color: white;")
        
        
        # Créer un layout vertical principal
        main_layout = QVBoxLayout(central_widget)

        # Ajouter un logo
        logo = QLabel(self)
        pixmap = QPixmap('img\\logo_mairie.png')
        logo.setPixmap(pixmap)
        logo.resize(pixmap.width(), pixmap.height())  # Ajuster la taille du QLabel
        main_layout.addWidget(logo, alignment=Qt.AlignmentFlag.AlignLeft)

        # Créer un layout horizontal pour les colonnes et le cadre PDF
        columns_and_pdf_layout = QHBoxLayout()

        # Créer un widget pour contenir les colonnes
        columns_widget = QWidget(self)

        # Créer un layout pour les colonnes et leur titre
        columns_layout = QVBoxLayout(columns_widget)

        # Ajouter un titre pour les colonnes
        columns_title = QLabel("Vos informations", self)
        columns_title.setFont(QFont('Arial', 15, QFont.Weight.Bold))
        columns_title.setStyleSheet("color: #476e9e;")
        columns_layout.addWidget(columns_title, alignment=Qt.AlignmentFlag.AlignCenter)
        columns_layout.addSpacing(30)

        # Créer deux colonnes pour les QLabel et QLineEdit
        fields_layout = QHBoxLayout()
        column_layouts = [QVBoxLayout(), QVBoxLayout()]

        # Chargez les données de fiche.json
        with open('fiche.json', 'r') as f:
            champs = json.load(f)
        with open('config.json', 'r') as w:
            config = json.load(w)
        if config['fiche']['fiche_15min']:
            self.session_duration_combo.addItem("15 minutes")
        if config['fiche']['fiche_30min']:
            self.session_duration_combo.addItem("30 minutes")
        if config['fiche']['fiche_1h']:
            self.session_duration_combo.addItem("1 heure")
        # Triez les champs par le numéro d'ordre (qui est la clé du dictionnaire)
        champs_sorted = sorted(champs.items(), key=lambda item: int(item[0]))

        # Parcourez tous les champs
        for j, (order, champ) in enumerate(champs_sorted):
            # Crée un QVBoxLayout pour chaque groupe QLabel et QLineEdit
            group_layout = QVBoxLayout()
            # Crée un QLabel pour le champ
            label = QLabel(champ.get("label_content", ""))
            group_layout.addWidget(label)
            # Crée un QLineEdit pour le champ si nécessaire et l'ajoute au QVBoxLayout
            if champ.get("add_line_edit", False):
                line_edit = QLineEdit()
                line_edit.setObjectName(champ.get("label_content", "").replace(" ", ""))
                group_layout.addWidget(line_edit)
            # Ajouter le QVBoxLayout au layout de la colonne
            column_layouts[j % 2].addLayout(group_layout)
            # Ajouter un QSpacerItem entre chaque groupe
            if j < len(champs_sorted) - 1:  # Pas besoin d'ajouter un espace après le dernier groupe
                spacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
                column_layouts[j % 2].addItem(spacer)

        # Ajoutez le QLabel et le QComboBox à votre layout
        if config['fiche']['fiche_duree_session']:
            group_layout = QVBoxLayout()
            group_layout.addWidget(self.session_duration_label)
            group_layout.addWidget(self.session_duration_combo)
            # Ajouter le QVBoxLayout au layout de la colonne
            column_layouts[len(champs_sorted) % 2].addLayout(group_layout)
        else:
            self.session_duration_label.hide()
            self.session_duration_combo.hide()

        for i in range(2):
            column_layouts[i].setAlignment(Qt.AlignmentFlag.AlignTop)  # Ajouter cette ligne
            fields_layout.addLayout(column_layouts[i])
            if i == 0:
                fields_layout.addSpacing(20)

        columns_layout.addLayout(fields_layout)
        
        if not config['fiche']['fiche_duree_session']:
            self.session_duration_label.hide()
            self.session_duration_combo.hide()

        # Ajouter un spacer à la fin du layout vertical
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        columns_layout.addItem(spacer)

        # Ajouter le widget contenant les colonnes au layout principal
        columns_and_pdf_layout.addWidget(columns_widget)

        # Ajouter une marge à gauche pour les colonnes
        columns_widget.setContentsMargins(40, 0, 0, 0)  # 40 pixels à gauche

        # Ajouter un spacer au milieu
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        columns_and_pdf_layout.addItem(spacer)

        # Ajouter un cadre pour le PDF
        pdf_layout = QVBoxLayout()
        pdf_title = QLabel("Réglement intérieur de l'espace cyber", self)
        pdf_title.setFont(QFont('Arial', 15, QFont.Weight.Bold))
        pdf_title.setStyleSheet("color: #476e9e;")
        pdf_layout.addWidget(pdf_title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.pdf_frame = QFrame(self)
        self.pdf_frame.setFrameShape(QFrame.Shape.Box)
        self.pdf_frame.setLayout(QVBoxLayout())
        self.pdf_frame.layout().setContentsMargins(0, 0, 0, 0)

        self.pdf_frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.pdf_scroll_area = QScrollArea(self)
        self.pdf_scroll_area.setWidget(self.pdf_frame)
        self.pdf_scroll_area.setWidgetResizable(True)
        pdf_layout.addWidget(self.pdf_scroll_area)
        columns_and_pdf_layout.addLayout(pdf_layout)

        # Ajouter une marge à droite pour le cadre PDF
        pdf_layout.setContentsMargins(0, 0, 50, 0)  # 50 pixels à droite

        # Définir la proportion de l'espace que chaque layout doit occuper
        columns_and_pdf_layout.setStretch(0, 2)  # Les colonnes doivent occuper 2/6 de l'espace
        columns_and_pdf_layout.setStretch(1, 1)  # Le spacer doit occuper 1/6 de l'espace
        columns_and_pdf_layout.setStretch(2, 3)  # Le cadre PDF doit occuper 3/6 de l'espace

        # Ajouter le layout contenant les colonnes et le cadre PDF au layout principal
        main_layout.addLayout(columns_and_pdf_layout)

        # Créer une police
        font = QFont('Arial', 13, QFont.Weight.Bold)

        # Ajouter une QCheckBox
        self.reglement = QCheckBox("J'ai lu et j'accepte les conditions du règlement intérieur de l'espace numérique", self)
        self.reglement.setFont(font)  # Appliquer la police
        self.reglement.setStyleSheet("color: #476e9e;")
        main_layout.addWidget(self.reglement, alignment=Qt.AlignmentFlag.AlignCenter)

        # Ajouter un petit espace entre la QCheckBox et le QPushButton
        spacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        main_layout.addItem(spacer)

        # Ajouter un bouton
        self.connecter = QPushButton("Se connecter", self)
        #self.connecter.setFont(font)  # Appliquer la police
        self.connecter.setMinimumSize(160, 35)
        self.connecter.setStyleSheet("""
            QPushButton:enabled {
                background: linear-gradient(to bottom, #7892c2 5%, #476e9e 100%);
                background-color: #7892c2;
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
            QPushButton:disabled {
                background:linear-gradient(to bottom, #ededed 5%, #e3e3e3 100%);
                background-color:#ededed;
                border-radius:4px;
                border:1px solid #d6bcd6;
                color:#c9c9c9;
                font-family:Arial;
                font-size:15px;
                font-weight:bold;
                padding:9px 50px;
                text-decoration:none;
            }
        """)
        main_layout.addWidget(self.connecter, alignment=Qt.AlignmentFlag.AlignCenter)

        # Définir la proportion de l'espace que chaque widget ou layout doit occuper
        main_layout.setStretch(0, 1)  # Le logo doit occuper 1/10 de l'espace
        main_layout.setStretch(1, 8)  # Le layout contenant les colonnes et le cadre PDF doit occuper 6/10 de l'espace
        main_layout.setStretch(2, 0)  # La QCheckBox doit occuper 1/10 de l'espace
        main_layout.setStretch(3, 1)  # Le QPushButton doit occuper 2/10 de l'espace

        # Afficher la fenêtre en plein écran
        self.showFullScreen()


        # Désactive le bouton 'connecter' au démarrage
        self.connecter.setEnabled(False)
        # Connecte le signal 'clicked' de la checkbox à la méthode 'toggleConnectButton'
        self.reglement.clicked.connect(self.toggleConnectButton)
        # Connecte le signal 'clicked' du bouton à la méthode 'close'
        self.connecter.clicked.connect(self.close)




    def toggleConnectButton(self):
        # Active le bouton 'connecter' si la checkbox est cochée, le désactive sinon
        self.connecter.setEnabled(self.reglement.isChecked())




    def closeEvent(self, event):
        # Vérifier que tous les champs sont remplis
        all_fields_filled = all(line_edit.text() for line_edit in self.findChildren(QLineEdit))

        # Vérifier que la case du règlement est cochée
        reglement_checked = self.reglement.isChecked()

        # Réinitialiser le style de tous les champs
        for line_edit in self.findChildren(QLineEdit):
            line_edit.setStyleSheet("")

        if not all_fields_filled or not reglement_checked:
            # Si tous les champs ne sont pas remplis ou que la case du règlement n'est pas cochée, annuler la fermeture de la fenêtre
            event.ignore()

            # Afficher un message d'erreur
            error_message = QMessageBox()
            error_message.setIcon(QMessageBox.Icon.Warning)
            error_message.setWindowTitle("Erreur")
            error_message.setText("Vous devez remplir tous les champs pour vous connecter à votre session.")
            error_message.exec()

            # Encadrer les champs non remplis en rouge
            for line_edit in self.findChildren(QLineEdit):
                if not line_edit.text():
                    line_edit.setStyleSheet("border: 1px solid red;")
        else:
            # Si tous les champs sont remplis et que la case du règlement est cochée, fermer la fenêtre
            event.accept()



    def show_pdf(self, filename):
        try:
            # Obtenir le chemin absolu du fichier
            pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
            print(f"Chemin : {pdf_path} ")

            # Créer une scène pour les pages du PDF
            scene = QGraphicsScene()

            # Utiliser QImageReader pour charger les images du PDF
            image_reader = QImageReader(pdf_path)

            # Convertir chaque page en image et l'ajouter à la scène
            for i in range(image_reader.imageCount()):
                print(f"Boucle {i}")
                try:
                    # Charger l'image avec QImageReader
                    img = image_reader.read()

                    # Afficher les dimensions de l'image avant redimensionnement
                    print("Dimensions de l'image (avant redimensionnement) : ", img.width(), img.height())

                    # Créer un QGraphicsPixmapItem pour afficher l'image sans redimensionnement
                    pixmap_item = QGraphicsPixmapItem(QPixmap.fromImage(img))

                    # Ajouter le QGraphicsPixmapItem à la scène
                    scene.addItem(pixmap_item)

                    print("Objet ajouté à la scène")

                except Exception as conversion_error:
                    print(f"Erreur lors de la conversion de l'image {i}: {conversion_error}")
                    import traceback
                    traceback.print_exc()  # Affiche la trace de la pile d'appels

            # Créer un QGraphicsView pour afficher la scène
            print("Création de la vue")
            view = QGraphicsView(scene)
            print("Création du QGraphicsView")

            # Ajouter le QGraphicsView au cadre PDF
            self.pdf_frame.layout().addWidget(view)
            # Utiliser la variable de classe
            print("Ajout de la vue au cadre PDF")

            # Ajouter un message après la création du QGraphicsView pour vérifier si cette partie du code est atteinte
            print("Fin du traitement")

        except Exception as e:
            print(f"Erreur générale : {e}")
            import traceback
            traceback.print_exc()
        print("Fin du traitement")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FicheWindow()
    window.show_pdf("reglement.pdf")
    window.show()
    app.exec()