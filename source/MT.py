class MT:
    # Construtor da classe MT, inicializa os estados, estado inicial, estados finais e transições
    def __init__(self, estados, alfabeto_entrada, alfabeto_fita, estado_inicial, estados_finais):
        self.alfabeto_entrada = alfabeto_entrada  # Alfabeto de entrada do autômato
        self.alfabeto_fita = alfabeto_fita # Alfabeto da fita do autômato
        self.estados = estados  # Conjunto de estados do autômato
        self.estado_inicial = estado_inicial  # Estado inicial do autômato
        self.estados_finais = estados_finais  # Conjunto de estados finais do autômato
        self.transicoes = {}  # Dicionário para armazenar as transições

    # Método para adicionar uma transição ao autômato
    def adicionar_transicao(self, de, simbolo, escreve, direcao, para):
        if de not in self.transicoes:  # Se o estado de origem não tem transições ainda
            self.transicoes[de] = {}  # Inicializa o dicionário de transições para este estado
        self.transicoes[de][simbolo] = (escreve, direcao, para)  # Adiciona a transição para o estado de destino

    # Método para verificar se a entrada é válida
    def verificar_entrada(self, entrada):
        for simbolo in entrada:
            if simbolo not in self.alfabeto_entrada:
                print(f'Erro: Símbolo inválido "{simbolo}"')  # Imprime erro e retorna False
                return False
        return True

   # Método para processar uma entrada no autômato
    def processar_entrada(self, entrada):
        if not self.verificar_entrada(entrada):
            return False
        
        estado_atual = self.estado_inicial  # Começa no estado inicial

        fita = ['<'] + list(entrada)  # Adiciona o símbolo < no início da fita e converte a entrada em uma lista de caracteres para simular a fita
        posicao = 1 # Posição inicial na fita

        while estado_atual not in self.estados_finais:  # Continua até alcançar um estado final
            estado_anterior = estado_atual  # Salva o estado anterior
            simbolo_atual = fita[posicao]  # Lê o símbolo atual na fita
            if estado_atual in self.transicoes and simbolo_atual in self.transicoes[estado_atual]:  # Se há uma transição válida
                simbolo_escrito, direcao, estado_atual = self.transicoes[estado_atual][simbolo_atual]  # Obtém a transição
                fita[posicao] = simbolo_escrito  # Escreve o símbolo na fita
                print(f'Transição: {estado_anterior} -> {estado_atual}, Estado: {simbolo_escrito}, Direção: {direcao}')  # Imprime a transição
                if direcao == 'D':  # Move para a direita
                    posicao += 1
                elif direcao == 'E':  # Move para a esquerda
                    posicao -= 1
                if posicao < 0:  # Se a posição for negativa, adiciona um espaço em branco à esquerda
                    fita.insert(0, ' ')
                    posicao = 1
                elif posicao >= len(fita):  # Se a posição for além do final da fita, adiciona um espaço em branco à direita
                    fita.append(' ')
            else:
                print('Erro: Transição inválida')  # Se não há transição válida, imprime erro
                return False  # Retorna False indicando que a entrada não foi aceita
        print("Fita final:", "".join(fita)[1:-1])  # Imprime a fita final
        return estado_atual in self.estados_finais  # Retorna True indicando que a entrada foi aceita
    
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

        alfabeto_entrada = set(linhas[3].strip().split()[1:])  # Lê o alfabeto de entrada

        alfabeto_fita = set(linhas[4].strip().split()[1:])  # Lê o alfabeto da fita 

        automato = MT(estados, alfabeto_entrada, alfabeto_fita, estado_inicial, estados_finais)  # Cria uma instância do autômato

        # Lê as transições do autômato
        for linha in linhas[5:]:  # Para cada linha a partir da sexta linha
            if linha.strip() == '---':  # Se a linha contém '---', para de ler transições
                break
            partes = linha.split('->')  # Divide a linha na seta de transição
            estado_de = partes[0].strip()  # Pega o estado de origem
            transicao = partes[1].split('|')  # Divide a parte da transição nos componentes
            estado_para = transicao[0].strip()  # Pega o estado de destino
            simbolo = transicao[1].strip()  # Pega o símbolo de entrada
            escrita = transicao[2].strip()  # Pega o símbolo a ser escrito
            direcao = transicao[3].strip()  # Pega a direção da fita sem o \n no final
            automato.adicionar_transicao(estado_de, simbolo, escrita, direcao, estado_para)  # Adiciona a transição ao autômato

        return automato  # Retorna a instância do autômato

if __name__ == "__main__":
    try:
        automato = MT.carregar_de_arquivo("testes/testeMT.txt")
        entrada = "10"  # Entrada a ser processada
        entrada += "_"  # Adiciona o símbolo de fim de fita
        aceita = automato.processar_entrada(entrada)

        if aceita:
            print("Entrada aceita.")
        else:
            print("Entrada rejeitada.")
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")