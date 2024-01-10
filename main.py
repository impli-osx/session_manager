from PyQt6.QtWidgets import QApplication, QMainWindow
from interface import Ui_Configuration  # Assurez-vous que c'est le bon chemin d'importation

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Configuration()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()