'''
Created on 26/01/2013

@author: NADHINE
'''


class Tabuleiro():
    def __init__(self):
        self.tabuleiro = [0,1,2,3,4,5,6,7,8]
    
    def  mostraTabuleiro(self):
        print self.tabuleiro[0] ,'|',self.tabuleiro[1],'|',self.tabuleiro[2]
        print '___________'
        print self.tabuleiro[3] ,'|',self.tabuleiro[4],'|',self.tabuleiro[5]
        print '___________'
        print self.tabuleiro[6] ,'|',self.tabuleiro[7],'|',self.tabuleiro[8]


t = Tabuleiro()
t.mostraTabuleiro()