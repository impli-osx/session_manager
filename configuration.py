import json # Importe le module json
import os # Importe le module os
import subprocess # Importe le module subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox # Importe les classes QApplication, QMainWindow, QMessageBox et QComboBox
from PyQt6.QtGui import QFontDatabase # Importe la classe QFontDatabase
from PyQt6.QtCore import Qt # Importe la classe Qt
from Ui_configuration import Ui_Configuration # Importe la classe Ui_MainWindow du fichier Ui_mainwindow.py

# Classe principale de l'application
class MainWindow(QMainWindow):
    
    # Constructeur de la classe
    def __init__(self, parent=None):
        super().__init__(parent) # Appelle le constructeur de la classe parente
        self.ui = Ui_Configuration() # Crée une instance de Ui_MainWindow
        self.ui.setupUi(self) # Charge l'interface utilisateur
        self.charger_conf() # Charge les données à partir du fichier JSON
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
                
        
        
        
        # Charge les données à partir du fichier JSON
        try:
            with open("config.json", "r") as f: # Ouvre le fichier JSON en lecture
                data = json.load(f) # Charge les données dans un dictionnaire
        except FileNotFoundError: # Si le fichier n'est pas trouvé, crée un dictionnaire vide
                data = {}



    # Fonction pour afficher l'aide
    def afficher_aide(self, type_aide):
        try:
            chemin_fichier = os.path.join("Aide", f"{type_aide}.txt")
            print(f"Ouverture du fichier : {chemin_fichier}")  # Affiche le chemin du fichier
            with open(chemin_fichier, "r",encoding="utf-8") as f:
                aide = f.read()
            msgBox = QMessageBox()
            msgBox.setTextFormat(Qt.TextFormat.PlainText)  # Utilise un format de texte simple
            msgBox.setText(aide) # Définit le texte de la fenêtre
            msgBox.setWindowTitle(f"Aide pour l'onglet {type_aide.capitalize()}") # Définit le titre de la fenêtre
            msgBox.exec()
        except FileNotFoundError: # Si le fichier n'est pas trouvé, affiche un message d'erreur
            QMessageBox.warning(self, "Erreur", f"Le fichier d'aide pour {type_aide} n'a pas été trouvé.")



    # Fonction pour exécuter gpupdate
    def make_gpupdate(self):
        try:
            # Exécute la commande et capture la sortie
            result = subprocess.run(["gpupdate", "/force"], capture_output=True, text=True, check=True)

            # Met à jour le label avec la sortie de la commande
            self.ui.retour_gpupdate.setText(result.stdout)
        except subprocess.CalledProcessError as e:
            # Si la commande échoue, affiche l'erreur dans le label
            self.ui.retour_gpupdate.setText(f"Erreur : {e.stderr}")
        
        
        
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
                },
                "text" :{
                    "text_popup_1" : self.ui.text_popup_1.toPlainText(), # Récupère le texte du champ text_popup_1
                    "text_popup_2" : self.ui.text_popup_2.toPlainText(), # Récupère le texte du champ text_popup_2
                    "text_popup_3" : self.ui.text_popup_3.toPlainText(), # Récupère le texte du champ text_popup_3
                    "text_popup_4" : self.ui.text_popup_4.toPlainText(), # Récupère le texte du champ text_popup_4
                },
                "timer" :{
                    "delai_fermeture" : self.ui.delai_fermeture.text(), # Récupère le texte du champ delai_fermeture
                    "duree_session" : self.ui.duree_session.text(), # Récupère le texte du champ duree_session
                    "timer_second_popup" : self.ui.timer_second_popup.text(), # Récupère le texte du champ timer_second_popup
                    "timer_troisieme_popup" : self.ui.timer_troisieme_popup.text(), # Récupère le texte du champ timer_troisieme_popup
                    "timer_dernier_popup" : self.ui.timer_dernier_popup.text(), # Récupère le texte du champ timer_dernier_popup
                },
                "fiche" :{
                    "fiche_log" : self.ui.fiche_log.isChecked(), # Récupère l'état du champ fiche_log
                    "fiche_activation" : self.ui.fiche_activation.isChecked(), # Récupère l'état du champ fiche_activation
                    "fiche_nom" : self.ui.fiche_nom.isChecked(), # Récupère l'état du champ fiche_nom
                    "fiche_mail" : self.ui.fiche_mail.isChecked(), # Récupère l'état du champ fiche_mail
                    "fiche_adresse" : self.ui.fiche_adresse.isChecked(), # Récupère l'état du champ fiche_adresse
                    "fiche_telephone" : self.ui.fiche_telephone.isChecked(), # Récupère l'état du champ fiche_telephone
                    "fiche_duree_session" : self.ui.fiche_duree_session.isChecked(), # Récupère l'état du champ fiche_duree_session
                    "fiche_15min" : self.ui.fiche_15min.isChecked(), # Récupère l'état du champ fiche_15min
                    "fiche_30min" : self.ui.fiche_30min.isChecked(), # Récupère l'état du champ fiche_30min
                    "fiche_1h" : self.ui.fiche_1h.isChecked(), # Récupère l'état du champ fiche_1h
                    "fiche_bouton_reglement" : self.ui.fiche_bouton_reglement.isChecked(), # Récupère l'état du champ fiche_bouton_reglement
                    "fiche_reglement" : self.ui.fiche_reglement.isChecked(), # Récupère l'état du champ fiche_reglement
                },
                "session" :{
                    "session_user" : self.ui.session_user.currentText(), # Récupère le texte du champ session_user
                    "session_activation" : self.ui.session_activation.isChecked(), # Récupère l'état du champ session_activation
                },
                "style" :{
                    "largeur_popup" : self.ui.largeur_popup.text(), # Récupère le texte du champ largeur_popup
                    "hauteur_popup" : self.ui.hauteur_popup.text(), # Récupère le texte du champ hauteur_popup
                    "police" : self.ui.police.currentText(), # Récupère le texte du champ police
                    "taille_police" : self.ui.taille_police.text(), # Récupère le texte du champ taille_police
                },
                "fermeture" :{
                    "fermeture_session" : self.ui.fermeture_session.currentText(), # Récupère le texte du champ fermeture_session
                    "fermeture_popup" : self.ui.activation_fermeture.isChecked(), # Récupère l'état du champ activation_fermeture
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
        self.ui.titre_popup_3.setText(data.get("titre", {}).get("titre_popup_3", "")) # Vous avez compris le principe ...
        self.ui.titre_popup_4.setText(data.get("titre", {}).get("titre_popup_4", ""))
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
        self.ui.fiche_nom.setChecked(data.get("fiche", {}).get("fiche_nom", False))
        self.ui.fiche_mail.setChecked(data.get("fiche", {}).get("fiche_mail", False))
        self.ui.fiche_adresse.setChecked(data.get("fiche", {}).get("fiche_adresse", False))
        self.ui.fiche_telephone.setChecked(data.get("fiche", {}).get("fiche_telephone", False))
        self.ui.fiche_duree_session.setChecked(data.get("fiche", {}).get("fiche_duree_session", False))
        self.ui.fiche_15min.setChecked(data.get("fiche", {}).get("fiche_15min", False))
        self.ui.fiche_30min.setChecked(data.get("fiche", {}).get("fiche_30min", False))
        self.ui.fiche_1h.setChecked(data.get("fiche", {}).get("fiche_1h", False))
        self.ui.fiche_bouton_reglement.setChecked(data.get("fiche", {}).get("fiche_bouton_reglement", False))
        self.ui.fiche_reglement.setChecked(data.get("fiche", {}).get("fiche_reglement", False))
        self.ui.session_user.setCurrentText(data.get("session", {}).get("session_user", ""))
        self.ui.session_activation.setChecked(data.get("session", {}).get("session_activation", False))
        self.ui.largeur_popup.setText(data.get("style", {}).get("largeur_popup", ""))
        self.ui.hauteur_popup.setText(data.get("style", {}).get("hauteur_popup", ""))
        self.ui.police.setCurrentText(data.get("style", {}).get("police", ""))
        self.ui.taille_police.setText(data.get("style", {}).get("taille_police", ""))
        self.ui.fermeture_session.setCurrentText(data.get("fermeture", {}).get("fermeture_session", ""))
        self.ui.activation_fermeture.setChecked(data.get("fermeture", {}).get("activation_fermeture", False))
        
        
# Point d'entrée de l'application
if __name__ == "__main__":
    app = QApplication([]) # Crée une instance de QApplication
    window = MainWindow() # Crée une instance de MainWindow
    window.show() # Affiche la fenêtre
    app.exec() # Lance l'application