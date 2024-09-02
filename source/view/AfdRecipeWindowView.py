# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'afdRecipeWindow.ui'
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

class Ui_afdRecipeWindow(object):
    def setupUi(self, afdRecipeWindow):
        if not afdRecipeWindow.objectName():
            afdRecipeWindow.setObjectName(u"afdRecipeWindow")
        afdRecipeWindow.resize(322, 329)
        afdRecipeWindow.setMinimumSize(QSize(322, 329))
        afdRecipeWindow.setMaximumSize(QSize(322, 329))
        afdRecipeWindow.setWindowOpacity(1.000000000000000)
        self.centralwidget = QWidget(afdRecipeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 40, 181, 281))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.vitalidadeButton = QPushButton(self.formLayoutWidget)
        self.vitalidadeButton.setObjectName(u"vitalidadeButton")
        self.vitalidadeButton.setMinimumSize(QSize(118, 24))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.vitalidadeButton)

        self.asasButton = QPushButton(self.formLayoutWidget)
        self.asasButton.setObjectName(u"asasButton")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.asasButton)

        self.miniaturizacaoButton = QPushButton(self.formLayoutWidget)
        self.miniaturizacaoButton.setObjectName(u"miniaturizacaoButton")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.miniaturizacaoButton)

        self.sussurroButton = QPushButton(self.formLayoutWidget)
        self.sussurroButton.setObjectName(u"sussurroButton")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.sussurroButton)

        self.metamorfoseButton = QPushButton(self.formLayoutWidget)
        self.metamorfoseButton.setObjectName(u"metamorfoseButton")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.metamorfoseButton)

        self.percepcaoButton = QPushButton(self.formLayoutWidget)
        self.percepcaoButton.setObjectName(u"percepcaoButton")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.percepcaoButton)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 231, 28))
        afdRecipeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(afdRecipeWindow)
        self.statusbar.setObjectName(u"statusbar")
        afdRecipeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(afdRecipeWindow)

        QMetaObject.connectSlotsByName(afdRecipeWindow)
    # setupUi

    def retranslateUi(self, afdRecipeWindow):
        afdRecipeWindow.setWindowTitle(QCoreApplication.translate("afdRecipeWindow", u"Recipe Window", None))
        self.vitalidadeButton.setText(QCoreApplication.translate("afdRecipeWindow", u"Elixir da Vitalidade", None))
        self.asasButton.setText(QCoreApplication.translate("afdRecipeWindow", u"Elixir das Asas Celestes", None))
        self.miniaturizacaoButton.setText(QCoreApplication.translate("afdRecipeWindow", u"Elixir da Miniaturiza\u00e7\u00e3o", None))
        self.sussurroButton.setText(QCoreApplication.translate("afdRecipeWindow", u"Po\u00e7\u00e3o do Sussurro Sombrio", None))
        self.metamorfoseButton.setText(QCoreApplication.translate("afdRecipeWindow", u"N\u00e9ctar da Metamorfose", None))
        self.percepcaoButton.setText(QCoreApplication.translate("afdRecipeWindow", u"Elixir da Percep\u00e7\u00e3o Agu\u00e7ada", None))
        self.label.setText(QCoreApplication.translate("afdRecipeWindow", u"Escolha a Receita que voc\u00ea deseja fazer", None))
    # retranslateUi

