from AFD import AFD
from MT import MT
from Mealy import Mealy
from Moore import Moore
import sys

if __name__ == "__main__":
    try:
        opçao = None
        caminhoArquivo = None

        if(sys.argv[-1] == "-g"):
            # Insira aqui código da interface gráfica
            print("Em breve modo gráfico")
            sys.exit()

        print("Olá, seja bem vindo, selecione qual autômato você deseja utilizar :");
        print("1) Autômato Finito Determinístico")
        print("2) Autômato de Pilha Determinístico")
        print("==========Extras==========")
        print("3)Máquina de Mealy")
        print("4)Máquina de Moore")
        print("5)Máquina de Turing")
        opçao = input()

        dicionario = {
            "1":lambda: AFD.carregar_de_arquivo("Gramaticas/p1.txt"),
            "2":lambda: print("Autômato de pilha ainda não implementado"),
            "3":lambda: Mealy.carregar_de_arquivo("testes/testeMealy.txt"),
            "4":lambda: Moore.carregar_de_arquivo("testes/testeMoore.txt"),
            "5":lambda: MT.carregar_de_arquivo("testes/testeMT.txt")
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
            print("Autômato de pilha ainda não implementado")
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
