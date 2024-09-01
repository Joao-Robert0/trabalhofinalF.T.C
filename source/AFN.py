class AFN:
    # Construtor da classe AFN, inicializa os estados, estado inicial, estados finais e estado_atual
    def __init__(self, estados, estados_iniciais, estados_finais,):
        self.estados = estados
        self.estados_iniciais = estados_iniciais
        self.estados_finais = estados_finais
        self.transicoes = {}
        self.estado_atual = estados_iniciais 

        # Método para adicionar transições

    def adicionar_transicaoAFN(self, estado_origem, simbolo, estado_destino):
        if estado_origem not in self.transicoes:
            self.transicoes[estado_origem] = {}
        if simbolo not in self.transicoes[estado_origem]:
            self.transicoes[estado_origem][simbolo] = []
        self.transicoes[estado_origem][simbolo].append(estado_destino)
    
    # Método para realizar uma transição
    def transitar_AFN(self, simbolo):
        novos_estados = []
        for estado in self.estado_atual:
            if estado in self.transicoes and simbolo in self.transicoes[estado]:
                novos_estados.extend(self.transicoes[estado][simbolo])
        self.estado_atual = novos_estados

    # Método para ler o arquivo de entrada e inicializar o AFN
    @classmethod
    def ler_arquivo_AFN(cls, nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
        
        estados = linhas[0].strip().split()
        estado_inicial = linhas[1].strip()
        estado_final = linhas[2].strip()
        transicoes = {}

        for linha in linhas[3:]:
            partes = linha.strip().split()
            estado_origem = partes[0]
            simbolo = partes[1]
            estado_destino = partes[2]

            if estado_origem not in transicoes:
                transicoes[estado_origem] = {}
            if simbolo not in transicoes[estado_origem]:
                transicoes[estado_origem][simbolo] = []
            transicoes[estado_origem][simbolo].append(estado_destino)

        afn = cls(estados, estado_inicial, estado_final)
        afn.transicoes = transicoes
        return afn