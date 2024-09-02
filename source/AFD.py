class AFD:
    # Construtor da classe AFD, inicializa os estados, estado inicial, estados finais e transições
    def __init__(self, estados, estado_inicial, estados_finais):
        self.estados = estados  # Conjunto de estados do autômato
        self.estado_inicial = estado_inicial  # Estado inicial do autômato
        self.estados_finais = estados_finais  # Conjunto de estados finais do autômato
        self.transicoes = {}  # Dicionário para armazenar as transições
        self.estado_atual = estado_inicial

    # Método para adicionar uma transição ao autômato
    def adicionar_transicao(self, de, simbolo, para):
        if de not in self.transicoes:  # Se o estado de origem não tem transições ainda
            self.transicoes[de] = {}  # Inicializa o dicionário de transições para este estado
        self.transicoes[de][simbolo] = para  # Adiciona a transição para o estado de destino

    # Método para processar uma entrada no autômato
    def processar_simbolo(self, simbolo):
        if self.estado_atual in self.transicoes and simbolo in self.transicoes[self.estado_atual]:  # Se há uma transição válida
            self.estado_atual = self.transicoes[self.estado_atual][simbolo]  # Move para o próximo estado
            print(f'Transição: {simbolo} -> Estado: {self.estado_atual}')  # Imprime a transição
        else:
            print('Erro: Transição inválida')  # Se não há transição válida, imprime erro
            return False  # Retorna False indicando que o símbolo não foi aceito
        return True  # Retorna True indicando que a transição foi realizada com sucesso

    # Método para verificar se o estado atual é um estado final
    def verificar_estado_final(self):
        return self.estado_atual in self.estados_finais  # Retorna True se o estado atual é um estado final

    # Método para reiniciar o autômato para o estado inicial
    def reiniciar(self):
        self.estado_atual = self.estado_inicial  # Reseta o estado atual para o estado inicial


    # Método estático para carregar um autômato de um arquivo
    @staticmethod
    def carregar_de_arquivo(caminho_arquivo):
        with open(caminho_arquivo, 'r') as file:  # Abre o arquivo para leitura
            linhas = file.readlines()  # Lê todas as linhas do arquivo

        # Lê os estados do autômato
        partes = linhas[0].strip().split()[1:]  # Divide a linha e ignora o primeiro elemento
        estados = set(partes)  # Cria um conjunto de estados

        # Lê o estado inicial do autômato
        estado_inicial = linhas[1].strip().split()[1]  # Divide a linha e pega o segundo elemento

        # Lê os estados finais do autômato
        estados_finais = set(linhas[2].strip().split()[1:])  # Divide a linha e cria um conjunto de estados finais

        automato = AFD(estados, estado_inicial, estados_finais)  # Cria uma instância do autômato

        # Lê as transições do autômato
        for linha in linhas[3:]:  # Para cada linha a partir da quarta linha
            if linha.strip() == '---':  # Se a linha contém '---', para de ler transições
                break
            partes = linha.split('->')  # Divide a linha na seta de transição
            estado_de = partes[0].strip()  # Pega o estado de origem
            transicao = partes[1].split('|')  # Divide a parte da transição no símbolo
            estado_para = transicao[0].strip()  # Pega o estado de destino
            simbolo = transicao[1].strip()  # Pega o símbolo de transição
            automato.adicionar_transicao(estado_de, simbolo, estado_para)  # Adiciona a transição ao autômato

        return automato  # Retorna a instância do autômato
