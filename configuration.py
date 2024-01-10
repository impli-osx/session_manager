import json
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from Ui_configuration import Ui_Configuration

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Configuration()
        self.ui.setupUi(self)
        self.charger_conf()
        self.ui.Enregistrer.clicked.connect(self.enregistrer_conf)
        self.ui.gpupdate.clicked.connect(self.make_gpupdate)   
        # Charge les données à partir du fichier JSON
        try:
            with open("config.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
                data = {}

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
            config = {
                "titre" :{
                    "titre_popup_1" : self.ui.titre_popup_1.text(),
                    "titre_popup_2" : self.ui.titre_popup_2.text(),
                    "titre_popup_3" : self.ui.titre_popup_3.text(),
                    "titre_popup_4" : self.ui.titre_popup_4.text(),
                },
                "text" :{
                    "text_popup_1" : self.ui.text_popup_1.toPlainText(),
                    "text_popup_2" : self.ui.text_popup_2.toPlainText(),
                    "text_popup_3" : self.ui.text_popup_3.toPlainText(),
                    "text_popup_4" : self.ui.text_popup_4.toPlainText(),
                },
                "timer" :{
                    "delai_fermeture" : self.ui.delai_fermeture.text(),
                    "duree_session" : self.ui.duree_session.text(),
                    "timer_second_popup" : self.ui.timer_second_popup.text(),
                    "timer_troisieme_popup" : self.ui.timer_troisieme_popup.text(),
                    "timer_dernier_popup" : self.ui.timer_dernier_popup.text(),
                },
                "fiche" :{
                    "fiche_log" : self.ui.fiche_log.isChecked(),
                    "fiche_activation" : self.ui.fiche_activation.isChecked(),
                    "fiche_nom" : self.ui.fiche_nom.isChecked(),
                    "fiche_mail" : self.ui.fiche_mail.isChecked(),
                    "fiche_adresse" : self.ui.fiche_adresse.isChecked(),
                    "fiche_telephone" : self.ui.fiche_telephone.isChecked(),
                    "fiche_duree_session" : self.ui.fiche_duree_session.isChecked(),
                    "fiche_15min" : self.ui.fiche_15min.isChecked(),
                    "fiche_30min" : self.ui.fiche_30min.isChecked(),
                    "fiche_1h" : self.ui.fiche_1h.isChecked(),
                    "fiche_bouton_reglement" : self.ui.fiche_bouton_reglement.isChecked(),
                    "fiche_reglement" : self.ui.fiche_reglement.isChecked(),
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
            QMessageBox.critical(self, "Erreur", str(e))
            
        self.close()
            
    def charger_conf(self):
        try:
            with open("config.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
            
        self.ui.titre_popup_1.setText(data.get("titre", {}).get("titre_popup_1", ""))
        self.ui.titre_popup_2.setText(data.get("titre", {}).get("titre_popup_2", ""))
        self.ui.titre_popup_3.setText(data.get("titre", {}).get("titre_popup_3", ""))
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
        
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()