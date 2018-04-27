# -*- coding: cp1252 -*-
import logging
import itertools

class DFA(object):

    def __init__(self, states, alphabet, transitions, start, accepts):
        assert start in states, \
                'Start state must be a valid state.'
        assert set(accepts).issubset(set(states)), \
                'Accept states must be a subset of states.'
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.accepts = accepts

    def test(self, word):
        current_state = self.start
        logging.info('Testing word "%s"...' % word)
        logging.debug('Initial state: %s' % current_state)
        for symbol in word:
            logging.debug('Current symbol: %s' % symbol)
            assert symbol in self.alphabet, \
                    'Symbol "%s" must be in alphabet.' % symbol
            current_state = self.transitions[(current_state, symbol)]
            assert current_state in self.states, \
                    'Current state must be a valid state.'
            logging.debug('New state: %s' % current_state)
        logging.debug('Final state: %s' % current_state)
        logging.info('Accepted: %s\n' % (current_state in self.accepts))
        return current_state in self.accepts

    def generateLenguage(self, b):
        lista_total=[] #lista donde est�n todos los string posibles de longitud menor a b y mayor o igual a cero
        lista_aceptada = [] #lista donde est�n los string aceptados por la funci�n test
        elementosTotales = 0 #Contador de los elementos en lista_total
        string = "" #Variable string que recibe cada posibilidad de construcci�n y con la que se eval�a
        for i in range(b +1): #Construcci�n de todos los caminos posibles del aut�mata
            a = list(itertools.product(self.alphabet, repeat = i))
            lista_total.append(a)
        for i in lista_total: #Evaluaci�n de cada elemento de la lista lista_total
            for ev in i:
                elementosTotales+=1
                for op in ev:
                    string+=op #Agrega los elementos de cada posible camino al string
                evaluacion = self.test(string) #Eval�a si el string es un camino aceptado
                if(evaluacion==True):#Si el string es aceptado lo agrega a la lista lista_aceptada
                    lista_aceptada.append(string)
                string=""
        totalAceptado = len(lista_aceptada)
        print "De %r elementos evaluados, solo %r son caminos aceptados" %(elementosTotales,totalAceptado)
        return lista_aceptada
            
            
