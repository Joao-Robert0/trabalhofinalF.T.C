from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import (QMovie, QPixmap)
from PySide6.QtCore import QTimer
from view.AfdWindowView import Ui_afdWindow
from controller.ProductWindowController import ProductWindowController
#from controller.AfdRecipeWindowController import AfdRecipeWindowController
from AFD import AFD
import model.SharedData

class AFDWindowController(QMainWindow):
    def __init__(self):
        super(AFDWindowController, self).__init__()
        self.ui = Ui_afdWindow()
        self.ui.setupUi(self)

        #self.afdRecipeWindow = AfdRecipeWindowController() #Janela que vai permitir escolher a receita
        #self.afdRecipeWindow.show()
        
        self.automato = AFD.carregar_de_arquivo(model.SharedData.recipePath)


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
        self.automato.processar_simbolo("a")
        imagePath = "./source/assets/waterbottle.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def bButtonClicked(self):
        self.automato.processar_simbolo("b")
        imagePath="./source/assets/butterflywing.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def dButtonClicked(self):
        self.automato.processar_simbolo("d")
        imagePath="./source/assets/finger.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def mButtonClicked(self):
        self.automato.processar_simbolo("m")
        imagePath="./source/assets/batwing.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)

    def oButtonClicked(self):
        self.automato.processar_simbolo("o")
        imagePath = "./source/assets/bonemeal.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def pButtonClicked(self):
        self.automato.processar_simbolo("p")
        imagePath="./source/assets/petals.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def rButtonClicked(self):
        self.automato.processar_simbolo("r")
        imagePath="./source/assets/rattail.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)

    def vButtonClicked(self):
        self.automato.processar_simbolo("v")
        imagePath="./source/assets/snakevenom.png"
        self.pixmap = QPixmap(imagePath)
        self.ui.ingredientLabel.setPixmap(self.pixmap)
        self.ui.ingredientLabel.setVisible(True)
        self.timer.start(50)
    
    def stopButtonClicked(self):
        if self.automato.estado_atual == "F":
            model.SharedData.sucessoFlag = True
        if self.productWindow is None:
            self.productWindow = ProductWindowController()
        self.automato.reiniciar()
        model.SharedData.sucessoFlag = False
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