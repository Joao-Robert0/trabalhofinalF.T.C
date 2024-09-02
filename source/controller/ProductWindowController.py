from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap
from view.ProductWindowView import Ui_ProductWindow
import model.SharedData

class ProductWindowController(QMainWindow):
    def __init__(self):
        super(ProductWindowController, self).__init__()
        self.ui = Ui_ProductWindow()
        self.ui.setupUi(self)

        if model.SharedData.sucessoFlag == False:
            imagePath = "./source/assets/failedpotion.png"
            self.ui.descriptionLabel.setText("Você não misturou os itens corretamente !")
            self.pixmap = QPixmap(imagePath)
            self.ui.productLabel.setPixmap(self.pixmap)
        
        # TODO: Lógica para a mudança da imagem em caso de sucesso
        # TODO: Lógica para a mudança do Label em caso de sucesso

        self.ui.stopButton.clicked.connect(self.stopButtonClicked)

    
    def stopButtonClicked(self):
        self.close()

    