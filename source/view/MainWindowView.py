# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(315, 249)
        mainWindow.setMinimumSize(QSize(315, 249))
        mainWindow.setMaximumSize(QSize(315, 249))
        mainWindow.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 0, 241, 241))
        self.menuLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.menuLayout.setObjectName(u"menuLayout")
        self.menuLayout.setContentsMargins(0, 0, 0, 0)
        self.afdButton = QPushButton(self.verticalLayoutWidget)
        self.afdButton.setObjectName(u"afdButton")
        self.afdButton.setMaximumSize(QSize(239, 24))

        self.menuLayout.addWidget(self.afdButton)

        self.apdButton = QPushButton(self.verticalLayoutWidget)
        self.apdButton.setObjectName(u"apdButton")
        self.apdButton.setMaximumSize(QSize(239, 24))

        self.menuLayout.addWidget(self.apdButton)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Trabalho Final de F.T.C", None))
        self.afdButton.setText(QCoreApplication.translate("mainWindow", u"Caldeir\u00e3o Finito Deterministico", None))
        self.apdButton.setText(QCoreApplication.translate("mainWindow", u"Caldeir\u00e3o de Pilha Deterministico", None))
    # retranslateUi

