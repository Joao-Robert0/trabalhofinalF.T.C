from PySide6.QtWidgets import QMainWindow
from view.ProductWindowView import Ui_ProductWindow

class ProductWindowController(QMainWindow):
    def __init__(self):
        super(ProductWindowController, self).__init__()
        self.ui = Ui_ProductWindow()
        self.ui.setupUi(self)

        # TODO: Lógica para a mudança da imagem
        # TODO: Lógica para a mudança do Label

        self.ui.stopButton.clicked.connect(self.stopButtonClicked)

    
    def stopButtonClicked(self):
        self.close()

    