from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import (QMovie, QPixmap)
from PySide6.QtCore import QTimer
from view.ApdWindowView import Ui_apdWindow
from controller.ProductWindowController import ProductWindowController
from controller.ApdRecipeWindowController import ApdRecipeWindowController
import model.SharedData

class APDWindowController(QMainWindow):
    def __init__(self):
        super(APDWindowController, self).__init__()
        self.ui = Ui_apdWindow()
        self.ui.setupUi(self)

        self.apdRecipeWindow = ApdRecipeWindowController() #Janela que vai permitir escolher a receita
        self.apdRecipeWindow.show()

        self.productWindow = None #Janela com o resultado da função

        #Gif do caldeirão
        self.movie = QMovie("./source/assets/Caldeirão.gif")
        self.ui.cauldronLabel.setMovie(self.movie)
        self.movie.start()

        #Imagem que vai cair no caldeirão, inicialmente não vai estar vísivel
        self.ui.ingredientLabel.setVisible(False)
        self.original_position = self.ui.ingredientLabel.pos() #Posição original, vai ser usada na animação
        self.target_y = 350 # Até aonde ela vai cair

         # Inicialize o timer que vai controlar a animação
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.moveImage)
        
        #            Botões dos ingredientes               #
        self.ui.aButton.clicked.connect(self.aButtonClicked)  # Agua  
        self.ui.bButton.clicked.connect(self.bButtonClicked)  # Asa de Borboleta
        self.ui.dButton.clicked.connect(self.dButtonClicked)  # Dedos Humanos
        self.ui.mButton.clicked.connect(self.mButtonClicked)  # Asa de Morcego
        self.ui.oButton.clicked.connect(self.oButtonClicked)  # Pó de ossos
        self.ui.pButton.clicked.connect(self.pButtonClicked)  # Pétalas
        self.ui.rButton.clicked.connect(self.rButtonClicked)  # Rabo de rato
        self.ui.vButton.clicked.connect(self.vButtonClicked)  # Veneno de cobra
        # ================================================ #
        
        self.ui.stopButton.clicked.connect(self.stopButtonClicked) # Mostra a poção produzida

    def aButtonClicked(self):
        imagePath = "./source/assets/waterbottle.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def bButtonClicked(self):
        imagePath="./source/assets/butterflywing.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def dButtonClicked(self):
        imagePath="./source/assets/finger.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def mButtonClicked(self):
        imagePath="./source/assets/batwing.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)

    def oButtonClicked(self):
        imagePath = "./source/assets/bonemeal.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def pButtonClicked(self):
        imagePath="./source/assets/petals.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def rButtonClicked(self):
        imagePath="./source/assets/rattail.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)

    def vButtonClicked(self):
        imagePath="./source/assets/snakevenom.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def stopButtonClicked(self):
        if self.productWindow is None:
            self.productWindow = ProductWindowController()
        self.productWindow.show()

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