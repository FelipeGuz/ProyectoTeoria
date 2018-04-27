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
        #print self.accepts
        current_state = self.start
        #print "Inicial: ",current_state ################
        for symbol in word:
            #print "Simbolos: ",symbol ##############
            logging.debug('Current symbol: %s' % symbol)
            #print "Current state: ",current_state
            #print "Transicion: ",self.transitions[(current_state, symbol)] #############
            current_state = self.transitions[(current_state, symbol)]
            #print current_state in self.accepts
        return current_state in self.accepts

    def generateLenguage(self, b):
        lista_total=[] #lista donde están todos los string posibles de longitud menor a b y mayor o igual a cero
        lista_aceptada = [] #lista donde están los string aceptados por la función test
        elementosTotales = 0 #Contador de los elementos en lista_total
        string = "" #Variable string que recibe cada posibilidad de construcción y con la que se evalúa
        for i in range(b +1): #Construcción de todos los caminos posibles del autómata
            a = list(itertools.product(self.alphabet, repeat = i))
            lista_total.append(a)
        for i in lista_total: #Evaluación de cada elemento de la lista lista_total
            for ev in i:
                elementosTotales+=1
                for op in ev:
                    string+=op #Agrega los elementos de cada posible camino al string
                evaluacion = self.test(string) #Evalúa si el string es un camino aceptado
                if(evaluacion==True):#Si el string es aceptado lo agrega a la lista lista_aceptada
                    lista_aceptada.append(string)
                string=""
        totalAceptado = len(lista_aceptada)
        print "De %r elementos evaluados, solo %r son caminos aceptados" %(elementosTotales,totalAceptado)
        return lista_aceptada

class NDFA(object):

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
        current_state = [self.start]
        for symbol in word:
            possible_states = []
            for s in current_state:
                if((s,symbol) in self.transitions):
                    assert symbol in self.alphabet
                    possible_states = possible_states + self.transitions[(s, symbol)]
            current_state = possible_states
        return (set(self.accepts) & set(current_state) != set([]))

    def convertToDFA(self):
        transitions = {} #Diccionario de las transiciones
        white_state = [] #Lista con estados que llegan a un estado de error
        start = self.start #Estado inicial
        alphabet = self.alphabet #Alfabeto del automata
        states = [[start]] #Lista de estados del DFA
        acceptNDFA = self.accepts #Estado inicial del NDFA
        accepts = [] #Lista de estados de aceptacion del DFA

        #Evalua cada estado en la lista de estados
        for element in states:
            current_state = [element]

            #Evalua la transicion de cada estado 
            for i in alphabet: #{a,b}
                posible_state = []
                for state in current_state:
                    for ele in state:
                        #Evalua si la transicion esta en las transiciones del NDFA
                        if((ele,i) in self.transitions):
                            posible_state = posible_state+self.transitions[(ele,i)]
                        else:
                            white_state.append((ele,i))
                posible_notstate = []
                if(posible_state!= []):
                    temp_lis = set(posible_state) #Sin repeticiones en los estados
                    lista = []
                    for p in temp_lis:
                        lista.append(p)
                    string = ''
                    string2 = ''
                    #Hace que cada estado pase de ser una lista a un string 
                    for k in state:
                        stringTemp = ''.join(k)
                        string = string+stringTemp
                    #Hace que para cada transicion el estado de llegada sea un string
                    for element in lista:
                        src = ''.join(element)
                        string2 = string2+src
                    transitions[(string,i)] = string2
                    #Evalua si el estado de llegada ya existe en la lista de estados
                    if(states.count(lista)==0):
                        states.append(lista)
                        posible_state=[]
                    else:
                        posible_state = []
        #Convierte los estados de state en string 
        statesCon = []
        for i in states:
            src = ''.join(i)
            statesCon = statesCon+[src]
            src = ''
        #Crea las tranciciones para los estados de error de llegada y salida
        for letra in alphabet:
            transitions[('',letra)] = ''
            for state in statesCon:
                if(not((state,letra)in transitions)):
                    transitions[(state,letra)] = ''
        #Genera una lista con los estados de aceptacion del DFA
        for state in states:
            for u in acceptNDFA:
                if(u in state):
                    src = ''.join(state)
                    accepts = accepts+[src]
        dfa = DFA(statesCon, alphabet, transitions, start, accepts)
        return dfa
