from AFD import AFD
from MT import MT
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
        opçao = input();
        #caminhoArquivo = input("Insira o caminho do arquivo com a receita :")
        #caminhoArquivo = "testes/teste0.txt"

        dicionario = {
            "1":lambda: AFD.carregar_de_arquivo("testes/teste0.txt"),
            "2":lambda: print("Autômato de pilha ainda não implementado"),
            "3":lambda: print("Máquina de Mealy ainda não implementada"),
            "4":lambda: print("Máquina de Moore ainda não implementada"),
            "5":lambda: MT.carregar_de_arquivo("testes/testeMT.txt")
        }
        automato = dicionario.get(opçao)();
        entrada = "apo"  # Entrada a ser processada
        aceita = automato.processar_entrada(entrada)

        if aceita:
            print("Entrada aceita.")
        else:
            print("Entrada rejeitada.")
    
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")
