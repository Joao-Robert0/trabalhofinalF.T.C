from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import (QMovie, QPixmap)
from PySide6.QtCore import QTimer
from view.AfdWindowView import Ui_afdWindow  # Certifique-se de que o nome da view esteja correto

class AFDWindowController(QMainWindow):
    def __init__(self):
        super(AFDWindowController, self).__init__()
        self.ui = Ui_afdWindow()
        self.ui.setupUi(self)

        #Gif do caldeirão
        self.movie = QMovie("./assets/Caldeirão.gif")
        self.ui.cauldronLabel.setMovie(self.movie)
        self.movie.start()

        # Conecte os botões da janela AFD a funções se necessário
        self.ui.aButton.clicked.connect(self.aButtonClicked)
        self.ui.bButton.clicked.connect(self.aButtonClicked)

    def aButtonClicked(self):
        print("Test Button in aButton Clicked")