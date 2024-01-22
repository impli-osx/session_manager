# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FicheEntree.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_Ficheentree(object):
    def setupUi(self, Ficheentree):
        if not Ficheentree.objectName():
            Ficheentree.setObjectName(u"Ficheentree")
        Ficheentree.resize(1535, 913)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ficheentree.sizePolicy().hasHeightForWidth())
        Ficheentree.setSizePolicy(sizePolicy)
        Ficheentree.setDocumentMode(False)
        self.centralwidget = QWidget(Ficheentree)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(460, 730, 615, 31))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.reglement = QCheckBox(self.formLayoutWidget_2)
        self.reglement.setObjectName(u"reglement")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.reglement.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.reglement)

        self.formLayoutWidget_3 = QWidget(self.centralwidget)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(650, 760, 221, 61))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.connecter = QPushButton(self.formLayoutWidget_3)
        self.connecter.setObjectName(u"connecter")
        self.connecter.setFont(font)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.connecter)

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 100, 261, 401))
        self.form_gauche = QFormLayout(self.formLayoutWidget)
        self.form_gauche.setObjectName(u"form_gauche")
        self.form_gauche.setContentsMargins(0, 0, 0, 0)
        self.formLayoutWidget_5 = QWidget(self.centralwidget)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(290, 100, 291, 401))
        self.form_centre = QFormLayout(self.formLayoutWidget_5)
        self.form_centre.setObjectName(u"form_centre")
        self.form_centre.setContentsMargins(0, 0, 0, 0)
        self.label_informations = QLabel(self.centralwidget)
        self.label_informations.setObjectName(u"label_informations")
        self.label_informations.setGeometry(QRect(140, 30, 281, 51))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_informations.setFont(font1)
        self.label_informations.setAlignment(Qt.AlignCenter)
        self.label_informations.setTextInteractionFlags(Qt.NoTextInteraction)
        self.formLayoutWidget_7 = QWidget(self.centralwidget)
        self.formLayoutWidget_7.setObjectName(u"formLayoutWidget_7")
        self.formLayoutWidget_7.setGeometry(QRect(750, 100, 721, 611))
        self.form_reglement = QFormLayout(self.formLayoutWidget_7)
        self.form_reglement.setObjectName(u"form_reglement")
        self.form_reglement.setContentsMargins(0, 0, 0, 0)
        self.label_reglement = QLabel(self.centralwidget)
        self.label_reglement.setObjectName(u"label_reglement")
        self.label_reglement.setGeometry(QRect(860, 40, 521, 41))
        self.label_reglement.setFont(font)
        self.label_reglement.setAlignment(Qt.AlignCenter)
        Ficheentree.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Ficheentree)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1535, 22))
        Ficheentree.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Ficheentree)
        self.statusbar.setObjectName(u"statusbar")
        Ficheentree.setStatusBar(self.statusbar)

        self.retranslateUi(Ficheentree)

        QMetaObject.connectSlotsByName(Ficheentree)
    # setupUi

    def retranslateUi(self, Ficheentree):
        Ficheentree.setWindowTitle(QCoreApplication.translate("Ficheentree", u"MainWindow", None))
        self.reglement.setText(QCoreApplication.translate("Ficheentree", u"J'ai lu et j'accepte les conditions du r\u00e8glement int\u00e9rieur de l'espace num\u00e9rique", None))
        self.connecter.setText(QCoreApplication.translate("Ficheentree", u"Ouvrir la session", None))
        self.label_informations.setText(QCoreApplication.translate("Ficheentree", u"Vos informations", None))
        self.label_reglement.setText(QCoreApplication.translate("Ficheentree", u"R\u00e8glement int\u00e9rieur de l'espace num\u00e9rique", None))
    # retranslateUi

