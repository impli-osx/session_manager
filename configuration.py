import json
import os
import subprocess
import pickle
import ctypes
import ctypes.wintypes
import psutil
import winshell
import threading
import markdown
from psutil import users as psutil_users
from PyQt6 import QtWidgets, QtCore # Importe le module QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel # Importe les classes QApplication, QMainWindow, QMessageBox et QComboBox
from PyQt6.QtGui import QFontDatabase # Importe la classe QFontDatabase
from PyQt6.QtCore import Qt, QTimer, QObject, pyqtSignal # Importe les classes Qt, QTimer
from PyQt6.QtWebEngineWidgets import QWebEngineView # Importe la classe QWebEngineView
from Ui_configuration import Ui_Configuration # Importe la classe Ui_MainWindow du fichier Ui_mainwindow.py



# Classe pour la gestion de la fiche d'entrée
class AjouterChampDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)

        self.label_name_line_edit = QLineEdit(self)
        self.layout.addWidget(QLabel("Nom du QLabel :"))
        self.layout.addWidget(self.label_name_line_edit)

        self.enregistrer_button = QPushButton("Enregistrer", self)
        self.enregistrer_button.clicked.connect(self.enregistrer)
        self.layout.addWidget(self.enregistrer_button)

    def enregistrer(self):
        label_name = self.label_name_line_edit.text()

        # Créez un nouveau QLabel et ajoutez-le à un QVBoxLayout
        label = QLabel(label_name)
        layout = QVBoxLayout()
        layout.addWidget(label)

        # Enregistrez les données dans un fichier JSON
        data = {"label_name": label_name}
        with open("data.json", "w") as f:
            json.dump(data, f)

        self.close()

    def add_champ(self):
        self.dialog_ajouter_champ = AjouterChampDialog(self)
        self.dialog_ajouter_champ.show()


# Classe pour exécuter la commande gpupdate dans un thread
class Worker(QObject):
    output = pyqtSignal(str)
           
    def run_gpupdate(self):
        try:
            # Exécute la commande et capture la sortie
            result = subprocess.run(["gpupdate", "/force"], capture_output=True, text=True, check=True)
            lines = result.stdout.split('\n')
            non_empty_lines = [line for line in lines if line.strip() != '']
            cleaned_output = '\n'.join(non_empty_lines)
            self.output.emit(cleaned_output)

        except subprocess.CalledProcessError as e:
            # Si la commande échoue, affiche l'erreur dans le label
            self.output.emit(f"Erreur : {e.stderr}")
            
            
