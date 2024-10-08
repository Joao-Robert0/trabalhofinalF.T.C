from PySide6.QtWidgets import QMainWindow
from view.AfdRecipeWindowView import Ui_afdRecipeWindow
from controller.AfdWindowController import AFDWindowController
import model.SharedData

class AfdRecipeWindowController(QMainWindow):
   def __init__(self):
      super(AfdRecipeWindowController, self).__init__()
      self.ui = Ui_afdRecipeWindow()
      self.ui.setupUi(self)

      self.afdWindow = None

      self.ui.vitalidadeButton.clicked.connect(self.vitalidadeButtonClicked)
      self.ui.asasButton.clicked.connect(self.asasButtonClicked)
      self.ui.miniaturizacaoButton.clicked.connect(self.miniaturizacaoButtonClicked)
      self.ui.sussurroButton.clicked.connect(self.sussurroButtonClicked)
      self.ui.metamorfoseButton.clicked.connect(self.metamorfoseButtonClicked)
      self.ui.percepcaoButton.clicked.connect(self.percepcaoButtonClicked)
   
   def vitalidadeButtonClicked(self):
      model.SharedData.recipePath = "Gramaticas/p1.txt"
      model.SharedData.recipeName = "o Elixir da Vitalidade"
      if self.afdWindow is None:
            self.afdWindow = AFDWindowController()
      self.afdWindow.show()
      self.close()


   def asasButtonClicked(self):
      model.SharedData.recipePath = "Gramaticas/p2.txt"
      model.SharedData.recipeName = "o Elixr das Asas Celestes"
      if self.afdWindow is None:
            self.afdWindow = AFDWindowController()
      self.afdWindow.show()
      self.close()

   def miniaturizacaoButtonClicked(self):
      model.SharedData.recipePath = "Gramaticas/p3.txt"
      model.SharedData.recipeName = "o Elixir da Miniaturização"
      if self.afdWindow is None:
            self.afdWindow = AFDWindowController()
      self.afdWindow.show()
      self.close()

   def sussurroButtonClicked(self):
      model.SharedData.recipePath = "Gramaticas/p4.txt"
      model.SharedData.recipeName = "a Poção do Sussurro Sombrio"
      if self.afdWindow is None:
            self.afdWindow = AFDWindowController()
      self.afdWindow.show()
      self.close()

   def metamorfoseButtonClicked(self):
      model.SharedData.recipePath = "Gramaticas/p5.txt"
      model.SharedData.recipeName = "o Néctar da Metamorfose"
      if self.afdWindow is None:
            self.afdWindow = AFDWindowController()
      self.afdWindow.show()
      self.close()

   def percepcaoButtonClicked(self):
      model.SharedData.recipePath = "Gramaticas/p6.txt"
      model.SharedData.recipeName = "o Elixir da Percepção Aguçada"
      if self.afdWindow is None:
            self.afdWindow = AFDWindowController()
      self.afdWindow.show()
      self.close()
