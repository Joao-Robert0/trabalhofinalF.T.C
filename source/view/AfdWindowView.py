# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adfWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_afdWindow(object):
    def setupUi(self, afdWindow):
        if not afdWindow.objectName():
            afdWindow.setObjectName(u"afdWindow")
        afdWindow.resize(608, 566)
        self.centralwidget = QWidget(afdWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.aLabel = QLabel(self.centralwidget)
        self.aLabel.setObjectName(u"aLabel")
        self.aLabel.setGeometry(QRect(50, 40, 30, 17))
        self.aLabel.setMinimumSize(QSize(30, 17))
        self.aLabel.setMaximumSize(QSize(30, 17))
        self.bLabel = QLabel(self.centralwidget)
        self.bLabel.setObjectName(u"bLabel")
        self.bLabel.setGeometry(QRect(100, 20, 61, 51))
        self.bLabel.setMinimumSize(QSize(61, 51))
        self.bLabel.setMaximumSize(QSize(61, 51))
        self.bLabel.setWordWrap(True)
        self.aButton = QPushButton(self.centralwidget)
        self.aButton.setObjectName(u"aButton")
        self.aButton.setGeometry(QRect(50, 60, 20, 25))
        self.aButton.setMaximumSize(QSize(20, 50))
        self.bButton = QPushButton(self.centralwidget)
        self.bButton.setObjectName(u"bButton")
        self.bButton.setGeometry(QRect(110, 60, 20, 25))
        self.bButton.setMaximumSize(QSize(20, 50))
        self.dButton = QPushButton(self.centralwidget)
        self.dButton.setObjectName(u"dButton")
        self.dButton.setGeometry(QRect(180, 60, 21, 25))
        self.dLabel = QLabel(self.centralwidget)
        self.dLabel.setObjectName(u"dLabel")
        self.dLabel.setGeometry(QRect(170, 20, 61, 51))
        self.dLabel.setMinimumSize(QSize(61, 51))
        self.dLabel.setMaximumSize(QSize(61, 51))
        self.dLabel.setWordWrap(True)
        self.mLabel = QLabel(self.centralwidget)
        self.mLabel.setObjectName(u"mLabel")
        self.mLabel.setGeometry(QRect(240, 20, 61, 51))
        self.mLabel.setMinimumSize(QSize(61, 51))
        self.mLabel.setMaximumSize(QSize(61, 51))
        self.mLabel.setWordWrap(True)
        self.mButton = QPushButton(self.centralwidget)
        self.mButton.setObjectName(u"mButton")
        self.mButton.setGeometry(QRect(250, 60, 21, 25))
        self.oButton = QPushButton(self.centralwidget)
        self.oButton.setObjectName(u"oButton")
        self.oButton.setGeometry(QRect(310, 60, 21, 25))
        self.oLabel = QLabel(self.centralwidget)
        self.oLabel.setObjectName(u"oLabel")
        self.oLabel.setGeometry(QRect(310, 20, 61, 51))
        self.oLabel.setMinimumSize(QSize(61, 51))
        self.oLabel.setMaximumSize(QSize(61, 51))
        self.oLabel.setWordWrap(True)
        self.pButton = QPushButton(self.centralwidget)
        self.pButton.setObjectName(u"pButton")
        self.pButton.setGeometry(QRect(380, 60, 21, 25))
        self.rButton = QPushButton(self.centralwidget)
        self.rButton.setObjectName(u"rButton")
        self.rButton.setGeometry(QRect(440, 60, 21, 25))
        self.vButton = QPushButton(self.centralwidget)
        self.vButton.setObjectName(u"vButton")
        self.vButton.setGeometry(QRect(500, 60, 21, 25))
        self.pLabel = QLabel(self.centralwidget)
        self.pLabel.setObjectName(u"pLabel")
        self.pLabel.setGeometry(QRect(370, 20, 61, 51))
        self.pLabel.setMinimumSize(QSize(61, 51))
        self.pLabel.setMaximumSize(QSize(61, 51))
        self.pLabel.setWordWrap(True)
        self.rLabel = QLabel(self.centralwidget)
        self.rLabel.setObjectName(u"rLabel")
        self.rLabel.setGeometry(QRect(430, 20, 61, 51))
        self.rLabel.setMinimumSize(QSize(61, 51))
        self.rLabel.setMaximumSize(QSize(61, 51))
        self.rLabel.setWordWrap(True)
        self.vLabel = QLabel(self.centralwidget)
        self.vLabel.setObjectName(u"vLabel")
        self.vLabel.setGeometry(QRect(490, 20, 61, 51))
        self.vLabel.setMinimumSize(QSize(61, 51))
        self.vLabel.setMaximumSize(QSize(61, 51))
        self.vLabel.setWordWrap(True)
        self.cauldronLabel = QLabel(self.centralwidget)
        self.cauldronLabel.setObjectName(u"cauldronLabel")
        self.cauldronLabel.setGeometry(QRect(160, 120, 281, 421))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 110, 58, 16))
        afdWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(afdWindow)
        self.statusbar.setObjectName(u"statusbar")
        afdWindow.setStatusBar(self.statusbar)

        self.retranslateUi(afdWindow)

        QMetaObject.connectSlotsByName(afdWindow)
    # setupUi

    def retranslateUi(self, afdWindow):
        afdWindow.setWindowTitle(QCoreApplication.translate("afdWindow", u"Caldeir\u00e3o Finito Deterministico", None))
        self.aLabel.setText(QCoreApplication.translate("afdWindow", u"\u00c1gua", None))
        self.bLabel.setText(QCoreApplication.translate("afdWindow", u"Asas de Borboleta", None))
        self.aButton.setText(QCoreApplication.translate("afdWindow", u"a", None))
        self.bButton.setText(QCoreApplication.translate("afdWindow", u"b", None))
        self.dButton.setText(QCoreApplication.translate("afdWindow", u"d", None))
        self.dLabel.setText(QCoreApplication.translate("afdWindow", u"Dedos Humanos", None))
        self.mLabel.setText(QCoreApplication.translate("afdWindow", u"Asas de Morcego", None))
        self.mButton.setText(QCoreApplication.translate("afdWindow", u"m", None))
        self.oButton.setText(QCoreApplication.translate("afdWindow", u"o", None))
        self.oLabel.setText(QCoreApplication.translate("afdWindow", u"P\u00f3 de Ossos", None))
        self.pButton.setText(QCoreApplication.translate("afdWindow", u"p", None))
        self.rButton.setText(QCoreApplication.translate("afdWindow", u"r", None))
        self.vButton.setText(QCoreApplication.translate("afdWindow", u"v", None))
        self.pLabel.setText(QCoreApplication.translate("afdWindow", u"P\u00e9talas", None))
        self.rLabel.setText(QCoreApplication.translate("afdWindow", u"Rabo de Rato", None))
        self.vLabel.setText(QCoreApplication.translate("afdWindow", u"Veneno de Cobra", None))
        self.cauldronLabel.setText("")
        self.label.setText("")
    # retranslateUi

