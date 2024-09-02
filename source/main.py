from PySide6.QtWidgets import QApplication
from controller.MainWindowController import MainWindowController
from AFD import AFD
from AFN import AFN
from MT import MT
from Mealy import Mealy
from Moore import Moore
from APD import AP
import sys

def runGraphicalInterface():
    app = QApplication(sys.argv)  # Cria a aplicação Qt
    window = MainWindowController()  # Cria uma instância do controlador
    window.show()  # Exibe a janela principal
    sys.exit(app.exec())  # Inicia o loop de eventos da aplicação

if __name__ == "__main__":
    try:
        opçao = None
        caminhoArquivo = None

        if(sys.argv[-1] == "-g"):
            runGraphicalInterface()

        print("Olá, seja bem vindo, selecione qual autômato você deseja utilizar :");
        print("1) Autômato Finito Determinístico")
        print("2) Autômato Finito Não Determinístico")
        print("3) Autômato de Pilha Determinístico")
        print("==========Extras==========")
        print("4)Máquina de Mealy")
        print("5)Máquina de Moore")
        print("6)Máquina de Turing")
        opçao = input()

        dicionario = {
            "1":lambda: AFD.carregar_de_arquivo("Gramaticas/pocao_especificacao.txt"),
            "2":lambda: AFN.ler_arquivo_AFN("Gramaticas/p1.txt"),
            "3":lambda: AP.leitura_arquivo("Gramaticas/Pocao_Invisibilidade.txt"),
            "4":lambda: Mealy.carregar_de_arquivo("testes/testeMealy.txt"),
            "5":lambda: Moore.carregar_de_arquivo("testes/testeMoore.txt"),
            "6":lambda: MT.carregar_de_arquivo("testes/testeMT.txt")
        }
        automato = dicionario.get(opçao)();
        if opçao == "1":
            automato.processar_simbolo(input("Insira o simbolo do primeiro ingrediente da receita:\n "))
            while automato.estado_atual != "F":
                print("Deseja inserir mais um ingrediente? (s/n)")
                if input() == "n":
                    break
                automato.processar_simbolo(input("Qual ingrediete será inserido?\n"))
        elif opçao == "2":
            automato.transitar_AFN(input("Insira o simbolo do primeiro ingrediente da receita:\n "))
            while "F" not in automato.estados_atuais:
                print("Deseja inserir mais um ingrediente? (s/n)")
                if input() == "n":
                    break
                automato.transitar_AFN(input("Qual ingrediente será inserido?\n"))
        elif opçao == "3":
            automato.processar_entrada(input("Insira o simbolo do primeiro ingrediente da receita:\n "))
            while True:
                print("Deseja inserir mais um ingrediente? (s/n)")
                if input() == "n":
                    break
                automato.processar_entrada(input("Qual ingrediete será inserido?\n"))
            automato.resultado_total()
        else:
            entrada = input()  # Entrada a ser processada
            aceita = automato.processar_entrada(entrada)
            if aceita:
                print("Entrada aceita.")
            else:
                print("Entrada rejeitada.")
    
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")