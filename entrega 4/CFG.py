# -*-coding: cp1252 -*-

class CFG(object):

    def __init__(self,nonterminals,terminals,rules,start):
        self.nonterminals = nonterminals
        self.terminals = terminals
        self.rules = rules
        self.start = start


    def test(self,word):
        contador = 0
        states = []
        dicc = {}
        for i in word:
            temp_rule = []
            for key in self.rules.keys():
                for eleState in self.rules[(key)]:
                    lista = list(self.rules[(key)])
                    if(i in lista):
                        temp_rule.append(key)
            dicc[contador+1,contador+1] = list(set(temp_rule))
            contador+=1

        fila = 2
        columna = 1
        while(fila!=len(word)):
            for i in range(1,len(dicc)+1):
                states+=[dicc[(columna,i)]]
            
            dicc = {}
            
                
        
            
            
        #return dicc
            
            



####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
            
##    def test(self, word):
##        contador = 1
##        l = len(word)
##        #Inicializar la matriz
##        X = []
##        for i in range(l):
##            X.append([['']])
##            for j in range(l-1):
##                X[i].append([''])
##
##        
##        # Llenar primera fila de la piramide
##        for i in range(l):
##            for var in self.rules.keys():
##                for rule in self.rules[var]:
##                    if rule == word[i]:
##                        X[i][i].append(var)
##            X[i][i] = list(set(X[i][i]))
##
##        while(contador!=len(word)):
##            for i in range(l-contador):
##                for var1 in X[i][i]:
##                    for var2 in X[i+1][i+1]:
##                        for var in self.rules.keys():
##                            for rule in self.rules[var]:
##                                if rule == var1+var2:
##                                    X[i][i+1].append(var)           
##                X[i][i+1] = list(set(X[i][i+1]))
##            contador+=1
##        print 'Primera fila:' 
##        for i in range(l):
##            print X[i][i]         
##
##        print 'Segunda fila:'
##        
##        for i in range(l-1):
##            print X[i][i+1]    
##
##        return True

        
