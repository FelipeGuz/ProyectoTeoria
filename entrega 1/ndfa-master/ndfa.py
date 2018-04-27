# -*- coding: cp1252 -*-
import logging


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

    
    def busqueda(self,string,lista_f,n):
        for i in self.alphabet: #Evalua cada elemento del alfabeto
            print "Este es el string: ",list(string)
            string+=i #Agrega al string el valor del alfabeto
            print "Este es el valor de i: ",i
            print "Este es el tamaño del string al sumar i: ",len(string)
            print "Este es el valor del test: ",self.test(string) #Evalua si el string llega a un estado de aceptacion
            if(self.test(string)==False):#Si el string no llega
                if(len(string)<n): #Si no llega y el tamanño del estring es menor al valor ingresado
                    print "Valor del string para evaluar",len(string)
                    print "-----------------"
                    self.busqueda(string,lista_f,n)
                elif(len(string)==n): #Si no llega y el tamaño del string es igual a n
                    print "Llego a",n
                    string = ""
                    self.busqueda(string,lista_f,n)
                    break
            else: #Si el string llega
                print "Es correcto"
                lista_f.append(string)
                print "Esta es la lista final: ",lista_f
                string = ""
                print "----------------------"
                break

    def languaje(self,n):
        lista_f=[]
        #vuelta=0
        string=""
        self.busqueda(string,lista_f,n)
        return lista_f



