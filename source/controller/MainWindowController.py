import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from view.MainWindowView import Ui_mainWindow

class MainWindowController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()  # Instancia a classe da interface
        self.ui.setupUi(self)  # Configura a interface no QMainWindow

        # Conecta os botões às funções do controlador
        self.ui.afdButton.clicked.connect(self.afd_button_clicked)
        self.ui.apdButton.clicked.connect(self.apd_button_clicked)
        self.ui.mooreButton.clicked.connect(self.moore_button_clicked)
        self.ui.mealyButton.clicked.connect(self.mealy_button_clicked)

    def afd_button_clicked(self):
        print("Botão AFD clicado!")
        # Aqui você pode adicionar a lógica específica para o botão AFD

    def apd_button_clicked(self):
        print("Botão APD clicado!")
        # Aqui você pode adicionar a lógica específica para o botão APD

    def moore_button_clicked(self):
        print("Botão Moore clicado!")
        # Aqui você pode adicionar a lógica específica para o botão Moore

    def mealy_button_clicked(self):
        print("Botão Mealy clicado!")
        # Aqui você pode adicionar a lógica específica para o botão Mealy