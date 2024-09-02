from PySide6.QtWidgets import QMainWindow
from view.MainWindowView import Ui_mainWindow
from controller.AfdWindowController import AFDWindowController
from controller.ApdWindowController import APDWindowController

class MainWindowController(QMainWindow):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # Conecte os botões às suas funções
        self.ui.afdButton.clicked.connect(self.afd_button_clicked)
        self.ui.apdButton.clicked.connect(self.apd_button_clicked)
        #self.ui.mooreButton.clicked.connect(self.moore_button_clicked)
        #self.ui.mealyButton.clicked.connect(self.mealy_button_clicked)

        self.afdWindow = None #Essa aqui vai ser a janela do AFD
        self.apdWindow = None #Essa aqui vai ser a janela da APD

    def afd_button_clicked(self):
        print("AFD Button clicked - Caldeirão Finito Deterministico")
        if self.afdWindow is None:
            self.afdWindow = AFDWindowController()
        self.afdWindow.show()

    def apd_button_clicked(self):
        print("APD Button clicked - Caldeirão de Pilha Deterministico")
        if self.apdWindow is None:
            self.apdWindow = APDWindowController()
        self.apdWindow.show()
        
        #self

    #def moore_button_clicked(self):
        #print("Moore Button clicked - Calculadora de Moore")

    #def mealy_button_clicked(self):
        #print("Mealy Button clicked - Calculadora de Mealy")