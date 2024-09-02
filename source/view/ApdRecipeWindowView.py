# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apdRecipeWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_apdRecipeWindow(object):
    def setupUi(self, apdRecipeWindow):
        if not apdRecipeWindow.objectName():
            apdRecipeWindow.setObjectName(u"apdRecipeWindow")
        apdRecipeWindow.resize(322, 329)
        apdRecipeWindow.setMinimumSize(QSize(322, 329))
        apdRecipeWindow.setMaximumSize(QSize(322, 329))
        apdRecipeWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(apdRecipeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 40, 208, 281))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.restauracaoButton = QPushButton(self.formLayoutWidget)
        self.restauracaoButton.setObjectName(u"restauracaoButton")
        self.restauracaoButton.setMinimumSize(QSize(118, 24))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.restauracaoButton)

        self.invisibilidadeButton = QPushButton(self.formLayoutWidget)
        self.invisibilidadeButton.setObjectName(u"invisibilidadeButton")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.invisibilidadeButton)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 231, 28))
        apdRecipeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(apdRecipeWindow)
        self.statusbar.setObjectName(u"statusbar")
        apdRecipeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(apdRecipeWindow)

        QMetaObject.connectSlotsByName(apdRecipeWindow)
    # setupUi

    def retranslateUi(self, apdRecipeWindow):
        apdRecipeWindow.setWindowTitle(QCoreApplication.translate("apdRecipeWindow", u"Recipe Window", None))
        self.restauracaoButton.setText(QCoreApplication.translate("apdRecipeWindow", u"Po\u00e7\u00e3o de Invisibilidade", None))
        self.invisibilidadeButton.setText(QCoreApplication.translate("apdRecipeWindow", u"Po\u00e7\u00e3o de Restaura\u00e7\u00e3o do Tempo", None))
        self.label.setText(QCoreApplication.translate("apdRecipeWindow", u"Escolha a Receita que voc\u00ea deseja fazer", None))
    # retranslateUi

