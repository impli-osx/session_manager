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
        self.retour_activation.setGeometry(QRect(40, 100, 791, 21))
        self.session_user = QComboBox(self.accueil)
        self.session_user.setObjectName(u"session_user")
        self.session_user.setGeometry(QRect(170, 20, 141, 22))
        self.user_session = QLabel(self.accueil)
        self.user_session.setObjectName(u"user_session")
        self.user_session.setGeometry(QRect(20, 20, 151, 16))
        self.gpupdate = QPushButton(self.accueil)
        self.gpupdate.setObjectName(u"gpupdate")
        self.gpupdate.setGeometry(QRect(20, 140, 301, 24))
        self.retour_gpupdate = QLabel(self.accueil)
        self.retour_gpupdate.setObjectName(u"retour_gpupdate")
        self.retour_gpupdate.setGeometry(QRect(40, 180, 771, 161))
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
        self.Informations.setGeometry(QRect(10, 100, 821, 241))
        self.fiche_nom = QCheckBox(self.Informations)
        self.fiche_nom.setObjectName(u"fiche_nom")
        self.fiche_nom.setGeometry(QRect(20, 40, 181, 20))
        self.fiche_mail = QCheckBox(self.Informations)
        self.fiche_mail.setObjectName(u"fiche_mail")
        self.fiche_mail.setGeometry(QRect(20, 80, 221, 20))
        self.fiche_adresse = QCheckBox(self.Informations)
        self.fiche_adresse.setObjectName(u"fiche_adresse")
        self.fiche_adresse.setGeometry(QRect(20, 120, 241, 20))
        self.fiche_telephone = QCheckBox(self.Informations)
        self.fiche_telephone.setObjectName(u"fiche_telephone")
        self.fiche_telephone.setGeometry(QRect(20, 160, 241, 20))
        self.fiche_duree_session = QCheckBox(self.Informations)
        self.fiche_duree_session.setObjectName(u"fiche_duree_session")
        self.fiche_duree_session.setGeometry(QRect(410, 40, 241, 20))
        self.fiche_15min = QCheckBox(self.Informations)
        self.fiche_15min.setObjectName(u"fiche_15min")
        self.fiche_15min.setGeometry(QRect(440, 70, 221, 20))
        self.fiche_30min = QCheckBox(self.Informations)
        self.fiche_30min.setObjectName(u"fiche_30min")
        self.fiche_30min.setGeometry(QRect(440, 100, 241, 20))
        self.fiche_1h = QCheckBox(self.Informations)
        self.fiche_1h.setObjectName(u"fiche_1h")
        self.fiche_1h.setGeometry(QRect(440, 130, 231, 20))
        self.fiche_bouton_reglement = QCheckBox(self.Informations)
        self.fiche_bouton_reglement.setObjectName(u"fiche_bouton_reglement")
        self.fiche_bouton_reglement.setGeometry(QRect(20, 200, 281, 20))
        self.fiche_reglement = QCheckBox(self.Informations)
        self.fiche_reglement.setObjectName(u"fiche_reglement")
        self.fiche_reglement.setGeometry(QRect(410, 160, 351, 20))
        self.onglet.addTab(self.formulaire, "")
        self.titres = QWidget()
        self.titres.setObjectName(u"titres")
        self.aide_titres = QPushButton(self.titres)
        self.aide_titres.setObjectName(u"aide_titres")
        self.aide_titres.setGeometry(QRect(760, 10, 75, 24))
        self.label_titre_1 = QLabel(self.titres)
        self.label_titre_1.setObjectName(u"label_titre_1")
        self.label_titre_1.setGeometry(QRect(20, 20, 151, 16))
        self.label_titre_2 = QLabel(self.titres)
        self.label_titre_2.setObjectName(u"label_titre_2")
        self.label_titre_2.setGeometry(QRect(20, 60, 131, 16))
        self.label_titre__3 = QLabel(self.titres)
        self.label_titre__3.setObjectName(u"label_titre__3")
        self.label_titre__3.setGeometry(QRect(20, 100, 141, 16))
        self.titre_popup_1 = QLineEdit(self.titres)
        self.titre_popup_1.setObjectName(u"titre_popup_1")
        self.titre_popup_1.setGeometry(QRect(160, 20, 431, 21))
        self.titre_popup_2 = QLineEdit(self.titres)
        self.titre_popup_2.setObjectName(u"titre_popup_2")
        self.titre_popup_2.setGeometry(QRect(160, 60, 431, 21))
        self.titre_popup_3 = QLineEdit(self.titres)
        self.titre_popup_3.setObjectName(u"titre_popup_3")
        self.titre_popup_3.setGeometry(QRect(160, 100, 431, 21))
        self.label_18 = QLabel(self.titres)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 140, 161, 16))
        self.titre_popup_4 = QLineEdit(self.titres)
        self.titre_popup_4.setObjectName(u"titre_popup_4")
        self.titre_popup_4.setGeometry(QRect(180, 140, 421, 21))
        self.onglet.addTab(self.titres, "")
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
        self.text_popup_4 = QPlainTextEdit(self.onglet_popup_4)
        self.text_popup_4.setObjectName(u"text_popup_4")
        self.text_popup_4.setGeometry(QRect(10, 40, 811, 241))
        self.text_popup_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.onglet_popup.addTab(self.onglet_popup_4, "")
        self.onglet.addTab(self.textes, "")
        self.style = QWidget()
        self.style.setObjectName(u"style")
        self.aide_style = QPushButton(self.style)
        self.aide_style.setObjectName(u"aide_style")
        self.aide_style.setGeometry(QRect(760, 10, 75, 24))
        self.label = QLabel(self.style)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 121, 16))
        self.largeur_popup = QLineEdit(self.style)
        self.largeur_popup.setObjectName(u"largeur_popup")
        self.largeur_popup.setGeometry(QRect(150, 20, 113, 21))
        self.label_2 = QLabel(self.style)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 20, 49, 16))
        self.label_3 = QLabel(self.style)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 60, 121, 16))
        self.hauteur_popup = QLineEdit(self.style)
        self.hauteur_popup.setObjectName(u"hauteur_popup")
        self.hauteur_popup.setGeometry(QRect(150, 60, 113, 21))
        self.label_4 = QLabel(self.style)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 60, 49, 16))
        self.label_5 = QLabel(self.style)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 100, 121, 16))
        self.police = QComboBox(self.style)
        self.police.setObjectName(u"police")
        self.police.setGeometry(QRect(150, 100, 171, 22))
        self.label_6 = QLabel(self.style)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 140, 171, 16))
        self.taille_police = QLineEdit(self.style)
        self.taille_police.setObjectName(u"taille_police")
        self.taille_police.setGeometry(QRect(190, 140, 71, 21))
        self.label_7 = QLabel(self.style)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(270, 140, 49, 16))
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
        self.label_12.setGeometry(QRect(20, 100, 241, 16))
        self.timer_second_popup = QLineEdit(self.temps)
        self.timer_second_popup.setObjectName(u"timer_second_popup")
        self.timer_second_popup.setGeometry(QRect(260, 100, 51, 21))
        self.label_13 = QLabel(self.temps)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(320, 100, 49, 16))
        self.label_14 = QLabel(self.temps)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 180, 391, 16))
        self.timer_dernier_popup = QLineEdit(self.temps)
        self.timer_dernier_popup.setObjectName(u"timer_dernier_popup")
        self.timer_dernier_popup.setGeometry(QRect(410, 180, 51, 21))
        self.label_15 = QLabel(self.temps)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(470, 180, 49, 16))
        self.label_19 = QLabel(self.temps)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 140, 311, 16))
        self.timer_troisieme_popup = QLineEdit(self.temps)
        self.timer_troisieme_popup.setObjectName(u"timer_troisieme_popup")
        self.timer_troisieme_popup.setGeometry(QRect(330, 140, 51, 21))
        self.label_20 = QLabel(self.temps)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(390, 140, 49, 16))
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
        self.activation_fermeture.setGeometry(QRect(20, 60, 361, 20))
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

        self.onglet.setCurrentIndex(0)
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
        self.fiche_log.setText(QCoreApplication.translate("Configuration", u"Stocker les informations donn\u00e9es dans la fiche d'entr\u00e9e dans un document excel", None))
        self.Informations.setTitle(QCoreApplication.translate("Configuration", u"Informations requises", None))
        self.fiche_nom.setText(QCoreApplication.translate("Configuration", u"Nom de famille + pr\u00e9nom", None))
        self.fiche_mail.setText(QCoreApplication.translate("Configuration", u"Adresse mail", None))
        self.fiche_adresse.setText(QCoreApplication.translate("Configuration", u"Adresse postale", None))
        self.fiche_telephone.setText(QCoreApplication.translate("Configuration", u"Num\u00e9ro de t\u00e9l\u00e9phone", None))
        self.fiche_duree_session.setText(QCoreApplication.translate("Configuration", u"Choix du dur\u00e9e de la session", None))
        self.fiche_15min.setText(QCoreApplication.translate("Configuration", u"15 minutes", None))
        self.fiche_30min.setText(QCoreApplication.translate("Configuration", u"30 minutes", None))
        self.fiche_1h.setText(QCoreApplication.translate("Configuration", u"1 heure", None))
        self.fiche_bouton_reglement.setText(QCoreApplication.translate("Configuration", u"Afficher le bouton vers le r\u00e9glement int\u00e9rieur", None))
        self.fiche_reglement.setText(QCoreApplication.translate("Configuration", u"Afficher la checkbox pour accepter le r\u00e9glement int\u00e9rieur", None))
        self.onglet.setTabText(self.onglet.indexOf(self.formulaire), QCoreApplication.translate("Configuration", u"Fiche d'entr\u00e9e", None))
        self.aide_titres.setText(QCoreApplication.translate("Configuration", u"Aide", None))
        self.label_titre_1.setText(QCoreApplication.translate("Configuration", u"Titre du premier popup :", None))
        self.label_titre_2.setText(QCoreApplication.translate("Configuration", u"Titre du second popup :", None))
        self.label_titre__3.setText(QCoreApplication.translate("Configuration", u"Titre du troisi\u00e8me popup :", None))
        self.label_18.setText(QCoreApplication.translate("Configuration", u"Titre du popup de fermeture :", None))
        self.onglet.setTabText(self.onglet.indexOf(self.titres), QCoreApplication.translate("Configuration", u"Titres", None))
        self.aide_textes.setText(QCoreApplication.translate("Configuration", u"Aide", None))
        self.label_text_1.setText(QCoreApplication.translate("Configuration", u"Texte affich\u00e9 dans le premier popup :", None))
        self.onglet_popup.setTabText(self.onglet_popup.indexOf(self.onglet_popup_1), QCoreApplication.translate("Configuration", u"Premier popup", None))
        self.label_text_2.setText(QCoreApplication.translate("Configuration", u"Texte affich\u00e9 dans le second popup :", None))
        self.onglet_popup.setTabText(self.onglet_popup.indexOf(self.onglet_popup_2), QCoreApplication.translate("Configuration", u"Second popup", None))
        self.label_popup_3.setText(QCoreApplication.translate("Configuration", u"Texte affich\u00e9 dans le troisi\u00e8me popup :", None))
        self.onglet_popup.setTabText(self.onglet_popup.indexOf(self.onglet_popup_3), QCoreApplication.translate("Configuration", u"Troisi\u00e8me popup", None))
        self.label_16.setText(QCoreApplication.translate("Configuration", u"Texte affich\u00e9 dans le popup de fermeture de session :", None))
        self.onglet_popup.setTabText(self.onglet_popup.indexOf(self.onglet_popup_4), QCoreApplication.translate("Configuration", u"Popup de femerture", None))
        self.onglet.setTabText(self.onglet.indexOf(self.textes), QCoreApplication.translate("Configuration", u"Textes", None))
        self.aide_style.setText(QCoreApplication.translate("Configuration", u"Aide", None))
        self.label.setText(QCoreApplication.translate("Configuration", u"Largeur des popups :", None))
        self.label_2.setText(QCoreApplication.translate("Configuration", u"pixels", None))
        self.label_3.setText(QCoreApplication.translate("Configuration", u"Hauteur des popups :", None))
        self.label_4.setText(QCoreApplication.translate("Configuration", u"pixels", None))
        self.label_5.setText(QCoreApplication.translate("Configuration", u"Police de caract\u00e8res :", None))
        self.label_6.setText(QCoreApplication.translate("Configuration", u"Taille de la police de caract\u00e8re :", None))
        self.label_7.setText(QCoreApplication.translate("Configuration", u"pixels", None))
        self.onglet.setTabText(self.onglet.indexOf(self.style), QCoreApplication.translate("Configuration", u"Style", None))
        self.aide_temps.setText(QCoreApplication.translate("Configuration", u"Aide", None))
        self.label_8.setText(QCoreApplication.translate("Configuration", u"D\u00e9lai avant fermetures automatique d'un popup :", None))
        self.label_9.setText(QCoreApplication.translate("Configuration", u"secondes", None))
        self.label_10.setText(QCoreApplication.translate("Configuration", u"Dur\u00e9e totale de la session utilisateur :", None))
        self.label_11.setText(QCoreApplication.translate("Configuration", u"minutes", None))
        self.label_12.setText(QCoreApplication.translate("Configuration", u"D\u00e9lai avant ouverture de la seconde popup :", None))
        self.label_13.setText(QCoreApplication.translate("Configuration", u"minutes", None))
        self.label_14.setText(QCoreApplication.translate("Configuration", u"Dur\u00e9e d'ouverture de la derni\u00e8re popup avant la fermeture de la session :", None))
        self.label_15.setText(QCoreApplication.translate("Configuration", u"secondes", None))
        self.label_19.setText(QCoreApplication.translate("Configuration", u"D\u00e9lai entre la troisi\u00e8me popup et la fermeture de session :", None))
        self.label_20.setText(QCoreApplication.translate("Configuration", u"minutes", None))
        self.onglet.setTabText(self.onglet.indexOf(self.temps), QCoreApplication.translate("Configuration", u"Temps", None))
        self.aide_gestion.setText(QCoreApplication.translate("Configuration", u"Aide", None))
        self.label_17.setText(QCoreApplication.translate("Configuration", u"Type de fermeture de session :", None))
        self.activation_fermeture.setText(QCoreApplication.translate("Configuration", u"Activer le popup bloqu\u00e9, plein \u00e9cran, \u00e0 la fermeture de la session", None))
        self.onglet.setTabText(self.onglet.indexOf(self.gestion), QCoreApplication.translate("Configuration", u"Gestion sessions", None))
        self.Enregistrer.setText(QCoreApplication.translate("Configuration", u"Enregistrer", None))
        self.annuler.setText(QCoreApplication.translate("Configuration", u"Annuler", None))
        self.menuConfiguration.setTitle(QCoreApplication.translate("Configuration", u"Configuration", None))
    # retranslateUi

