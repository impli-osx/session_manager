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
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QCheckBox, QScrollArea, QWidget, QFrame, QTableWidget, QTableWidgetItem # Importe les classes
from PyQt6.QtGui import QFontDatabase, QMovie  # Importe la classe QFontDatabase
from PyQt6.QtCore import Qt, QTimer, QObject, pyqtSignal, QThread, QSize # Importe les classes Qt, QTimer
from PyQt6.QtWebEngineWidgets import QWebEngineView # Importe la classe QWebEngineView
from Ui_configuration import Ui_Configuration # Importe la classe Ui_MainWindow du fichier Ui_mainwindow.py
from ficheentree import FicheWindow as FicheEntreeWindow # Importe la classe Ui_FicheEntree du fichier Ui_FicheEntree.py



# Classe pour la gestion de la fiche d'entrée
class AjouterChampDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Ajouter des champs")
        self.resize(600, 600)

        self.mainLayout = QVBoxLayout(self)  # Créez un layout pour le widget principal

        self.scrollArea = QScrollArea(self)  # Créez une QScrollArea
        self.scrollArea.setWidgetResizable(True)  # Permet au widget de se redimensionner
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Désactive le défilement horizontal

        self.scrollAreaContent = QWidget()  # Créez un widget pour le contenu de la zone de défilement
        self.layout = QVBoxLayout(self.scrollAreaContent)  # Ajoutez un layout à ce widget

        self.layout.addWidget(QLabel("Nombre de champs à ajouter :"))
        self.number_of_fields_line_edit = QLineEdit(self)
        self.layout.addWidget(self.number_of_fields_line_edit)

        self.enregistrer_button = QPushButton("Enregistrer", self)
        self.enregistrer_button.clicked.connect(self.enregistrer)
        self.layout.addWidget(self.enregistrer_button)

        self.fields = []  # Liste pour stocker les widgets

        self.table = QTableWidget(0, 2)  # Créez un QTableWidget avec 0 lignes et 2 colonnes
        self.table.setHorizontalHeaderLabels(["Contenu du label", "Ajouter un champ de saisie"])

        # Ajustez la largeur des colonnes
        self.table.setColumnWidth(0, 340)
        self.table.setColumnWidth(1, 200)

        self.layout.addWidget(self.table)

        self.scrollArea.setWidget(self.scrollAreaContent)  # Définissez le widget de la zone de défilement

        self.mainLayout.addWidget(self.scrollArea)  # Ajoutez la QScrollArea au layout principal




    def enregistrer(self):
        if not self.number_of_fields_line_edit.text():
            QMessageBox.critical(self, "Erreur", "Veuillez entrer le nombre de champs à ajouter.")
            return

        try:
            number_of_fields = int(self.number_of_fields_line_edit.text())
        except ValueError:
            QMessageBox.critical(self, "Erreur", "Veuillez entrer un nombre valide.")
            return

        for i in range(number_of_fields):
            self.table.insertRow(self.table.rowCount())  # Ajoutez une nouvelle ligne à la fin du tableau
            label_content_line_edit = QLineEdit(self)
            self.table.setCellWidget(i, 0, label_content_line_edit)
            add_line_edit_checkbox = QCheckBox("Ajouter un champ de saisie", self)
            self.table.setCellWidget(i, 1, add_line_edit_checkbox)
            self.fields.append((label_content_line_edit, add_line_edit_checkbox))

        # Vérifiez si le bouton "Enregistrer les champs" existe déjà
        if hasattr(self, 'enregistrer_button'):
            self.layout.removeWidget(self.enregistrer_button)
            self.enregistrer_button.deleteLater()

        self.enregistrer_button = QPushButton("Enregistrer les champs", self)
        self.enregistrer_button.clicked.connect(self.enregistrer_champs)
        self.layout.addWidget(self.enregistrer_button)



    def enregistrer_champs(self):
        fields = {}

        # Vérifiez si le fichier fiche.json existe déjà
        if os.path.exists('fiche.json'):
            with open('fiche.json', 'r') as f:
                fields = json.load(f)

        # Parcourez la liste et récupérez les informations de chaque champ
        for i, (label_content_line_edit, add_line_edit_checkbox) in enumerate(self.fields):
            label_content = label_content_line_edit.text()
            add_line_edit = add_line_edit_checkbox.isChecked()

            # Vérifiez si le champ est vide
            if not label_content.strip():
                QMessageBox.critical(self, "Erreur", "Veuillez remplir tous les champs avant d'enregistrer.")
                return

            display_order = str(max([int(k) for k in fields.keys()], default=0) + 1)

            # Enregistrez les données dans un dictionnaire
            fields[display_order] = {"label_content": label_content, "add_line_edit": add_line_edit}

        # Triez les champs par ordre d'affichage
        fields = dict(sorted(fields.items()))

        # Enregistrez les champs dans votre fichier JSON
        with open('fiche.json', 'w') as f:
            json.dump(fields, f)

        self.close()



    def add_champ(self):
        self.dialog_ajouter_champ = AjouterChampDialog(self)
        self.dialog_ajouter_champ.show()



class SupprimerChampDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Supprimer des champs")
        self.setMinimumSize(250, 500)  # Définir une taille minimale pour la fenêtre

        self.layout = QVBoxLayout(self)

        # Crée un QTableWidget pour afficher les éléments
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["Label", "Supprimer"])
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # Désactivez le défilement horizontal
        self.layout.addWidget(self.table)

        # Bouton pour confirmer la suppression
        self.confirm_button = QPushButton("Confirmer", self)
        self.confirm_button.clicked.connect(self.supprimer_champs)
        self.layout.addWidget(self.confirm_button)

        self.showEvent = self.update_liste

        self.update_liste()

    def update_liste(self, event=None):
        # Supprime les anciennes lignes
        self.table.setRowCount(0)

        # Vérifiez si le fichier fiche.json existe
        if not os.path.exists('fiche.json'):
            QMessageBox.critical(self, "Erreur", "Le fichier fiche.json n'existe pas.")
            return

        # Chargez les données de fiche.json
        with open('fiche.json', 'r') as f:
            fields = json.load(f)

        # Créez une ligne pour chaque entrée
        for field in fields.values():
            # Prenez les deux premiers mots du contenu du label
            label_content = field['label_content']
            words = label_content.split()
            label_text = ' '.join(words[:2])

            # Créez un QTableWidgetItem pour le label
            label_item = QTableWidgetItem(label_text)
            label_item.setFlags(label_item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Rend l'item non éditable

            # Créez un QCheckBox pour la case à cocher
            checkbox = QCheckBox()

            # Ajoutez une nouvelle ligne à la table
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, label_item)
            self.table.setCellWidget(row, 1, checkbox)

    def supprimer_champs(self):
        # Créez une liste pour stocker les labels à supprimer
        labels_to_remove = []

        # Parcourez les lignes de la table
        for row in range(self.table.rowCount()):
            # Obtenez la case à cocher pour cette ligne
            checkbox = self.table.cellWidget(row, 1)

            # Si la case à cocher est cochée, ajoutez le label à la liste des labels à supprimer
            if checkbox.isChecked():
                label_item = self.table.item(row, 0)
                labels_to_remove.append(label_item.text())

        # Maintenant, vous pouvez utiliser labels_to_remove pour supprimer les champs correspondants
        with open('fiche.json', 'r') as f:
            fields = json.load(f)

        keys_to_remove = []

        # Parcourez le dictionnaire pour trouver les clés correspondant aux labels à supprimer
        for key, value in fields.items():
            if value['label_content'] in labels_to_remove:
                keys_to_remove.append(key)

        # Supprimez les entrées correspondant aux clés à supprimer
        for key in keys_to_remove:
            del fields[key]

        with open('fiche.json', 'w') as f:
            json.dump(fields, f)

        # Ferme la fenêtre
        self.close()
        self.update_liste()



class ModifierOrdreDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Chargez les données de fiche.json
        with open('fiche.json', 'r') as f:
            self.champs = json.load(f)
            
        self.setWindowTitle("Modifier l'ordre des champs")
        
        # Triez les champs par le numéro d'ordre (qui est la clé du dictionnaire)
        self.champs_sorted = sorted(self.champs.items(), key=lambda item: int(item[0]))

        # Créez un QTableWidget pour afficher les éléments
        self.table = QTableWidget(len(self.champs_sorted), 2)
        self.table.setHorizontalHeaderLabels(["Label", "Numéro d'ordre"])

        # Parcourez tous les champs
        for i, (order, champ) in enumerate(self.champs_sorted):
            # Ajoutez le label de l'élément à la première colonne
            self.table.setItem(i, 0, QTableWidgetItem(champ.get("label_content", "")))

            # Ajoutez un QLineEdit pour modifier le numéro d'ordre à la deuxième colonne
            line_edit = QLineEdit(order)
            self.table.setCellWidget(i, 1, line_edit)

        # Créez un bouton pour enregistrer les modifications
        self.enregistrer_button = QPushButton('Enregistrer')
        self.enregistrer_button.clicked.connect(self.enregistrer)

        # Augmentez la taille de la fenêtre
        self.table.setFixedSize(240, 400)

        # Créez un QScrollArea et ajoutez le QTableWidget à celui-ci
        scroll_area = QScrollArea()
        scroll_area.setWidget(self.table)

        # Ajoutez le QScrollArea et le bouton à la fenêtre
        layout = QVBoxLayout(self)
        layout.addWidget(scroll_area)
        layout.addWidget(self.enregistrer_button)

        self.table.setCellWidget(i, 1, line_edit)

        # Créez un bouton pour enregistrer les modifications
        self.enregistrer_button = QPushButton('Enregistrer')
        self.enregistrer_button.clicked.connect(self.enregistrer)

        # Ajoutez le QTableWidget et le bouton à la fenêtre
        layout = QVBoxLayout(self)
        layout.addWidget(self.table)
        layout.addWidget(self.enregistrer_button)

        self.showEvent = self.update_liste



    def update_liste(self, event):
        # Chargez les données de fiche.json
        with open('fiche.json', 'r') as f:
            self.champs = json.load(f)

        # Triez les champs par le numéro d'ordre (qui est la clé du dictionnaire)
        self.champs_sorted = sorted(self.champs.items(), key=lambda item: int(item[0]))

        # Mettez à jour le nombre de lignes de la table
        self.table.setRowCount(len(self.champs_sorted))

        # Parcourez tous les champs
        for i, (order, champ) in enumerate(self.champs_sorted):
            # Ajoutez le label de l'élément à la première colonne
            self.table.setItem(i, 0, QTableWidgetItem(champ.get("label_content", "")))

            # Ajoutez un QLineEdit pour modifier le numéro d'ordre à la deuxième colonne
            line_edit = QLineEdit(order)
            self.table.setCellWidget(i, 1, line_edit)



    def enregistrer(self):
        # Collectez tous les nouveaux numéros d'ordre
        new_orders = [self.table.cellWidget(i, 1).text() for i in range(self.table.rowCount())]

        # Vérifiez si la liste contient des doublons
        if len(new_orders) != len(set(new_orders)):
            QMessageBox.critical(self, "Erreur", "Le numéro d'ordre est déjà utilisé.")
            return

        # Créez un nouveau dictionnaire pour les champs avec les nouveaux numéros d'ordre
        new_champs = {}
        for i, (order, champ) in enumerate(self.champs_sorted):
            new_champs[new_orders[i]] = champ

        # Enregistrez les modifications dans fiche.json
        with open('fiche.json', 'w') as f:
            json.dump(new_champs, f)

        # Mettez à jour self.champs et self.champs_sorted
        self.champs = new_champs
        self.champs_sorted = sorted(self.champs.items(), key=lambda item: int(item[0]))

        # Fermez la fenêtre
        self.accept()



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
        
        # Crée l'instance de classe pour l'ajout de champs de la fiche d'entrée
        self.ajouterchamp = AjouterChampDialog()
        self.ui.ajouter_champ.clicked.connect(self.ajouterchamp.add_champ)
        
        # Crée l'instance de classe pour la suppression de champs de la fiche d'entrée
        self.supprimerchamp = SupprimerChampDialog()
        self.ui.supprimer_champ.clicked.connect(self.supprimerchamp.show)
        
        # Crée l'instance de classe pour la modification de l'ordre des champs de la fiche d'entrée
        self.ui.modifierordre = ModifierOrdreDialog()
        self.ui.modifier_ordre.clicked.connect(self.ui.modifierordre.show)
        
        # Connecte le signal clicked du bouton fiche_afficher à la méthode afficher_fiche_entree
        self.ui.fiche_afficher.clicked.connect(self.afficher_fiche_entree)

        # Ajouter les choix à la QComboBox fermeture_session
        self.ui.fermeture_session.addItem("Déconnecter")
        self.ui.fermeture_session.addItem("Verrouiller")

        # Connectez le signal currentTextChanged à une nouvelle méthode
        self.ui.fermeture_session.currentTextChanged.connect(self.on_combobox_changed)

        # Crée et affiche un QLabel avec un QMovie
        self.movie = QMovie("loading.gif")  # Remplacez "loading.gif" par le chemin de votre fichier GIF
        self.movie.setScaledSize(QSize(140, 80)) 
        self.gpupdate_thread = QThread()
        self.ui.retour_gpupdate.setMovie(self.movie)

        # Arrête le QMovie et cache le QLabel lorsque le thread est terminé
        self.gpupdate_thread.finished.connect(self.movie.stop)

        # Charge les données à partir du fichier JSON
        try:
            with open("config.json", "r") as f: # Ouvre le fichier JSON en lecture
                data = json.load(f) # Charge les données dans un dictionnaire
        except FileNotFoundError: # Si le fichier n'est pas trouvé, crée un dictionnaire vide
            data = {}


    # On affiche un message d'informations si l'utilisateur sélectionne "Verrouiller"
    def on_combobox_changed(self, text):
        if text == "Verrouiller":
            QMessageBox.information(self, "Information", "Le verrouillage ne permettra pas de lancer le Session Manager automatiquement à la prochaine connexion de la session.\n\nVous devrez déconnecter la session manuellement pour que Session Manager fonctionne automatiquement.")



    def afficher_fiche_entree(self):
        # Crée et affiche une instance de FicheEntreeWindow
        self.fiche_entree_window = FicheEntreeWindow()
        self.fiche_entree_window.show()



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
        if hasattr(self, 'gpupdate_thread') and self.gpupdate_thread.isRunning():
            self.gpupdate_thread.quit()
            self.gpupdate_thread.wait()
        # Crée un Worker et un QThread
        self.gpupdate_thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.gpupdate_thread)

        # Connecte les signaux
        self.worker.output.connect(self.update_output)
        self.gpupdate_thread.started.connect(self.worker.run_gpupdate)
        self.gpupdate_thread.finished.connect(self.gpupdate_thread.deleteLater)

        # Crée et affiche un QLabel avec un QMovie
        #self.movie = QMovie("loading.gif")  # Remplacez "loading.gif" par le chemin de votre fichier GIF
        #self.movie.setScaledSize(QSize(140, 80)) 
        #self.ui.retour_gpupdate.setMovie(self.movie)

        # Arrête le QMovie et cache le QLabel lorsque le thread est terminé
        #self.gpupdate_thread.finished.connect(self.movie.stop)
        
        self.movie.start()
        # Démarre le thread
        self.gpupdate_thread.start()  
        
        
        
    def update_output(self, text):
        # Met à jour le QLabel avec le résultat de la commande gpupdate /force
        self.ui.retour_gpupdate.setText(text)
        
        
        
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