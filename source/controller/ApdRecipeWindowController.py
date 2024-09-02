from PySide6.QtWidgets import QMainWindow
from view.ApdRecipeWindowView import Ui_apdRecipeWindow
import model.SharedData

class ApdRecipeWindowController(QMainWindow):
    def __init__(self):
      super(ApdRecipeWindowController, self).__init__()
      self.ui = Ui_apdRecipeWindow()
      self.ui.setupUi(self)

      self.ui.invisibilidadeButton.clicked.connect(self.invisibilidadeButtonClicked)
      self.ui.restauracaoButton.clicked.connect(self.restauracaoButtonClicked)

    def invisibilidadeButtonClicked(self):
       model.SharedData.recipePath("Gramaticas/Pocao_Invisibilidade.txt")
       model.SharedData.recipeName("a Poção de Invisibilidade")
       self.close()

    def restauracaoButtonClicked(self):
        model.SharedData.recipePath("Gramaticas/Pocao_Tripla.txt")
        model.SharedData.recipeName("a Poção de Restauração")