# Classe principale de l'application
class MainWindow(QMainWindow):
    
    # Constructeur de la classe
    def __init__(self, parent=None):
        super().__init__(parent) # Appelle le constructeur de la classe parente
        self.ui = Ui_Configuration() # Crée une instance de Ui_MainWindow
        self.ui.setupUi(self) # Charge l'interface utilisateur
        self.charger_conf() # Charge les données à partir du fichier JSON
        self.ui.annuler.clicked.connect(self.close) # Ferme la fenêtre (annule les modifications
        self.ui.Enregistrer.clicked.connect(self.enregistrer_conf) # Enregistrement de la configuration
        self.ui.gpupdate.clicked.connect(self.make_gpupdate) # Exécution de gpupdate
        self.ui.aide_titres.clicked.connect(lambda: self.afficher_aide('titres')) # Affiche l'aide pour le titre
        self.ui.aide_textes.clicked.connect(lambda: self.afficher_aide('textes')) # Affiche l'aide pour le texte
        self.ui.aide_temps.clicked.connect(lambda: self.afficher_aide('temps')) # Affiche l'aide pour le timer
        self.ui.aide_fiche.clicked.connect(lambda: self.afficher_aide('fiche')) # Affiche l'aide pour la fiche
        self.ui.aide_gestion.clicked.connect(lambda: self.afficher_aide('gestion')) # Affiche l'aide pour la gestion
        self.ui.aide_style.clicked.connect(lambda: self.afficher_aide('style')) # Affiche l'aide pour le style
        self.ui.aide_accueil.clicked.connect(lambda: self.afficher_aide('accueil')) # Affiche l'aide pour l'accueil
        self.ui.police.addItems(QFontDatabase.families()) # Ajoute les polices disponibles dans la liste déroulante
        users = psutil_users() # Récupère la liste des utilisateurs
        user_names = [user.name for user in users] # Récupère les noms des utilisateurs
        self.ui.session_user.addItems(user_names) # Ajoute les noms des utilisateurs dans la liste déroulante
        self.ui.session_activation.stateChanged.connect(self.session_activation_changed)
        
        self.ajouterchamp = AjouterChampDialog()
        self.ui.ajouter_champ.clicked.connect(self.ajouterchamp.add_champ)

        # Charge les données à partir du fichier JSON
        try:
            with open("config.json", "r") as f: # Ouvre le fichier JSON en lecture
                data = json.load(f) # Charge les données dans un dictionnaire
        except FileNotFoundError: # Si le fichier n'est pas trouvé, crée un dictionnaire vide
            data = {}



    # Fonction pour créer le raccourci
    def create_shortcut(self):
        try:
            # Défini current_folder comme le répertoire courant
            current_folder = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(current_folder, "session_manager.exe")
            # Vérifie que le fichier session_manager.exe existe dans le répertoire courant
            if not os.path.exists(file_path):
                return f"Erreur : l'éxecutable session_manager.exe est introuvable dans le répertoire courant.\nIl doit se trouver dans le répertoire : {current_folder}."
            # Récupère le nom de l'utilisateur sélectionné dans la liste déroulante
            user = self.ui.session_user.currentText()
            shortcut_path = f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\session_manager.lnk"
            # Crée le raccourci
            with winshell.shortcut(shortcut_path) as shortcut:
                shortcut.path = file_path
                shortcut.working_directory = current_folder
            return "Le raccourci a été créé correctement."
        except FileNotFoundError:
            return "Erreur : le fichier session_manager.exe n'a pas été trouvé."
        except Exception as e:
            return f"Erreur inattendue : {e}"




    # Fonction pour gérer l'activation du raccourci
    def session_activation_changed(self, state):
        user = self.ui.session_user.currentText()
        shortcut_path = f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\session_manager.lnk"
        # Si la case est cochée, crée le raccourci
        if self.ui.session_activation.isChecked():
            message = self.create_shortcut()
            self.ui.retour_activation.setText(message)
        # Sinon, supprime le raccourci
        else:
            if os.path.exists(shortcut_path):
                try:
                    os.remove(shortcut_path)
                    self.ui.retour_activation.setText("Le raccourci a été supprimé correctement.")
                except FileNotFoundError:
                    self.ui.retour_activation.setText("Erreur : Le raccourci n'existe pas.")
                except Exception as e:
                    self.ui.retour_activation.setText(f"Erreur inattendue : {e}")
    



    # Fonction pour afficher l'aide 
    def afficher_aide(self, type_aide):
        try:
            chemin_fichier = os.path.join("Aide", f"{type_aide}.md")
            with open(chemin_fichier, "r",encoding="utf-8") as f:
                aide = f.read()
            aide_html = markdown.markdown(aide)  # Convertit le Markdown en HTML
            msgBox = QMessageBox()
            msgBox.setTextFormat(Qt.TextFormat.RichText)  # Utilise un format de texte riche pour prendre en compte le HTML
            msgBox.setText(aide_html)  # Définit le texte de la fenêtre
            msgBox.setWindowTitle(f"Aide pour l'onglet {type_aide.capitalize()}")  # Définit le titre de la fenêtre
            msgBox.exec()
        except FileNotFoundError:  # Si le fichier n'est pas trouvé, affiche un message d'erreur
            QMessageBox.warning(self, "Erreur", f"Le fichier d'aide pour {type_aide} n'a pas été trouvé.")


            
        
        
    # Fonction pour modifier le label retour_gpupdate et éxecuter la fonction run_gpupdate dans un thread
    def make_gpupdate(self):
        # Affiche le message "gpupdate /force en cours..." dans le label retour_gpupdate
        self.ui.retour_gpupdate.setText("gpupdate /force en cours...")
        # Crée une instance de la classe Worker
        worker = Worker()
        # Connecte le signal output de l'instance worker à la fonction set_text
        worker.output.connect(self.ui.retour_gpupdate.setText)
        # Exécute la fonction run_gpupdate dans un thread
        threading.Thread(target=worker.run_gpupdate).start()    
        
        
        
        
    # Fonction pour enregistrer les données dans un fichier JSON
    def enregistrer_conf(self):
        try:
            # Crée un dictionnaire avec les données de l'interface utilisateur
            # Les données sont stockées dans un dictionnaire imbriqué
            config = {
                "titre" :{
                    "titre_popup_1" : self.ui.titre_popup_1.text(), # Récupère le texte du champ titre_popup_1
                    "titre_popup_2" : self.ui.titre_popup_2.text(), # Récupère le texte du champ titre_popup_2
                    "titre_popup_3" : self.ui.titre_popup_3.text(), # Récupère le texte du champ titre_popup_3
                    "titre_popup_4" : self.ui.titre_popup_4.text(), # Récupère le texte du champ titre_popup_4
                    "titre_reglement" : self.ui.titre_reglement.text(), # Récupère le texte du champ titre_reglement
                },
                "text" :{
                    "text_popup_1" : self.ui.text_popup_1.toPlainText(), # Récupère le texte du champ text_popup_1
                    "text_popup_2" : self.ui.text_popup_2.toPlainText(), # Récupère le texte du champ text_popup_2
                    "text_popup_3" : self.ui.text_popup_3.toPlainText(), # Récupère le texte du champ text_popup_3
                    "text_popup_4" : self.ui.text_popup_4.toPlainText(), # Récupère le texte du champ text_popup_4
                },
                "timer" :{
                    "delai_fermeture" : self.ui.delai_fermeture.text(), # Etc etc... other champ, same principe
                    "duree_session" : self.ui.duree_session.text(),
                    "timer_second_popup" : self.ui.timer_second_popup.text(),
                    "timer_troisieme_popup" : self.ui.timer_troisieme_popup.text(),
                    "timer_dernier_popup" : self.ui.timer_dernier_popup.text(),
                },
                "fiche" :{
                    "fiche_log" : self.ui.fiche_log.isChecked(),
                    "fiche_activation" : self.ui.fiche_activation.isChecked(),
                    "fiche_duree_session" : self.ui.fiche_duree_session.isChecked(),
                    "fiche_15min" : self.ui.fiche_15min.isChecked(),
                    "fiche_30min" : self.ui.fiche_30min.isChecked(),
                    "fiche_1h" : self.ui.fiche_1h.isChecked(),
                },
                "session" :{
                    "session_user" : self.ui.session_user.currentText(),
                    "session_activation" : self.ui.session_activation.isChecked(),
                },
                "style" :{
                    "largeur_popup" : self.ui.largeur_popup.text(),
                    "hauteur_popup" : self.ui.hauteur_popup.text(),
                    "police" : self.ui.police.currentText(),
                    "taille_police" : self.ui.taille_police.text(),
                },
                "fermeture" :{
                    "fermeture_session" : self.ui.fermeture_session.currentText(),
                    "fermeture_popup" : self.ui.activation_fermeture.isChecked(), 
                }
            }

            # Enregistrez les données dans un fichier JSON
            with open("config.json", "w") as f:
                json.dump(config, f,indent=4)
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Impossible d'enregistrer la configuration : {e}")
        # Ferme la fenêtre
        self.close()
            
            
            
    # Fonction pour charger les données à partir du fichier JSON
    def charger_conf(self):
        try:
            with open("config.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
        # Charge les données dans l'interface utilisateur
        self.ui.titre_popup_1.setText(data.get("titre", {}).get("titre_popup_1", "")) # Récupère le texte du champ titre_popup_1
        self.ui.titre_popup_2.setText(data.get("titre", {}).get("titre_popup_2", "")) # Récupère le texte du champ titre_popup_2
        self.ui.titre_popup_3.setText(data.get("titre", {}).get("titre_popup_3", "")) # Vous avez compris le concept...
        self.ui.titre_popup_4.setText(data.get("titre", {}).get("titre_popup_4", ""))
        self.ui.titre_reglement.setText(data.get("titre", {}).get("titre_reglement", ""))
        self.ui.text_popup_1.setPlainText(data.get("text", {}).get("text_popup_1", ""))
        self.ui.text_popup_2.setPlainText(data.get("text", {}).get("text_popup_2", ""))
        self.ui.text_popup_3.setPlainText(data.get("text", {}).get("text_popup_3", ""))
        self.ui.text_popup_4.setPlainText(data.get("text", {}).get("text_popup_4", ""))
        self.ui.delai_fermeture.setText(data.get("timer", {}).get("delai_fermeture", ""))
        self.ui.duree_session.setText(data.get("timer", {}).get("duree_session", ""))
        self.ui.timer_second_popup.setText(data.get("timer", {}).get("timer_second_popup", ""))
        self.ui.timer_troisieme_popup.setText(data.get("timer", {}).get("timer_troisieme_popup", ""))
        self.ui.timer_dernier_popup.setText(data.get("timer", {}).get("timer_dernier_popup", ""))
        self.ui.fiche_log.setChecked(data.get("fiche", {}).get("fiche_log", False))
        self.ui.fiche_activation.setChecked(data.get("fiche", {}).get("fiche_activation", False))
        self.ui.fiche_duree_session.setChecked(data.get("fiche", {}).get("fiche_duree_session", False))
        self.ui.fiche_15min.setChecked(data.get("fiche", {}).get("fiche_15min", False))
        self.ui.fiche_30min.setChecked(data.get("fiche", {}).get("fiche_30min", False))
        self.ui.fiche_1h.setChecked(data.get("fiche", {}).get("fiche_1h", False))
        self.ui.session_user.setCurrentText(data.get("session", {}).get("session_user", ""))
        self.ui.session_activation.setChecked(data.get("session", {}).get("session_activation", False))
        self.ui.largeur_popup.setText(data.get("style", {}).get("largeur_popup", ""))
        self.ui.hauteur_popup.setText(data.get("style", {}).get("hauteur_popup", ""))
        QTimer.singleShot(100, lambda: self.ui.police.setCurrentText(data.get("style", {}).get("police", "")))
        self.ui.taille_police.setText(data.get("style", {}).get("taille_police", ""))
        self.ui.fermeture_session.setCurrentText(data.get("fermeture", {}).get("fermeture_session", ""))
        self.ui.activation_fermeture.setChecked(data.get("fermeture", {}).get("activation_fermeture", False))
        
    # Fonction pour ajouter un champ à la fiche d'entrée
    def ajouter_champ(self):
        self.dialog_ajouter = QDialog()
        self.dialog_ajouter.show()



# Point d'entrée de l'application
if __name__ == "__main__":
    app = QApplication([]) # Crée une instance de QApplication
    window = MainWindow() # Crée une instance de MainWindow
    window.show() # Affiche la fenêtre
    app.exec() # Lance l'application