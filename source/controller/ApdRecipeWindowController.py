from PySide6.QtWidgets import QMainWindow
from view.ApdRecipeWindowView import Ui_apdRecipeWindow
import model.SharedData

class ApdRecipeWindowController(QMainWindow):
    def __init__(self):
      super(ApdRecipeWindowController, self).__init__()
      self.ui = Ui_apdRecipeWindow()
      self.ui.setupUi(self)
