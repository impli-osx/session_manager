from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QMainWindow, QSpacerItem, QSizePolicy
from Ui_FicheEntree import Ui_Ficheentree
from PyQt6.QtCore import Qt

  
            
app = QApplication([])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Ficheentree()
        self.ui.setupUi(self)


        # Création d'un layout principal
        main_layout = QHBoxLayout(self)
        main_layout.addStretch(1)
        main_layout.addLayout(self.ui.formLayout_2)
        main_layout.addLayout(self.ui.formLayout_3)
        main_layout.addStretch(1)
        


        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        # Désactive le bouton 'connecter' au démarrage
        self.ui.connecter.setEnabled(False)

        # Connecte le signal 'clicked' de la checkbox à la méthode 'toggleConnectButton'
        self.ui.reglement.clicked.connect(self.toggleConnectButton)
        
        # Connecte le signal 'clicked' du bouton à la méthode 'close'
        self.ui.connecter.clicked.connect(self.close)

    def toggleConnectButton(self):
        # Active le bouton 'connecter' si la checkbox est cochée, le désactive sinon
        self.ui.connecter.setEnabled(self.ui.reglement.isChecked())

    def closeEvent(self, event):
        # Si la checkbox n'est pas cochée, ignore l'événement de fermeture
        if self.ui.reglement.checkState() != Qt.CheckState.Checked:
            event.ignore()

window = MainWindow()
window.showFullScreen()

app.exec()