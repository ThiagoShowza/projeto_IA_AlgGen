# -*- coding: utf-8 -*-
"""
Algoritmo Genético

"""
import numpy as np

class AlgoritmoGenetico:
    def __init__(self, TAM_POP, TAM_GENE):
        print("Algoritmo Genético")
        self.TAM_POP = TAM_POP
        self.TAM_GENE = TAM_GENE
        self.POP = []
        self.POP_AUX = []
        self.aptidao = []
        self.aptidao_perc = [] #porcentagem
        self.populacao_inicial()
    
    def populacao_inicial(self):
        print("Criando pupulação inicial!")
        
        for i in range(self.TAM_POP):
            self.POP.append(np.random.randint(0, 2, self.TAM_GENE))

    def pre_roleta(self):
        aptidao_total = sum(self.aptidao)
        self.aptidao_perc = []
        
        for i in range(self.TAM_POP):
            x = (self.aptidao[i] * 100)/aptidao_total
            self.aptidao_perc.append(x)
            x = 0

    def roleta(self):
        sorteado = np.random.uniform(0.1, 100.1)
        quintal = 0.0
        for i in range(self.TAM_POP):
            quintal += self.aptidao_perc[i]
            
            if quintal > sorteado:
                return i
        return 0

    def operadores_geneticos(self):
        tx_cruzamento_simples = 30
        tx_cruzamento_uniforme = 70
        tx_elitismo = 
        tx_mutacao = 2
        
        self.POP_AUX = []
        
        self.avaliacao()
        self.pre_roleta()
        
        ## cruzamento simples
        qtd = (self.TAM_POP * tx_cruzamento_simples)/100
        for i in range(qtd):
            pai1 = self.roleta()
            pai2 = self.roleta()
            while pai1 == pai2:
                pai2 = self.roleta()
            self.cruzamento_simples(pai1, pai2)
        
        ## cruzamento uniforme
        qtd = (self.TAM_POP * tx_cruzamento_uniforme)/100
        for i in range(qtd):
            pai1 = self.roleta()
            pai2 = self.roleta()
            while pai1 == pai2:
                pai2 = self.roleta()
            self.cruzamento_uniforme(pai1, pai2)  
        
        ## GARANTIR O TAMANHO POPULACIONAL.
        
         ## mutação
        qtd = (self.TAM_POP * tx_mutacao)/100
        for i in range(qtd):
            quem = np.random.randint(0, self.TAM_POP)
            self.mutacao(quem)
        
    def cruzamento_simples(self, pai1, pai2):
        print("Cruzamento com 1 ponto de corte.")
        
        desc1 = np.zeros(self.TAM_GENE, dtype=int)
        desc2 = np.zeros(self.TAM_GENE, dtype=int)
        
        for i in range(self.TAM_GENE):
            if i < self.TAM_GENE/2:
                desc1[i] = self.POP[pai1][i]
                desc2[i] = self.POP[pai2][i]
            else:
                desc1[i] = self.POP[pai2][i]
                desc2[i] = self.POP[pai1][i]
                
        self.POP_AUX.append(desc1)
        self.POP_AUX.append(desc2)
                
    def cruzamento_uniforme(self, pai1, pai2):
        print("Cruzamento uniforme.")
        
        desc1 = np.zeros(self.TAM_GENE, dtype=int)
        desc2 = np.zeros(self.TAM_GENE, dtype=int)
        
        for i in range(self.TAM_GENE):
            if 0 == np.random.randint(0, 2):
                desc1[i] = self.POP[pai1][i]
                desc2[i] = self.POP[pai2][i]
            else:
                desc1[i] = self.POP[pai2][i]
                desc2[i] = self.POP[pai1][i]
                
        self.POP_AUX.append(desc1)
        self.POP_AUX.append(desc2)    
    
    ## Função de mutação. Deve ser utilizada na POP_AUX
    ## após sua população estar completa.
    def mutacao(self, i):
        g = np.random.randint(0, self.TAM_GENE)
        if self.POP_AUX[i][g] == 0:
            self.POP_AUX[i][g] = 1
        else:
            self.POP_AUX[i][g] = 0
            
    def avaliacao(self):
        livros = []
        livros.append(0.6)
        livros.append(1.6)
        livros.append(0.8)
        livros.append(0.7)
        livros.append(1.2)
        livros.append(0.3)
        livros.append(0.1)
        livros.append(1.4)
        livros.append(1.3)
        livros.append(0.5)
        
        self.aptidao = []
        
        for i in range(self.TAM_POP):
            peso = 0.0
            for g in range(self.TAM_GENE):
                peso += (self.POP[i][g] * livros[g])
            self.aptidao.append(peso)
        