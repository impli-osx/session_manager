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
        Ficheentree.resize(1482, 866)
        Ficheentree.setDocumentMode(False)
        self.centralwidget = QWidget(Ficheentree)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(550, 730, 421, 31))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.reglement = QCheckBox(self.formLayoutWidget_2)
        self.reglement.setObjectName(u"reglement")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.reglement)

        self.formLayoutWidget_3 = QWidget(self.centralwidget)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(650, 760, 221, 61))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.connecter = QPushButton(self.formLayoutWidget_3)
        self.connecter.setObjectName(u"connecter")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.connecter)

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 100, 131, 401))
        self.label_gauche = QFormLayout(self.formLayoutWidget)
        self.label_gauche.setObjectName(u"label_gauche")
        self.label_gauche.setContentsMargins(0, 0, 0, 0)
        self.formLayoutWidget_4 = QWidget(self.centralwidget)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(150, 100, 191, 401))
        self.text_gauche = QFormLayout(self.formLayoutWidget_4)
        self.text_gauche.setObjectName(u"text_gauche")
        self.text_gauche.setContentsMargins(0, 0, 0, 0)
        self.formLayoutWidget_5 = QWidget(self.centralwidget)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(370, 100, 161, 401))
        self.label_centre = QFormLayout(self.formLayoutWidget_5)
        self.label_centre.setObjectName(u"label_centre")
        self.label_centre.setContentsMargins(0, 0, 0, 0)
        self.formLayoutWidget_6 = QWidget(self.centralwidget)
        self.formLayoutWidget_6.setObjectName(u"formLayoutWidget_6")
        self.formLayoutWidget_6.setGeometry(QRect(530, 100, 201, 401))
        self.text_centre = QFormLayout(self.formLayoutWidget_6)
        self.text_centre.setObjectName(u"text_centre")
        self.text_centre.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 40, 101, 31))
        self.formLayoutWidget_7 = QWidget(self.centralwidget)
        self.formLayoutWidget_7.setObjectName(u"formLayoutWidget_7")
        self.formLayoutWidget_7.setGeometry(QRect(750, 30, 721, 571))
        self.formLayout = QFormLayout(self.formLayoutWidget_7)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1000, 10, 241, 16))
        Ficheentree.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Ficheentree)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1482, 22))
        Ficheentree.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Ficheentree)
        self.statusbar.setObjectName(u"statusbar")
        Ficheentree.setStatusBar(self.statusbar)

        self.retranslateUi(Ficheentree)

        QMetaObject.connectSlotsByName(Ficheentree)
    # setupUi

    def retranslateUi(self, Ficheentree):
        Ficheentree.setWindowTitle(QCoreApplication.translate("Ficheentree", u"MainWindow", None))
        self.reglement.setText(QCoreApplication.translate("Ficheentree", u"J'ai lu j'accepte les conditions du r\u00e8glement int\u00e9rieur de l'espace num\u00e9rique", None))
        self.connecter.setText(QCoreApplication.translate("Ficheentree", u"Ouvrir la session", None))
        self.label.setText(QCoreApplication.translate("Ficheentree", u"Vos informations", None))
        self.label_2.setText(QCoreApplication.translate("Ficheentree", u"R\u00e8glement int\u00e9rieur de l'espace num\u00e9rique", None))
    # retranslateUi

