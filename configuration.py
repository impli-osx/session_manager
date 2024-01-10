import json
from PyQt6.QtWidgets import QApplication, QMainWindow
from interface import Ui_Configuration  # Assurez-vous que c'est le bon chemin d'importation

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Configuration()
        self.ui.setupUi(self)
            
        # Load data from the JSON file
        try:
            with open("config.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
                data = {}
        """  
        # Fill the user interface fields with the data
        self.ui.fermeture_session.setText(data.get("fermeture_session", ""))
        self.ui.activation_fermeture.setChecked(data.get("activation_fermeture", False))
        """
        self.ui.Enregistrer.clicked.connect(self.enregistrer_conf)
                    
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
                    "text_popup_1" : self.ui.text_popup_1.text(),
                    "text_popup_2" : self.ui.text_popup_2.text(),
                    "text_popup_3" : self.ui.text_popup_3.text(),
                    "text_popup_4" : self.ui.text_popup_4.text(),
                },
                "timer" :{
                    "delai_fermeture" : self.ui.delai_fermeture.text(),
                    "duree_session" : self.ui.duree_session.text(),
                    "timer_second_popup" : self.ui.timer_second_popup.text(),
                    "timer_dernier_popup" : self.ui.timer_dernier_popup.text(),
                },
                "fiche" :{
                    "fiche_log" : self.ui.fiche_log.isChecked(),
                    "fiche_activation" : self.ui.ficher_activation.isChecked(),
                    "fiche_nom" : self.ui.fiche_nom.isChecked(),
                    "fiche_mail" : self.ui.fiche_mail.isChecked(),
                    "fiche_adresse" : self.ui.fiche_adresse.isChecked(),
                    "fiche_telephone" : self.ui.fiche_tel.isChecked(),
                    "fiche_duree_session" : self.ui.fiche_duree_session.isChecked(),
                    "fiche_15min" : self.ui.fiche_15min.isChecked(),
                    "fiche_30min" : self.ui.fiche_30min.isChecked(),
                    "fiche_1h" : self.ui.fiche_1h.isChecked(),
                    "fiche_bouton_reglement" : self.ui.fiche_bouton_reglement.isChecked(),
                    "fiche_reglement" : self.ui.fiche_reglement.isChecked(),
                },
                "session" :{
                    "session_user" : self.ui.session_user.text(),
                    "session_activation" : self.ui.session_activation.text(),
                },
                "style" :{
                    "largeur_popup" : self.ui.largeur_popup.text(),
                    "hauteur_popup" : self.ui.hauteur_popup.text(),
                    "police" : self.ui.police.text(),
                    "taille_police" : self.ui.taille_police.text(),
                },
                "fermeture" :{
                    "fermeture_session" : self.ui.fermeture_session.text(),
                    "fermeture_popup" : self.ui.fermeture_popup.text(),
                }
            }
        # Cette fonction est appelée lorsque l'utilisateur clique sur le bouton "Enregistrer"

        # Récupérez les données de l'interface utilisateur
        data = {
            "fermeture_session": self.ui.fermeture_session.text(),
            "activation_fermeture": self.ui.activation_fermeture.isChecked(),
            # Ajoutez ici d'autres champs si nécessaire
        }

        # Enregistrez les données dans un fichier JSON
        with open("config.json", "w") as f:
            json.dump(data, f)
            
            

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()