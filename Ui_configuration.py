# Form implementation generated from reading ui file 'configuration.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Configuration(object):
    def setupUi(self, Configuration):
        Configuration.setObjectName("Configuration")
        Configuration.resize(868, 478)
        self.centralwidget = QtWidgets.QWidget(parent=Configuration)
        self.centralwidget.setObjectName("centralwidget")
        self.onglet = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.onglet.setGeometry(QtCore.QRect(10, 10, 851, 381))
        self.onglet.setObjectName("onglet")
        self.accueil = QtWidgets.QWidget()
        self.accueil.setObjectName("accueil")
        self.session_activation = QtWidgets.QCheckBox(parent=self.accueil)
        self.session_activation.setGeometry(QtCore.QRect(20, 60, 361, 31))
        self.session_activation.setObjectName("session_activation")
        self.aide_accueil = QtWidgets.QPushButton(parent=self.accueil)
        self.aide_accueil.setGeometry(QtCore.QRect(760, 10, 75, 24))
        self.aide_accueil.setObjectName("aide_accueil")
        self.retour_activation = QtWidgets.QLabel(parent=self.accueil)
        self.retour_activation.setGeometry(QtCore.QRect(40, 100, 791, 71))
        self.retour_activation.setObjectName("retour_activation")
        self.session_user = QtWidgets.QComboBox(parent=self.accueil)
        self.session_user.setGeometry(QtCore.QRect(170, 20, 141, 22))
        self.session_user.setObjectName("session_user")
        self.user_session = QtWidgets.QLabel(parent=self.accueil)
        self.user_session.setGeometry(QtCore.QRect(20, 20, 151, 16))
        self.user_session.setObjectName("user_session")
        self.gpupdate = QtWidgets.QPushButton(parent=self.accueil)
        self.gpupdate.setGeometry(QtCore.QRect(20, 180, 301, 24))
        self.gpupdate.setObjectName("gpupdate")
        self.retour_gpupdate = QtWidgets.QLabel(parent=self.accueil)
        self.retour_gpupdate.setGeometry(QtCore.QRect(30, 220, 771, 121))
        self.retour_gpupdate.setObjectName("retour_gpupdate")
        self.onglet.addTab(self.accueil, "")
        self.formulaire = QtWidgets.QWidget()
        self.formulaire.setObjectName("formulaire")
        self.fiche_activation = QtWidgets.QCheckBox(parent=self.formulaire)
        self.fiche_activation.setGeometry(QtCore.QRect(20, 20, 491, 20))
        self.fiche_activation.setObjectName("fiche_activation")
        self.fiche_log = QtWidgets.QCheckBox(parent=self.formulaire)
        self.fiche_log.setGeometry(QtCore.QRect(20, 60, 491, 20))
        self.fiche_log.setObjectName("fiche_log")
        self.Informations = QtWidgets.QGroupBox(parent=self.formulaire)
        self.Informations.setGeometry(QtCore.QRect(10, 250, 821, 71))
        self.Informations.setObjectName("Informations")
        self.ajouter_champ = QtWidgets.QPushButton(parent=self.Informations)
        self.ajouter_champ.setGeometry(QtCore.QRect(110, 30, 141, 24))
        self.ajouter_champ.setObjectName("ajouter_champ")
        self.supprimer_champ = QtWidgets.QPushButton(parent=self.Informations)
        self.supprimer_champ.setGeometry(QtCore.QRect(300, 30, 141, 24))
        self.supprimer_champ.setObjectName("supprimer_champ")
        self.fiche_afficher = QtWidgets.QPushButton(parent=self.Informations)
        self.fiche_afficher.setGeometry(QtCore.QRect(490, 30, 231, 24))
        self.fiche_afficher.setObjectName("fiche_afficher")
        self.aide_fiche = QtWidgets.QPushButton(parent=self.formulaire)
        self.aide_fiche.setGeometry(QtCore.QRect(760, 10, 75, 24))
        self.aide_fiche.setObjectName("aide_fiche")
        self.fiche_1h = QtWidgets.QCheckBox(parent=self.formulaire)
        self.fiche_1h.setGeometry(QtCore.QRect(50, 190, 75, 20))
        self.fiche_1h.setObjectName("fiche_1h")
        self.fiche_duree_session = QtWidgets.QCheckBox(parent=self.formulaire)
        self.fiche_duree_session.setGeometry(QtCore.QRect(20, 100, 341, 20))
        self.fiche_duree_session.setObjectName("fiche_duree_session")
        self.fiche_15min = QtWidgets.QCheckBox(parent=self.formulaire)
        self.fiche_15min.setGeometry(QtCore.QRect(50, 130, 221, 20))
        self.fiche_15min.setObjectName("fiche_15min")
        self.fiche_30min = QtWidgets.QCheckBox(parent=self.formulaire)
        self.fiche_30min.setGeometry(QtCore.QRect(50, 160, 181, 20))
        self.fiche_30min.setObjectName("fiche_30min")
        self.onglet.addTab(self.formulaire, "")
        self.titres = QtWidgets.QWidget()
        self.titres.setObjectName("titres")
        self.aide_titres = QtWidgets.QPushButton(parent=self.titres)
        self.aide_titres.setGeometry(QtCore.QRect(760, 10, 75, 24))
        self.aide_titres.setObjectName("aide_titres")
        self.label_titre_1 = QtWidgets.QLabel(parent=self.titres)
        self.label_titre_1.setGeometry(QtCore.QRect(20, 60, 151, 16))
        self.label_titre_1.setObjectName("label_titre_1")
        self.label_titre_2 = QtWidgets.QLabel(parent=self.titres)
        self.label_titre_2.setGeometry(QtCore.QRect(20, 100, 131, 16))
        self.label_titre_2.setObjectName("label_titre_2")
        self.label_titre__3 = QtWidgets.QLabel(parent=self.titres)
        self.label_titre__3.setGeometry(QtCore.QRect(20, 140, 141, 16))
        self.label_titre__3.setObjectName("label_titre__3")
        self.titre_popup_1 = QtWidgets.QLineEdit(parent=self.titres)
        self.titre_popup_1.setGeometry(QtCore.QRect(160, 60, 431, 21))
        self.titre_popup_1.setObjectName("titre_popup_1")
        self.titre_popup_2 = QtWidgets.QLineEdit(parent=self.titres)
        self.titre_popup_2.setGeometry(QtCore.QRect(160, 100, 431, 21))
        self.titre_popup_2.setObjectName("titre_popup_2")
        self.titre_popup_3 = QtWidgets.QLineEdit(parent=self.titres)
        self.titre_popup_3.setGeometry(QtCore.QRect(160, 140, 431, 21))
        self.titre_popup_3.setObjectName("titre_popup_3")
        self.label_18 = QtWidgets.QLabel(parent=self.titres)
        self.label_18.setGeometry(QtCore.QRect(20, 180, 161, 16))
        self.label_18.setObjectName("label_18")
        self.titre_popup_4 = QtWidgets.QLineEdit(parent=self.titres)
        self.titre_popup_4.setGeometry(QtCore.QRect(170, 180, 421, 21))
        self.titre_popup_4.setObjectName("titre_popup_4")
        self.label_21 = QtWidgets.QLabel(parent=self.titres)
        self.label_21.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_21.setObjectName("label_21")
        self.titre_reglement = QtWidgets.QLineEdit(parent=self.titres)
        self.titre_reglement.setGeometry(QtCore.QRect(160, 20, 431, 21))
        self.titre_reglement.setObjectName("titre_reglement")
        self.onglet.addTab(self.titres, "")
        self.textes = QtWidgets.QWidget()
        self.textes.setObjectName("textes")
        self.aide_textes = QtWidgets.QPushButton(parent=self.textes)
        self.aide_textes.setGeometry(QtCore.QRect(760, 10, 75, 24))
        self.aide_textes.setObjectName("aide_textes")
        self.onglet_popup = QtWidgets.QTabWidget(parent=self.textes)
        self.onglet_popup.setGeometry(QtCore.QRect(10, 40, 831, 311))
        self.onglet_popup.setObjectName("onglet_popup")
        self.onglet_popup_1 = QtWidgets.QWidget()
        self.onglet_popup_1.setObjectName("onglet_popup_1")
        self.label_text_1 = QtWidgets.QLabel(parent=self.onglet_popup_1)
        self.label_text_1.setGeometry(QtCore.QRect(10, 10, 211, 16))
        self.label_text_1.setObjectName("label_text_1")
        self.text_popup_1 = QtWidgets.QPlainTextEdit(parent=self.onglet_popup_1)
        self.text_popup_1.setGeometry(QtCore.QRect(10, 40, 811, 241))
        self.text_popup_1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_popup_1.setObjectName("text_popup_1")
        self.onglet_popup.addTab(self.onglet_popup_1, "")
        self.onglet_popup_2 = QtWidgets.QWidget()
        self.onglet_popup_2.setObjectName("onglet_popup_2")
        self.label_text_2 = QtWidgets.QLabel(parent=self.onglet_popup_2)
        self.label_text_2.setGeometry(QtCore.QRect(10, 10, 301, 16))
        self.label_text_2.setObjectName("label_text_2")
        self.text_popup_2 = QtWidgets.QPlainTextEdit(parent=self.onglet_popup_2)
        self.text_popup_2.setGeometry(QtCore.QRect(10, 40, 811, 241))
        self.text_popup_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_popup_2.setObjectName("text_popup_2")
        self.onglet_popup.addTab(self.onglet_popup_2, "")
        self.onglet_popup_3 = QtWidgets.QWidget()
        self.onglet_popup_3.setObjectName("onglet_popup_3")
        self.label_popup_3 = QtWidgets.QLabel(parent=self.onglet_popup_3)
        self.label_popup_3.setGeometry(QtCore.QRect(10, 10, 211, 16))
        self.label_popup_3.setObjectName("label_popup_3")
        self.text_popup_3 = QtWidgets.QPlainTextEdit(parent=self.onglet_popup_3)
        self.text_popup_3.setGeometry(QtCore.QRect(10, 40, 811, 241))
        self.text_popup_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_popup_3.setObjectName("text_popup_3")
        self.onglet_popup.addTab(self.onglet_popup_3, "")
        self.onglet_popup_4 = QtWidgets.QWidget()
        self.onglet_popup_4.setObjectName("onglet_popup_4")
        self.label_16 = QtWidgets.QLabel(parent=self.onglet_popup_4)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 301, 16))
        self.label_16.setObjectName("label_16")
        self.text_popup_4 = QtWidgets.QPlainTextEdit(parent=self.onglet_popup_4)
        self.text_popup_4.setGeometry(QtCore.QRect(10, 40, 811, 241))
        self.text_popup_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text_popup_4.setObjectName("text_popup_4")
        self.onglet_popup.addTab(self.onglet_popup_4, "")
        self.onglet.addTab(self.textes, "")
        self.style = QtWidgets.QWidget()
        self.style.setObjectName("style")
        self.aide_style = QtWidgets.QPushButton(parent=self.style)
        self.aide_style.setGeometry(QtCore.QRect(760, 10, 75, 24))
        self.aide_style.setObjectName("aide_style")
        self.label = QtWidgets.QLabel(parent=self.style)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 16))
        self.label.setObjectName("label")
        self.largeur_popup = QtWidgets.QLineEdit(parent=self.style)
        self.largeur_popup.setGeometry(QtCore.QRect(150, 20, 113, 21))
        self.largeur_popup.setObjectName("largeur_popup")
        self.label_2 = QtWidgets.QLabel(parent=self.style)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 49, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.style)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 121, 16))
        self.label_3.setObjectName("label_3")
        self.hauteur_popup = QtWidgets.QLineEdit(parent=self.style)
        self.hauteur_popup.setGeometry(QtCore.QRect(150, 60, 113, 21))
        self.hauteur_popup.setObjectName("hauteur_popup")
        self.label_4 = QtWidgets.QLabel(parent=self.style)
        self.label_4.setGeometry(QtCore.QRect(270, 60, 49, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.style)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 121, 16))
        self.label_5.setObjectName("label_5")
        self.police = QtWidgets.QComboBox(parent=self.style)
        self.police.setGeometry(QtCore.QRect(150, 100, 171, 22))
        self.police.setObjectName("police")
        self.label_6 = QtWidgets.QLabel(parent=self.style)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 171, 16))
        self.label_6.setObjectName("label_6")
        self.taille_police = QtWidgets.QLineEdit(parent=self.style)
        self.taille_police.setGeometry(QtCore.QRect(190, 140, 71, 21))
        self.taille_police.setObjectName("taille_police")
        self.label_7 = QtWidgets.QLabel(parent=self.style)
        self.label_7.setGeometry(QtCore.QRect(270, 140, 49, 16))
        self.label_7.setObjectName("label_7")
        self.onglet.addTab(self.style, "")
        self.temps = QtWidgets.QWidget()
        self.temps.setObjectName("temps")
        self.aide_temps = QtWidgets.QPushButton(parent=self.temps)
        self.aide_temps.setGeometry(QtCore.QRect(760, 10, 75, 24))
        self.aide_temps.setObjectName("aide_temps")
        self.label_8 = QtWidgets.QLabel(parent=self.temps)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 271, 16))
        self.label_8.setObjectName("label_8")
        self.delai_fermeture = QtWidgets.QLineEdit(parent=self.temps)
        self.delai_fermeture.setGeometry(QtCore.QRect(290, 20, 51, 21))
        self.delai_fermeture.setObjectName("delai_fermeture")
        self.label_9 = QtWidgets.QLabel(parent=self.temps)
        self.label_9.setGeometry(QtCore.QRect(350, 20, 61, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.temps)
        self.label_10.setGeometry(QtCore.QRect(20, 60, 231, 16))
        self.label_10.setObjectName("label_10")
        self.duree_session = QtWidgets.QLineEdit(parent=self.temps)
        self.duree_session.setGeometry(QtCore.QRect(220, 60, 51, 21))
        self.duree_session.setObjectName("duree_session")
        self.label_11 = QtWidgets.QLabel(parent=self.temps)
        self.label_11.setGeometry(QtCore.QRect(280, 60, 49, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.temps)
        self.label_12.setGeometry(QtCore.QRect(20, 100, 241, 16))
        self.label_12.setObjectName("label_12")
        self.timer_second_popup = QtWidgets.QLineEdit(parent=self.temps)
        self.timer_second_popup.setGeometry(QtCore.QRect(260, 100, 51, 21))
        self.timer_second_popup.setObjectName("timer_second_popup")
        self.label_13 = QtWidgets.QLabel(parent=self.temps)
        self.label_13.setGeometry(QtCore.QRect(320, 100, 49, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.temps)
        self.label_14.setGeometry(QtCore.QRect(20, 180, 391, 16))
        self.label_14.setObjectName("label_14")
        self.timer_dernier_popup = QtWidgets.QLineEdit(parent=self.temps)
        self.timer_dernier_popup.setGeometry(QtCore.QRect(410, 180, 51, 21))
        self.timer_dernier_popup.setObjectName("timer_dernier_popup")
        self.label_15 = QtWidgets.QLabel(parent=self.temps)
        self.label_15.setGeometry(QtCore.QRect(470, 180, 49, 16))
        self.label_15.setObjectName("label_15")
        self.label_19 = QtWidgets.QLabel(parent=self.temps)
        self.label_19.setGeometry(QtCore.QRect(20, 140, 311, 16))
        self.label_19.setObjectName("label_19")
        self.timer_troisieme_popup = QtWidgets.QLineEdit(parent=self.temps)
        self.timer_troisieme_popup.setGeometry(QtCore.QRect(330, 140, 51, 21))
        self.timer_troisieme_popup.setObjectName("timer_troisieme_popup")
        self.label_20 = QtWidgets.QLabel(parent=self.temps)
        self.label_20.setGeometry(QtCore.QRect(390, 140, 49, 16))
        self.label_20.setObjectName("label_20")
        self.onglet.addTab(self.temps, "")
        self.gestion = QtWidgets.QWidget()
        self.gestion.setObjectName("gestion")
        self.aide_gestion = QtWidgets.QPushButton(parent=self.gestion)
        self.aide_gestion.setGeometry(QtCore.QRect(760, 10, 75, 24))
        self.aide_gestion.setObjectName("aide_gestion")
        self.label_17 = QtWidgets.QLabel(parent=self.gestion)
        self.label_17.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.label_17.setObjectName("label_17")
        self.fermeture_session = QtWidgets.QComboBox(parent=self.gestion)
        self.fermeture_session.setGeometry(QtCore.QRect(190, 20, 161, 22))
        self.fermeture_session.setObjectName("fermeture_session")
        self.activation_fermeture = QtWidgets.QCheckBox(parent=self.gestion)
        self.activation_fermeture.setGeometry(QtCore.QRect(20, 60, 361, 20))
        self.activation_fermeture.setObjectName("activation_fermeture")
        self.onglet.addTab(self.gestion, "")
        self.Enregistrer = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Enregistrer.setGeometry(QtCore.QRect(270, 400, 101, 31))
        self.Enregistrer.setObjectName("Enregistrer")
        self.annuler = QtWidgets.QPushButton(parent=self.centralwidget)
        self.annuler.setGeometry(QtCore.QRect(500, 400, 81, 31))
        self.annuler.setObjectName("annuler")
        Configuration.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Configuration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 22))
        self.menubar.setObjectName("menubar")
        self.menuConfiguration = QtWidgets.QMenu(parent=self.menubar)
        self.menuConfiguration.setObjectName("menuConfiguration")
        Configuration.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Configuration)
        self.statusbar.setObjectName("statusbar")
        Configuration.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuConfiguration.menuAction())

        self.retranslateUi(Configuration)
        self.onglet.setCurrentIndex(0)
        self.onglet_popup.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Configuration)

    def retranslateUi(self, Configuration):
        _translate = QtCore.QCoreApplication.translate
        Configuration.setWindowTitle(_translate("Configuration", "MainWindow"))
        self.session_activation.setText(_translate("Configuration", "Activer Session Manager sur l\'ordinateur pour l\'utilisateur visé."))
        self.aide_accueil.setText(_translate("Configuration", "Aide"))
        self.retour_activation.setText(_translate("Configuration", "Résultat de la création du raccourci dans le dossier Démarrage ..."))
        self.user_session.setText(_translate("Configuration", "Choix de l\'utilisateur visé :"))
        self.gpupdate.setText(_translate("Configuration", "Recharger les stratégies de groupe locales"))
        self.retour_gpupdate.setText(_translate("Configuration", "Résultat du rechargement des stratégies de groupe ..."))
        self.onglet.setTabText(self.onglet.indexOf(self.accueil), _translate("Configuration", "Accueil"))
        self.fiche_activation.setText(_translate("Configuration", "Activer la fiche d\'entrée demandant les informations personnelles"))
        self.fiche_log.setText(_translate("Configuration", "Stocker les informations données dans un document excel"))
        self.Informations.setTitle(_translate("Configuration", "Gestion des champs de la fiche d\'entrée"))
        self.ajouter_champ.setText(_translate("Configuration", "Ajouter un champ"))
        self.supprimer_champ.setText(_translate("Configuration", "Supprimer un champ"))
        self.fiche_afficher.setText(_translate("Configuration", "Afficher la fenêtre de la fiche d\'entrée"))
        self.aide_fiche.setText(_translate("Configuration", "Aide"))
        self.fiche_1h.setText(_translate("Configuration", "1 heure"))
        self.fiche_duree_session.setText(_translate("Configuration", "Durée des sessions possibles"))
        self.fiche_15min.setText(_translate("Configuration", "15 minutes"))
        self.fiche_30min.setText(_translate("Configuration", "30 minutes"))
        self.onglet.setTabText(self.onglet.indexOf(self.formulaire), _translate("Configuration", "Fiche d\'entrée"))
        self.aide_titres.setText(_translate("Configuration", "Aide"))
        self.label_titre_1.setText(_translate("Configuration", "Titre du premier popup :"))
        self.label_titre_2.setText(_translate("Configuration", "Titre du second popup :"))
        self.label_titre__3.setText(_translate("Configuration", "Titre du troisième popup :"))
        self.label_18.setText(_translate("Configuration", "Titre fenêtre de fermeture :"))
        self.label_21.setText(_translate("Configuration", "Titre fenêtre règlement :"))
        self.onglet.setTabText(self.onglet.indexOf(self.titres), _translate("Configuration", "Titres"))
        self.aide_textes.setText(_translate("Configuration", "Aide"))
        self.label_text_1.setText(_translate("Configuration", "Texte affiché dans le premier popup :"))
        self.onglet_popup.setTabText(self.onglet_popup.indexOf(self.onglet_popup_1), _translate("Configuration", "Premier popup"))
        self.label_text_2.setText(_translate("Configuration", "Texte affiché dans le second popup :"))
        self.onglet_popup.setTabText(self.onglet_popup.indexOf(self.onglet_popup_2), _translate("Configuration", "Second popup"))
        self.label_popup_3.setText(_translate("Configuration", "Texte affiché dans le troisième popup :"))
        self.onglet_popup.setTabText(self.onglet_popup.indexOf(self.onglet_popup_3), _translate("Configuration", "Troisième popup"))
        self.label_16.setText(_translate("Configuration", "Texte affiché dans le popup de fermeture de session :"))
        self.onglet_popup.setTabText(self.onglet_popup.indexOf(self.onglet_popup_4), _translate("Configuration", "Popup de femerture"))
        self.onglet.setTabText(self.onglet.indexOf(self.textes), _translate("Configuration", "Textes"))
        self.aide_style.setText(_translate("Configuration", "Aide"))
        self.label.setText(_translate("Configuration", "Largeur des popups :"))
        self.label_2.setText(_translate("Configuration", "pixels"))
        self.label_3.setText(_translate("Configuration", "Hauteur des popups :"))
        self.label_4.setText(_translate("Configuration", "pixels"))
        self.label_5.setText(_translate("Configuration", "Police de caractères :"))
        self.label_6.setText(_translate("Configuration", "Taille de la police de caractère :"))
        self.label_7.setText(_translate("Configuration", "pixels"))
        self.onglet.setTabText(self.onglet.indexOf(self.style), _translate("Configuration", "Style"))
        self.aide_temps.setText(_translate("Configuration", "Aide"))
        self.label_8.setText(_translate("Configuration", "Délai avant fermetures automatique d\'un popup :"))
        self.label_9.setText(_translate("Configuration", "secondes"))
        self.label_10.setText(_translate("Configuration", "Durée totale de la session utilisateur :"))
        self.label_11.setText(_translate("Configuration", "minutes"))
        self.label_12.setText(_translate("Configuration", "Délai avant ouverture de la seconde popup :"))
        self.label_13.setText(_translate("Configuration", "minutes"))
        self.label_14.setText(_translate("Configuration", "Durée d\'ouverture de la dernière popup avant la fermeture de la session :"))
        self.label_15.setText(_translate("Configuration", "secondes"))
        self.label_19.setText(_translate("Configuration", "Délai entre la troisième popup et la fermeture de session :"))
        self.label_20.setText(_translate("Configuration", "minutes"))
        self.onglet.setTabText(self.onglet.indexOf(self.temps), _translate("Configuration", "Temps"))
        self.aide_gestion.setText(_translate("Configuration", "Aide"))
        self.label_17.setText(_translate("Configuration", "Type de fermeture de session :"))
        self.activation_fermeture.setText(_translate("Configuration", "Activer le popup bloqué, plein écran, à la fermeture de la session"))
        self.onglet.setTabText(self.onglet.indexOf(self.gestion), _translate("Configuration", "Gestion sessions"))
        self.Enregistrer.setText(_translate("Configuration", "Enregistrer"))
        self.annuler.setText(_translate("Configuration", "Annuler"))
        self.menuConfiguration.setTitle(_translate("Configuration", "Configuration"))
