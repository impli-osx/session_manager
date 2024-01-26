from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QCheckBox, QPushButton, QScrollArea, QFrame, QWidget,
                             QSpacerItem, QSizePolicy)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget

class FicheWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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
        columns_layout.addWidget(columns_title, alignment=Qt.AlignmentFlag.AlignCenter)

        # Créer deux colonnes pour les QLabel et QLineEdit
        fields_layout = QHBoxLayout()
        for _ in range(2):
            column_layout = QVBoxLayout()
            for _ in range(5):  # Ajouter 5 QLabel et QLineEdit à chaque colonne
                label = QLabel("Label", self)
                line_edit = QLineEdit(self)
                column_layout.addWidget(label)
                column_layout.addWidget(line_edit)
            fields_layout.addLayout(column_layout)
            if _ == 0:  # Ajouter de l'espace entre les deux colonnes
                fields_layout.addSpacing(20)
        columns_layout.addLayout(fields_layout)

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
        pdf_layout.addWidget(pdf_title, alignment=Qt.AlignmentFlag.AlignCenter)
        pdf_frame = QFrame(self)
        pdf_frame.setFrameShape(QFrame.Shape.Box)
        pdf_frame.setFrameShadow(QFrame.Shadow.Sunken)
        pdf_scroll_area = QScrollArea(self)
        pdf_scroll_area.setWidget(pdf_frame)
        pdf_scroll_area.setWidgetResizable(True)
        pdf_layout.addWidget(pdf_scroll_area)
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
        reglement = QCheckBox("J'ai lu et j'accepte le réglement intérieur de l'espace cyber", self)
        reglement.setFont(font)  # Appliquer la police
        main_layout.addWidget(reglement, alignment=Qt.AlignmentFlag.AlignCenter)

        # Ajouter un petit espace entre la QCheckBox et le QPushButton
        spacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        main_layout.addItem(spacer)

        # Ajouter un bouton
        connecter = QPushButton("Se connecter", self)
        connecter.setFont(font)  # Appliquer la police
        connecter.setMinimumSize(160, 35)
        main_layout.addWidget(connecter, alignment=Qt.AlignmentFlag.AlignCenter)

        # Définir la proportion de l'espace que chaque widget ou layout doit occuper
        main_layout.setStretch(0, 1)  # Le logo doit occuper 1/10 de l'espace
        main_layout.setStretch(1, 8)  # Le layout contenant les colonnes et le cadre PDF doit occuper 6/10 de l'espace
        main_layout.setStretch(2, 0)  # La QCheckBox doit occuper 1/10 de l'espace
        main_layout.setStretch(3, 1)  # Le QPushButton doit occuper 2/10 de l'espace

        # Afficher la fenêtre en plein écran
        self.showFullScreen()

if __name__ == "__main__":
    app = QApplication([])
    window = FicheWindow()
    window.show()
    app.exec()