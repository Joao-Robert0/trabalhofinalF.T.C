class Mealy:
    # Construtor da classe Mealy, inicializa os estados, estado inicial, e transições
    def __init__(self, estados, alfabeto_entrada, alfabeto_saida, estado_inicial):
        self.alfabeto_entrada = alfabeto_entrada  # Alfabeto de entrada do autômato
        self.alfabeto_saida = alfabeto_saida  # Alfabeto de saída do autômato
        self.estados = estados  # Conjunto de estados do autômato
        self.estado_inicial = estado_inicial  # Estado inicial do autômato
        self.transicoes = {}  # Dicionário para armazenar as transições

    # Método para adicionar uma transição ao autômato
    def adicionar_transicao(self, de, simbolo, para, saida):
        if de not in self.transicoes:  # Se o estado de origem não tem transições ainda
            self.transicoes[de] = {}  # Inicializa o dicionário de transições para este estado
        self.transicoes[de][simbolo] = (para, saida)  # Adiciona a transição para o estado de destino e a saída

    # Método para verificar se a entrada é válida
    def verificar_entrada(self, entrada):
        for simbolo in entrada:
            if simbolo not in self.alfabeto_entrada:
                print(f'Erro: Símbolo inválido "{simbolo}"')  # Imprime erro e retorna False
                return False
        return True

    # Método para processar uma entrada no autômato
    def processar_entrada(self, entrada):
        saida = ''  # Inicializa a saída
        if self.verificar_entrada(entrada):
            estado_atual = self.estado_inicial  # Começa no estado inicial
            for simbolo in entrada:  # Para cada símbolo na entrada
                if estado_atual in self.transicoes and simbolo in self.transicoes[estado_atual]:  # Se há uma transição válida
                    estado_para, saida_transicao = self.transicoes[estado_atual][simbolo]  # Move para o próximo estado e obtém a saída
                    print(f'Transição: {simbolo} -> Estado: {estado_para} - Saída: {saida_transicao}')  # Imprime a transição
                    saida += saida_transicao  # Adiciona a saída da transição
                    estado_atual = estado_para  # Atualiza o estado atual
                else:
                    print('Erro: Transição inválida')  # Se não há transição válida, imprime erro
                    return False  # Retorna False indicando que a entrada não foi aceita
            print("Saída final:", saida)  # Imprime a saída final
            return True  # Retorna True se o estado final é um estado de aceitação
        else:
            return False

    # Método estático para carregar um autômato de um arquivo
    @staticmethod
    def carregar_de_arquivo(caminho_arquivo):
        estados = set()  # Conjunto para armazenar os estados

        with open(caminho_arquivo, 'r') as file:  # Abre o arquivo para leitura
            linhas = file.readlines()  # Lê todas as linhas do arquivo

        # Lê os estados do autômato
        partes = linhas[0].strip().split()[1:]  # Divide a linha e ignora o primeiro elemento
        for parte in partes:  # Para cada parte
            estados.add(parte)  # Adiciona o estado ao conjunto

        # Lê o estado inicial do autômato
        estado_inicial = linhas[1].strip().split()[1]  # Divide a linha e pega o segundo elemento

        alfabeto_entrada = set(linhas[2].strip().split()[1:])  # Lê o alfabeto de entrada

        alfabeto_saida = set(linhas[3].strip().split()[1:])  # Lê o alfabeto de saída

        automato = Mealy(estados, alfabeto_entrada, alfabeto_saida, estado_inicial)  # Cria uma instância do autômato

        # Lê as transições do autômato
        for linha in linhas[4:]:  # Para cada linha a partir da quinta linha
            if linha.strip() == '---':  # Se a linha contém '---', para de ler transições
                break
            partes = linha.split('->')  # Divide a linha na seta de transição
            estado_de = partes[0].strip()  # Pega o estado de origem
            transicao = partes[1].split('|')  # Divide a parte da transição no símbolo e na saída
            estado_para = transicao[0].strip()  # Pega o estado de destino
            simbolo, saida = transicao[1].strip().split('/')  # Pega o símbolo de transição e a saída
            automato.adicionar_transicao(estado_de, simbolo, estado_para, saida)  # Adiciona a transição ao autômato

        return automato  # Retorna a instância do autômato

if __name__ == "__main__":
    try:
        automato = Mealy.carregar_de_arquivo("testes/testeMealy.txt")
        entrada = "10"  # Entrada a ser processada
        aceita = automato.processar_entrada(entrada)

        if aceita:
            print("Entrada aceita.")
        else:
            print("Entrada rejeitada.")
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")