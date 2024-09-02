class AFN:
    # Construtor da classe AFN, inicializa os estados, estado inicial, estados finais e estado_atual
    def __init__(self, estados, estado_inicial, estados_finais):
        self.estados = estados  # Conjunto de estados do autômato
        self.estado_inicial = estado_inicial  # Estado inicial do autômato
        self.estados_finais = estados_finais  # Conjunto de estados finais do autômato
        self.transicoes = {}  # Dicionário para armazenar as transições
        self.estados_atuais = {estado_inicial}  # Conjunto de estados atuais

    # Método para adicionar transições
    def adicionar_transicaoAFN(self, estado_origem, simbolo, estado_destino):
        if estado_origem not in self.transicoes:  # Se o estado de origem não tem transições ainda
            self.transicoes[estado_origem] = {}  # Inicializa o dicionário de transições para este estado
        if simbolo not in self.transicoes[estado_origem]:  # Se o símbolo não tem transições ainda
            self.transicoes[estado_origem][simbolo] = []  # Inicializa a lista de estados de destino para este símbolo
        self.transicoes[estado_origem][simbolo].append(estado_destino)  # Adiciona o estado de destino à lista

    # Método para realizar uma transição
    def transitar_AFN(self, simbolo):
        novos_estados = set()  # Conjunto para armazenar os novos estados após a transição
        for estado in self.estados_atuais:  # Para cada estado atual
            if estado in self.transicoes and simbolo in self.transicoes[estado]:  # Se há uma transição válida
                novos_estados.update(self.transicoes[estado][simbolo])  # Adiciona os estados de destino ao conjunto
        if not novos_estados:  # Se não há novos estados, a transição é inválida
            print('Erro: Transição inválida')
            return False
        self.estados_atuais = novos_estados  # Atualiza os estados atuais
        print(f'Transição: {simbolo} -> Estados: {self.estados_atuais}')  # Imprime a transição
        return True  # Retorna True indicando que a transição foi realizada com sucesso

    # Método para verificar se algum estado atual é um estado final
    def verificar_estado_final(self):
        return any(estado in self.estados_finais for estado in self.estados_atuais)  # Retorna True se algum estado atual é um estado final

    # Método para reiniciar o autômato
    def reiniciar(self):
        self.estados_atuais = {self.estado_inicial}  # Reseta os estados atuais para os estados iniciais

    # Método para ler o arquivo de entrada e inicializar o AFN
    @classmethod
    def ler_arquivo_AFN(cls, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

        # Extrair estados
        estados = set(linhas[0].strip().replace("Q: ", "").split())

        # Extrair estado inicial
        estado_inicial = linhas[1].strip().replace("I: ", "").split()[0]

        # Extrair estados finais
        estados_finais = set(linhas[2].strip().replace("F: ", "").split())

        # Construir dicionário de transições
        transicoes = {}
        for linha in linhas[3:]:
            if linha.strip() == "---":
                break
            partes = linha.strip().split(" -> ")
            estado_origem = partes[0].strip()
            destino_simbolos = partes[1].split(" | ")
            estado_destino = destino_simbolos[0].strip()
            simbolos = destino_simbolos[1].split()

            if estado_origem not in transicoes:
                transicoes[estado_origem] = {}
            for simbolo in simbolos:
                if simbolo not in transicoes[estado_origem]:
                    transicoes[estado_origem][simbolo] = []
                transicoes[estado_origem][simbolo].append(estado_destino)

        afn = cls(estados, estado_inicial, estados_finais)
        afn.transicoes = transicoes
        return afn