'''
Created on 26/01/2013

@author: NADHINE
'''



import tabuleiro
        

class jogodaVelha():
    def __init__(self):
        self.tabuleiro = tabuleiro()
        self.tabuleiro.mostraTabuleiro()
        self.numJogador = 1
    def entrada(self):
        self.entrada = input("Jogador %i digite uma posicao valida: " %(self.numJogador,))
    def jogadas(self,tabuleiro,entrada,numJogador):
        if tabuleiro[self.entrada] != 'x' or tabuleiro[self.entrada] != 'o':
            if self.numJogador == 1:
                self.entrada = 'x'
            else:
                self.entrada = 'o'
        else:
            print "jogada invalida!!!"  
    def jogo(self):
        pass
            
                 
            
        

jogo = jogodaVelha()
jogo.entrada()
        

