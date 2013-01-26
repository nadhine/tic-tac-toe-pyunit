'''
Created on 26/01/2013

@author: NADHINE
'''
import unittest
import tictactoe

class ChecarEntradaValida(unittest.TestCase):
    def checarJogador(self):
        jogo = tictactoe
        numJogador = jogo.numJogador
        assert numJogador == 1 or numJogador == 2
# def checarNumeroPosicao(self):
#    assert self.entrada <= 0 and self.entrada >=8
    
testCase = ChecarEntradaValida()
        
     
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    