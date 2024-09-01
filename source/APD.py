class AP:
    def __init__(self, estados, alfabeto, estado_inicial, estados_finais, receita):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = {}
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        
        self.receita = receita
        self.pilha = []
        
    def get_tam_pilha(self):
        return len(self.pilha)
    
    def get_pilha(self):
        return self.pilha    
    
    def add_transicao(self, estado_atual, simbolo, proximo_estado, simbolos_empilha, simbolos_desempilha):
        if estado_atual not in self.transicoes:
            self.transicoes[estado_atual] = {}
        self.transicoes[estado_atual][simbolo] = (proximo_estado, simbolos_empilha, simbolos_desempilha)
        return True
    
    def verifica_simbolo(self, simbolo):
        if simbolo not in self.alfabeto:
            print("Este símbolo não está presente no alfabeto")
            return False
        else:
            return True
    
    @staticmethod
    def leitura_arquivo(local_arquivo):
        with open(local_arquivo, 'r') as arquivo:
            receita = local_arquivo
            linhas = arquivo.readlines()

        partes = linhas[0].strip().split(" ")[1:]
        estados = set(partes)

        estado_inicial = linhas[1].strip().split(": ")[1]
        estados_finais = linhas[2].strip().split(": ")[1]

        alfabeto = set()
        automato = AP(estados, alfabeto, estado_inicial, estados_finais, receita)

        for linha in linhas[3:]:
            if linha.strip() == "---":
                break
            partes = linha.split("->")
            estado_origem = partes[0].strip()
            transicao = partes[1].split('|')
            estado_destino = transicao[0].strip()
            simbolo, desempilha, empilha = transicao[1].strip().split('/')

            alfabeto.add(simbolo)
            automato.add_transicao(estado_origem, simbolo, estado_destino, empilha, desempilha)

        return automato

    def processar_entrada(self, entrada):
        estado_atual = self.estado_inicial
        self.pilha = []
        entrada = entrada.upper()
        
        for simbolo in entrada:
            if self.verifica_simbolo(simbolo) and estado_atual in self.transicoes and simbolo in self.transicoes[estado_atual]:
                proximo_estado, simbolos_empilha, simbolos_desempilha = self.transicoes[estado_atual][simbolo]

                for simbolo_desempilha in simbolos_desempilha:
                    if (not self.pilha or self.pilha[len(self.pilha)-1] != simbolo_desempilha) and (simbolo_desempilha != 'λ'):
                        print("Erro: símbolo a ser desempilhado não está no topo da pilha.")
                        return False
                    if simbolo_desempilha != 'λ':
                        self.pilha.pop(len(self.pilha)-1)
                    
                for simbolo_empilha in simbolos_empilha:
                    if simbolo_empilha != 'λ':
                        self.pilha.append(simbolo_empilha)

                estado_passado = estado_atual
                estado_atual = proximo_estado
                print(f"{estado_passado} -- {simbolo.lower()} --> {estado_atual}")
                
            else:
                print(f"Ingrediente não presente na receita de {self.receita}")
                return False
        
        self.receita = self.receita.split(".txt")[0]
        if estado_atual in self.estados_finais and len(self.pilha) == 0:
            print(f"Poção de {self.receita} realizada com sucesso")
            return True
        else:
            print(f"Poção de {self.receita} com a quantidade errada de ingredientes")
            return False