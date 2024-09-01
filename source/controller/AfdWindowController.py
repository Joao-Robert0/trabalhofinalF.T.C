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

        #Imagem que vai cair no caldeirão, inicialmente não vai estar vísivel
        self.ui.ingredientLabel.setVisible(False)
        self.original_position = self.ui.ingredientLabel.pos() #Posição original, vai ser usada na animação
        self.target_y = 350 # Até aonde ela vai cair

         # Inicialize o timer que vai controlar a animação
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.moveImage)
        
        # Conecte os botões da janela AFD a funções se necessário
        self.ui.aButton.clicked.connect(self.aButtonClicked)
        self.ui.bButton.clicked.connect(self.bButtonClicked)
        self.ui.dButton.clicked.connect(self.dButtonClicked)
        self.ui.mButton.clicked.connect(self.mButtonClicked)
        self.ui.oButton.clicked.connect(self.oButtonClicked)
        self.ui.pButton.clicked.connect(self.pButtonClicked)
        self.ui.rButton.clicked.connect(self.rButtonClicked)
        self.ui.vButton.clicked.connect(self.vButtonClicked)

    def aButtonClicked(self):
        imagePath = "./assets/waterbottle.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def bButtonClicked(self):
        imagePath="./assets/butterflywing.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def dButtonClicked(self):
        imagePath="./assets/finger.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def mButtonClicked(self):
        imagePath="./assets/batwing.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)

    def oButtonClicked(self):
        imagePath = "./assets/bonemeal.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def pButtonClicked(self):
        imagePath="./assets/petals.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def rButtonClicked(self):
        imagePath="./assets/rattail.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)

    def vButtonClicked(self):
        imagePath="./assets/snakevenom.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)



    #Método que vai mover a imagem
    def moveImage(self):
        current_pos = self.ui.ingredientLabel.pos()
        if current_pos.y() < self.target_y:
            new_y = current_pos.y() + 20  # Velocidade da queda
            self.ui.ingredientLabel.move(current_pos.x(), new_y)
        else:
            self.timer.stop()
            self.ui.ingredientLabel.setVisible(False)
            self.ui.ingredientLabel.move(self.original_position)  # Retorne à posição original