# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'productWindow.ui'
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

class Ui_ProductWindow(object):
    def setupUi(self, ProductWindow):
        if not ProductWindow.objectName():
            ProductWindow.setObjectName(u"ProductWindow")
        ProductWindow.resize(406, 264)
        ProductWindow.setMinimumSize(QSize(406, 264))
        ProductWindow.setMaximumSize(QSize(406, 264))
        self.centralwidget = QWidget(ProductWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(150, 210, 80, 24))
        self.productLabel = QLabel(self.centralwidget)
        self.productLabel.setObjectName(u"productLabel")
        self.productLabel.setGeometry(QRect(150, 110, 91, 71))
        self.productLabel.setMinimumSize(QSize(91, 71))
        self.productLabel.setMaximumSize(QSize(91, 71))
        self.productLabel.setScaledContents(True)
        self.descriptionLabel = QLabel(self.centralwidget)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        self.descriptionLabel.setGeometry(QRect(100, 35, 191, 41))
        self.descriptionLabel.setWordWrap(True)
        ProductWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ProductWindow)
        self.statusbar.setObjectName(u"statusbar")
        ProductWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ProductWindow)

        QMetaObject.connectSlotsByName(ProductWindow)
    # setupUi

    def retranslateUi(self, ProductWindow):
        ProductWindow.setWindowTitle(QCoreApplication.translate("ProductWindow", u"Po\u00e7\u00e3o Adquirida", None))
        self.stopButton.setText(QCoreApplication.translate("ProductWindow", u"OK", None))
        self.productLabel.setText("")
        self.descriptionLabel.setText("")
    # retranslateUi

