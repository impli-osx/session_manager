# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuration.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QWidget)

class Ui_Configuration(object):
    def setupUi(self, Configuration):
        if not Configuration.objectName():
            Configuration.setObjectName(u"Configuration")
        Configuration.resize(868, 478)
        self.centralwidget = QWidget(Configuration)
        self.centralwidget.setObjectName(u"centralwidget")
        self.onglet = QTabWidget(self.centralwidget)
        self.onglet.setObjectName(u"onglet")
        self.onglet.setGeometry(QRect(10, 10, 851, 381))
        self.accueil = QWidget()
        self.accueil.setObjectName(u"accueil")
        self.session_activation = QCheckBox(self.accueil)
        self.session_activation.setObjectName(u"session_activation")
        self.session_activation.setGeometry(QRect(20, 60, 361, 31))
        self.aide_accueil = QPushButton(self.accueil)
        self.aide_accueil.setObjectName(u"aide_accueil")
        self.aide_accueil.setGeometry(QRect(760, 10, 75, 24))
        self.retour_activation = QLabel(self.accueil)
        self.retour_activation.setObjectName(u"retour_activation")
        self.retour_activation.setGeometry(QRect(30, 100, 791, 71))
        self.session_user = QComboBox(self.accueil)
        self.session_user.setObjectName(u"session_user")
        self.session_user.setGeometry(QRect(170, 20, 141, 22))
        self.user_session = QLabel(self.accueil)
        self.user_session.setObjectName(u"user_session")
        self.user_session.setGeometry(QRect(20, 20, 151, 16))
        self.gpupdate = QPushButton(self.accueil)
        self.gpupdate.setObjectName(u"gpupdate")
        self.gpupdate.setGeometry(QRect(20, 180, 301, 24))
        self.retour_gpupdate = QLabel(self.accueil)
        self.retour_gpupdate.setObjectName(u"retour_gpupdate")
        self.retour_gpupdate.setGeometry(QRect(30, 220, 791, 121))
        self.retour_gpupdate.setMargin(5)
        self.onglet.addTab(self.accueil, "")
        self.formulaire = QWidget()
        self.formulaire.setObjectName(u"formulaire")
        self.fiche_activation = QCheckBox(self.formulaire)
        self.fiche_activation.setObjectName(u"fiche_activation")
        self.fiche_activation.setGeometry(QRect(20, 20, 491, 20))
        self.fiche_log = QCheckBox(self.formulaire)
        self.fiche_log.setObjectName(u"fiche_log")
        self.fiche_log.setGeometry(QRect(20, 60, 491, 20))
        self.Informations = QGroupBox(self.formulaire)
        self.Informations.setObjectName(u"Informations")
        self.Informations.setGeometry(QRect(10, 250, 821, 71))
        self.ajouter_champ = QPushButton(self.Informations)
        self.ajouter_champ.setObjectName(u"ajouter_champ")
        self.ajouter_champ.setGeometry(QRect(10, 30, 141, 24))
        self.supprimer_champ = QPushButton(self.Informations)
        self.supprimer_champ.setObjectName(u"supprimer_champ")
        self.supprimer_champ.setGeometry(QRect(420, 30, 141, 24))
        self.fiche_afficher = QPushButton(self.Informations)
        self.fiche_afficher.setObjectName(u"fiche_afficher")
        self.fiche_afficher.setGeometry(QRect(580, 30, 231, 24))
        self.modifier_ordre = QPushButton(self.Informations)
        self.modifier_ordre.setObjectName(u"modifier_ordre")
        self.modifier_ordre.setGeometry(QRect(170, 30, 231, 24))
        self.aide_fiche = QPushButton(self.formulaire)
        self.aide_fiche.setObjectName(u"aide_fiche")
        self.aide_fiche.setGeometry(QRect(760, 10, 75, 24))
        self.fiche_1h = QCheckBox(self.formulaire)
        self.fiche_1h.setObjectName(u"fiche_1h")
        self.fiche_1h.setGeometry(QRect(50, 190, 75, 20))
        self.fiche_duree_session = QCheckBox(self.formulaire)
        self.fiche_duree_session.setObjectName(u"fiche_duree_session")
        self.fiche_duree_session.setGeometry(QRect(20, 100, 341, 20))
        self.fiche_15min = QCheckBox(self.formulaire)
        self.fiche_15min.setObjectName(u"fiche_15min")
        self.fiche_15min.setGeometry(QRect(50, 130, 221, 20))
        self.fiche_30min = QCheckBox(self.formulaire)
        self.fiche_30min.setObjectName(u"fiche_30min")
        self.fiche_30min.setGeometry(QRect(50, 160, 181, 20))
        self.onglet.addTab(self.formulaire, "")
        self.textes = QWidget()
        self.textes.setObjectName(u"textes")
        self.aide_textes = QPushButton(self.textes)
        self.aide_textes.setObjectName(u"aide_textes")
        self.aide_textes.setGeometry(QRect(760, 10, 75, 24))
        self.onglet_popup = QTabWidget(self.textes)
        self.onglet_popup.setObjectName(u"onglet_popup")
        self.onglet_popup.setGeometry(QRect(10, 40, 831, 311))
        self.onglet_popup_1 = QWidget()
        self.onglet_popup_1.setObjectName(u"onglet_popup_1")
        self.label_text_1 = QLabel(self.onglet_popup_1)
        self.label_text_1.setObjectName(u"label_text_1")
        self.label_text_1.setGeometry(QRect(10, 10, 211, 16))
        self.text_popup_1 = QPlainTextEdit(self.onglet_popup_1)
        self.text_popup_1.setObjectName(u"text_popup_1")
        self.text_popup_1.setGeometry(QRect(10, 40, 811, 241))
        self.text_popup_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.onglet_popup.addTab(self.onglet_popup_1, "")
        self.onglet_popup_2 = QWidget()
        self.onglet_popup_2.setObjectName(u"onglet_popup_2")
        self.label_text_2 = QLabel(self.onglet_popup_2)
        self.label_text_2.setObjectName(u"label_text_2")
        self.label_text_2.setGeometry(QRect(10, 10, 301, 16))
        self.text_popup_2 = QPlainTextEdit(self.onglet_popup_2)
        self.text_popup_2.setObjectName(u"text_popup_2")
        self.text_popup_2.setGeometry(QRect(10, 40, 811, 241))
        self.text_popup_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.onglet_popup.addTab(self.onglet_popup_2, "")
        self.onglet_popup_3 = QWidget()
        self.onglet_popup_3.setObjectName(u"onglet_popup_3")
        self.label_popup_3 = QLabel(self.onglet_popup_3)
        self.label_popup_3.setObjectName(u"label_popup_3")
        self.label_popup_3.setGeometry(QRect(10, 10, 211, 16))
        self.text_popup_3 = QPlainTextEdit(self.onglet_popup_3)
        self.text_popup_3.setObjectName(u"text_popup_3")
        self.text_popup_3.setGeometry(QRect(10, 40, 811, 241))
        self.text_popup_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.onglet_popup.addTab(self.onglet_popup_3, "")
        self.onglet_popup_4 = QWidget()
        self.onglet_popup_4.setObjectName(u"onglet_popup_4")
        self.label_16 = QLabel(self.onglet_popup_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 10, 301, 16))
        self.text_fermeture = QPlainTextEdit(self.onglet_popup_4)
        self.text_fermeture.setObjectName(u"text_fermeture")
        self.text_fermeture.setGeometry(QRect(10, 40, 811, 241))
        self.text_fermeture.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.onglet_popup.addTab(self.onglet_popup_4, "")
        self.onglet.addTab(self.textes, "")
        self.style = QWidget()
        self.style.setObjectName(u"style")
        self.aide_style = QPushButton(self.style)
        self.aide_style.setObjectName(u"aide_style")
        self.aide_style.setGeometry(QRect(760, 10, 75, 24))
        self.groupBox = QGroupBox(self.style)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 40, 321, 111))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 70, 49, 16))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 51, 16))
        self.hauteur_popup = QLineEdit(self.groupBox)
        self.hauteur_popup.setObjectName(u"hauteur_popup")
        self.hauteur_popup.setGeometry(QRect(80, 70, 51, 21))
        self.largeur_popup = QLineEdit(self.groupBox)
        self.largeur_popup.setObjectName(u"largeur_popup")
        self.largeur_popup.setGeometry(QRect(80, 30, 51, 21))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 30, 49, 16))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 70, 51, 16))
        self.groupBox_2 = QGroupBox(self.style)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 170, 321, 101))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 30, 101, 16))
        self.taille_police = QLineEdit(self.groupBox_2)
        self.taille_police.setObjectName(u"taille_police")
        self.taille_police.setGeometry(QRect(120, 30, 41, 21))
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 30, 49, 16))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 60, 121, 16))
        self.police = QComboBox(self.groupBox_2)
        self.police.setObjectName(u"police")
        self.police.setGeometry(QRect(140, 60, 171, 22))
        self.groupBox_3 = QGroupBox(self.style)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(370, 40, 381, 301))
        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 30, 161, 16))
        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 70, 171, 16))
        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(20, 110, 151, 16))
        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(20, 150, 161, 16))
        self.couleur_fond = QLineEdit(self.groupBox_3)
        self.couleur_fond.setObjectName(u"couleur_fond")
        self.couleur_fond.setGeometry(QRect(190, 30, 71, 21))
        self.couleur_texte = QLineEdit(self.groupBox_3)
        self.couleur_texte.setObjectName(u"couleur_texte")
        self.couleur_texte.setGeometry(QRect(190, 70, 71, 21))
        self.couleur_bouton = QLineEdit(self.groupBox_3)
        self.couleur_bouton.setObjectName(u"couleur_bouton")
        self.couleur_bouton.setGeometry(QRect(190, 110, 71, 21))
        self.couleur_bouton_texte = QLineEdit(self.groupBox_3)
        self.couleur_bouton_texte.setObjectName(u"couleur_bouton_texte")
        self.couleur_bouton_texte.setGeometry(QRect(190, 150, 71, 21))
        self.mod_fond = QPushButton(self.groupBox_3)
        self.mod_fond.setObjectName(u"mod_fond")
        self.mod_fond.setGeometry(QRect(270, 30, 75, 24))
        self.mod_texte = QPushButton(self.groupBox_3)
        self.mod_texte.setObjectName(u"mod_texte")
        self.mod_texte.setGeometry(QRect(270, 70, 75, 24))
        self.mod_bouton = QPushButton(self.groupBox_3)
        self.mod_bouton.setObjectName(u"mod_bouton")
        self.mod_bouton.setGeometry(QRect(270, 110, 75, 24))
        self.mod_bouton_texte = QPushButton(self.groupBox_3)
        self.mod_bouton_texte.setObjectName(u"mod_bouton_texte")
        self.mod_bouton_texte.setGeometry(QRect(270, 150, 75, 24))
        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 190, 161, 16))
        self.couleur_bouton_survol = QLineEdit(self.groupBox_3)
        self.couleur_bouton_survol.setObjectName(u"couleur_bouton_survol")
        self.couleur_bouton_survol.setGeometry(QRect(190, 190, 71, 21))
        self.mod_bouton_survol = QPushButton(self.groupBox_3)
        self.mod_bouton_survol.setObjectName(u"mod_bouton_survol")
        self.mod_bouton_survol.setGeometry(QRect(270, 190, 75, 24))
        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(20, 230, 171, 16))
        self.texte_bouton = QLineEdit(self.groupBox_3)
        self.texte_bouton.setObjectName(u"texte_bouton")
        self.texte_bouton.setGeometry(QRect(190, 230, 171, 21))
        self.previsu_popup = QPushButton(self.groupBox_3)
        self.previsu_popup.setObjectName(u"previsu_popup")
        self.previsu_popup.setGeometry(QRect(120, 270, 151, 24))
        self.onglet.addTab(self.style, "")
        self.temps = QWidget()
        self.temps.setObjectName(u"temps")
        self.aide_temps = QPushButton(self.temps)
        self.aide_temps.setObjectName(u"aide_temps")
        self.aide_temps.setGeometry(QRect(760, 10, 75, 24))
        self.label_8 = QLabel(self.temps)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 20, 271, 16))
        self.delai_fermeture = QLineEdit(self.temps)
        self.delai_fermeture.setObjectName(u"delai_fermeture")
        self.delai_fermeture.setGeometry(QRect(290, 20, 51, 21))
        self.label_9 = QLabel(self.temps)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(350, 20, 61, 16))
        self.label_10 = QLabel(self.temps)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 60, 231, 16))
        self.duree_session = QLineEdit(self.temps)
        self.duree_session.setObjectName(u"duree_session")
        self.duree_session.setGeometry(QRect(220, 60, 51, 21))
        self.label_11 = QLabel(self.temps)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(280, 60, 49, 16))
        self.label_12 = QLabel(self.temps)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 100, 391, 16))
        self.timer_popup_1 = QLineEdit(self.temps)
        self.timer_popup_1.setObjectName(u"timer_popup_1")
        self.timer_popup_1.setGeometry(QRect(410, 100, 51, 21))
        self.label_13 = QLabel(self.temps)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(470, 100, 49, 16))
        self.label_14 = QLabel(self.temps)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 180, 421, 16))
        self.timer_popup_3 = QLineEdit(self.temps)
        self.timer_popup_3.setObjectName(u"timer_popup_3")
        self.timer_popup_3.setGeometry(QRect(440, 180, 51, 21))
        self.label_15 = QLabel(self.temps)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(500, 180, 49, 16))
        self.label_19 = QLabel(self.temps)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 140, 411, 16))
        self.timer_popup_2 = QLineEdit(self.temps)
        self.timer_popup_2.setObjectName(u"timer_popup_2")
        self.timer_popup_2.setGeometry(QRect(430, 140, 51, 21))
        self.label_20 = QLabel(self.temps)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(490, 140, 49, 16))
        self.onglet.addTab(self.temps, "")
        self.gestion = QWidget()
        self.gestion.setObjectName(u"gestion")
        self.aide_gestion = QPushButton(self.gestion)
        self.aide_gestion.setObjectName(u"aide_gestion")
        self.aide_gestion.setGeometry(QRect(760, 10, 75, 24))
        self.label_17 = QLabel(self.gestion)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 20, 171, 16))
        self.fermeture_session = QComboBox(self.gestion)
        self.fermeture_session.setObjectName(u"fermeture_session")
        self.fermeture_session.setGeometry(QRect(190, 20, 161, 22))
        self.activation_fermeture = QCheckBox(self.gestion)
        self.activation_fermeture.setObjectName(u"activation_fermeture")
        self.activation_fermeture.setGeometry(QRect(20, 60, 441, 20))
        self.onglet.addTab(self.gestion, "")
        self.Enregistrer = QPushButton(self.centralwidget)
        self.Enregistrer.setObjectName(u"Enregistrer")
        self.Enregistrer.setGeometry(QRect(270, 400, 101, 31))
        self.annuler = QPushButton(self.centralwidget)
        self.annuler.setObjectName(u"annuler")
        self.annuler.setGeometry(QRect(500, 400, 81, 31))
        Configuration.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Configuration)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 868, 22))
        self.menuConfiguration = QMenu(self.menubar)
        self.menuConfiguration.setObjectName(u"menuConfiguration")
        Configuration.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Configuration)
        self.statusbar.setObjectName(u"statusbar")
        Configuration.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuConfiguration.menuAction())

        self.retranslateUi(Configuration)

        self.onglet.setCurrentIndex(3)
        self.onglet_popup.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Configuration)
    # setupUi

    def retranslateUi(self, Configuration):
        Configuration.setWindowTitle(QCoreApplication.translate("Configuration", u"MainWindow", None))
        self.session_activation.setText(QCoreApplication.translate("Configuration", u"Activer Session Manager sur l'ordinateur pour l'utilisateur vis\u00e9.", None))
        self.aide_accueil.setText(QCoreApplication.translate("Configuration", u"Aide", None))
        self.retour_activation.setText(QCoreApplication.translate("Configuration", u"R\u00e9sultat de la cr\u00e9ation du raccourci dans le dossier D\u00e9marrage ...", None))
        self.user_session.setText(QCoreApplication.translate("Configuration", u"Choix de l'utilisateur vis\u00e9 :", None))
        self.gpupdate.setText(QCoreApplication.translate("Configuration", u"Recharger les strat\u00e9gies de groupe locales", None))
        self.retour_gpupdate.setText(QCoreApplication.translate("Configuration", u"R\u00e9sultat du rechargement des strat\u00e9gies de groupe ...", None))
        self.onglet.setTabText(self.onglet.indexOf(self.accueil), QCoreApplication.translate("Configuration", u"Accueil", None))
        self.fiche_activation.setText(QCoreApplication.translate("Configuration", u"Activer la fiche d'entr\u00e9e demandant les informations personnelles", None))
        self.fiche_log.setText(QCoreApplication.translate("Configuration", u"Stocker les informations donn\u00e9es dans un document excel", None))
        self.Informations.setTitle(QCoreApplication.translate("Configuration", u"Gestion des champs de la fiche d'entr\u00e9e", None))
        self.ajouter_champ.setText(QCoreApplication.translate("Configuration", u"Ajouter des champs", None))
        self.supprimer_champ.setText(QCoreApplication.translate("Configuration", u"Supprimer des champs", None))
        self.fiche_afficher.setText(QCoreApplication.translate("Configuration", u"Afficher la fen\u00eatre de la fiche d'entr\u00e9e", None))
        self.modifier_ordre.setText(QCoreApplication.translate("Configuration", u"Modifier l'ordre d'affichage des champs", None))
        self.aide_fiche.setText(QCoreApplication.translate("Configuration", u"Aide", None))
        self.fiche_1h.setText(QCoreApplication.translate("Configuration", u"1 heure", None))
        self.fiche_duree_session.setText(QCoreApplication.translate("Configuration", u"Choix des dur\u00e9es des sessions possibles :", None))
        self.fiche_15min.setText(QCoreApplication.translate("Configuration", u"15 minutes", None))
        self.fiche_30min.setText(QCoreApplication.translate("Configuration", u"30 minutes", None))
        self.onglet.setTabText(self.onglet.indexOf(self.formulaire), QCoreApplication.translate("Configuration", u"Fiche d'entr\u00e9e", None))
        self.aide_textes.setText(QCoreApplication.translate("Configuration", u"Aide", None))
        self.label_text_1.setText(QCoreApplication.translate("Configuration", u"Texte affich\u00e9 dans la premi\u00e8re fen\u00eatre :", None))
        self.onglet_popup.setTabText(self.onglet_popup.indexOf(self.onglet_popup_1), QCoreApplication.translate("Configuration", u"Premi\u00e8re fen\u00eatre", None))
        self.label_text_2.setText(QCoreApplication.translate("Configuration", u"Texte affich\u00e9 dans la seconde fen\u00eatre :", None))
        self.onglet_popup.setTabText(self.onglet_popup.indexOf(self.onglet_popup_2), QCoreApplication.translate("Configuration", u"Seconde fen\u00eatre", None))
        self.label_popup_3.setText(QCoreApplication.translate("Configuration", u"Texte affich\u00e9 dans la troisi\u00e8me fen\u00eatre :", None))
        self.onglet_popup.setTabText(self.onglet_popup.indexOf(self.onglet_popup_3), QCoreApplication.translate("Configuration", u"Troisi\u00e8me fen\u00eatre", None))
        self.label_16.setText(QCoreApplication.translate("Configuration", u"Texte affich\u00e9 dans la fen\u00eatre de fermeture de session :", None))
        self.onglet_popup.setTabText(self.onglet_popup.indexOf(self.onglet_popup_4), QCoreApplication.translate("Configuration", u"Fen\u00eatre de femerture", None))
        self.onglet.setTabText(self.onglet.indexOf(self.textes), QCoreApplication.translate("Configuration", u"Textes", None))
        self.aide_style.setText(QCoreApplication.translate("Configuration", u"Aide", None))
        self.groupBox.setTitle(QCoreApplication.translate("Configuration", u"Dimensions de la fen\u00eatre", None))
        self.label_4.setText(QCoreApplication.translate("Configuration", u"pixels", None))
        self.label.setText(QCoreApplication.translate("Configuration", u"Largeur :", None))
        self.label_2.setText(QCoreApplication.translate("Configuration", u"pixels", None))
        self.label_3.setText(QCoreApplication.translate("Configuration", u"Hauteur :", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Configuration", u"Police de caract\u00e8re", None))
        self.label_6.setText(QCoreApplication.translate("Configuration", u"Taille de la police  :", None))
        self.label_7.setText(QCoreApplication.translate("Configuration", u"pixels", None))
        self.label_5.setText(QCoreApplication.translate("Configuration", u"Police de caract\u00e8res :", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Configuration", u"Couleurs de la fen\u00eatre", None))
        self.label_22.setText(QCoreApplication.translate("Configuration", u"Couleur du fond de la fen\u00eatre :", None))
        self.label_23.setText(QCoreApplication.translate("Configuration", u"Couleur du texte de la fen\u00eatre :", None))
        self.label_24.setText(QCoreApplication.translate("Configuration", u"Couleur du bouton valider :", None))
        self.label_25.setText(QCoreApplication.translate("Configuration", u"Couleur du texte du bouton :", None))
        self.mod_fond.setText(QCoreApplication.translate("Configuration", u"Modifier", None))
        self.mod_texte.setText(QCoreApplication.translate("Configuration", u"Modifier", None))
        self.mod_bouton.setText(QCoreApplication.translate("Configuration", u"Modifier", None))
        self.mod_bouton_texte.setText(QCoreApplication.translate("Configuration", u"Modifier", None))
        self.label_18.setText(QCoreApplication.translate("Configuration", u"Couleur du bouton au survol :", None))
        self.mod_bouton_survol.setText(QCoreApplication.translate("Configuration", u"Modifier", None))
        self.label_21.setText(QCoreApplication.translate("Configuration", u"Texte du bouton de validation :", None))
        self.previsu_popup.setText(QCoreApplication.translate("Configuration", u"Pr\u00e9visualiser la fen\u00eatre", None))
        self.onglet.setTabText(self.onglet.indexOf(self.style), QCoreApplication.translate("Configuration", u"Style", None))
        self.aide_temps.setText(QCoreApplication.translate("Configuration", u"Aide", None))
        self.label_8.setText(QCoreApplication.translate("Configuration", u"D\u00e9lai avant fermeture automatique d'une fen\u00eatre :", None))
        self.label_9.setText(QCoreApplication.translate("Configuration", u"secondes", None))
        self.label_10.setText(QCoreApplication.translate("Configuration", u"Dur\u00e9e totale de la session utilisateur :", None))
        self.label_11.setText(QCoreApplication.translate("Configuration", u"minutes", None))
        self.label_12.setText(QCoreApplication.translate("Configuration", u"D\u00e9lai entre l'ouverture de la session et l'affichage de la premi\u00e8re fen\u00eatre :", None))
        self.label_13.setText(QCoreApplication.translate("Configuration", u"minutes", None))
        self.label_14.setText(QCoreApplication.translate("Configuration", u"Dur\u00e9e d'affichage entre la fen\u00eatre de fermeture et l'interruption de la session :", None))
        self.label_15.setText(QCoreApplication.translate("Configuration", u"secondes", None))
        self.label_19.setText(QCoreApplication.translate("Configuration", u"D\u00e9lai entre l'affichage de la seconde fen\u00eatre et de la fermeture de la session : ", None))
        self.label_20.setText(QCoreApplication.translate("Configuration", u"minutes", None))
        self.onglet.setTabText(self.onglet.indexOf(self.temps), QCoreApplication.translate("Configuration", u"Temps", None))
        self.aide_gestion.setText(QCoreApplication.translate("Configuration", u"Aide", None))
        self.label_17.setText(QCoreApplication.translate("Configuration", u"Type de fermeture de session :", None))
        self.activation_fermeture.setText(QCoreApplication.translate("Configuration", u"Activer la fen\u00eatre de fermeture, plein \u00e9cran, avant l'interruption de la session", None))
        self.onglet.setTabText(self.onglet.indexOf(self.gestion), QCoreApplication.translate("Configuration", u"Gestion sessions", None))
        self.Enregistrer.setText(QCoreApplication.translate("Configuration", u"Enregistrer", None))
        self.annuler.setText(QCoreApplication.translate("Configuration", u"Annuler", None))
        self.menuConfiguration.setTitle(QCoreApplication.translate("Configuration", u"Configuration", None))
    # retranslateUi

