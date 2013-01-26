'''
Created on 26/01/2013

@author: NADHINE
'''
import unittest
import tabuleiro


class ChecarTabuleiro(unittest.TestCase):
    def checarTab(self):
        tab = tabuleiro
        tam = len(tab)
        esperado = 9
        assert tam == esperado

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    