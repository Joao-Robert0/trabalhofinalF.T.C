class AFD:
    def __init__(self, estados, estado_inicial, estados_finais):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = {}

    def adicionar_transicao(self, de, simbolo, para):
        if de not in self.transicoes:
            self.transicoes[de] = {}
        self.transicoes[de][simbolo] = para

    def processar_entrada(self, entrada):
        estado_atual = self.estado_inicial

        for simbolo in entrada:
            if estado_atual in self.transicoes and simbolo in self.transicoes[estado_atual]:
                estado_atual = self.transicoes[estado_atual][simbolo]
                print(f'Transição: {simbolo} -> Estado: {estado_atual}')
            else:
                print('Erro: Transição inválida')
                return False

        return estado_atual in self.estados_finais

    @staticmethod
    def carregar_de_arquivo(caminho_arquivo):
        with open(caminho_arquivo, 'r') as file:
            linhas = file.readlines()

        # Lê os estados
        partes = linhas[0].strip().split()[1:]
        estados = set(partes)

        # Lê o estado inicial
        estado_inicial = linhas[1].strip().split()[1]

        # Lê os estados finais
        estados_finais = set(linhas[2].strip().split()[1:])

        automato = AFD(estados, estado_inicial, estados_finais)

        # Lê as transições
        for linha in linhas[3:]:
            if linha.strip() == '---':
                break
            partes = linha.split('->')
            estado_de = partes[0].strip()
            transicao = partes[1].split('|')
            estado_para = transicao[0].strip()
            simbolo = transicao[1].strip()
            automato.adicionar_transicao(estado_de, simbolo, estado_para)

        return automato

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
