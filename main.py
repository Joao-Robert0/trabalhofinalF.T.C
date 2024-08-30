from AFD import AFD

if __name__ == "__main__":
    try:
        automato = AFD.carregar_de_arquivo("testes/teste0.txt")
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