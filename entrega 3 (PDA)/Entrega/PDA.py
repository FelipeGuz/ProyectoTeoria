# -*- coding: cp1252 -*-
import itertools
class PDA(object):

    def __init__(self,states,alphabet,gamma,transitions,start,accepts):
        self.states = states
        self.alphabet = alphabet
        self.gamma = gamma
        self.transitions = transitions
        self.start = start
        self.accepts = accepts


    def generateLenguage(self, b):
        lista_total=[] #lista donde est�n todos los string posibles de longitud menor a "b" y mayor o igual a cero
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
                #print string
                evaluacion = self.test(string) #Eval�a si el string es un camino aceptado
                if(evaluacion==True):#Si el string es aceptado lo agrega a la lista lista_aceptada
                    lista_aceptada.append(string)
                string=""
        totalAceptado = len(lista_aceptada)
        print lista_aceptada
        print "De %r elementos evaluados, solo %r son caminos aceptados" %(elementosTotales,totalAceptado)


    def test(self,word):
        start_state = self.start #Valor inicial del PDA
        stack = [''] #Stack del PDA
        word = list(word) #String ingresado para evaluar
        contador = 0 #Contador que crece para cada transici�n diferente de �psilon
        def fun(state,word,stack,contador): #Funci�n que realiza la recursi�n
            possible_state = []
            #Por recursi�n termina cuando el contador sea igual a la longitud del String
            if(contador==len(word)): 
                #Busca llegar a un estado de aceptaci�n si existe una transici�n por �psilon
                while((state in self.accepts)==False and ((state,'') in self.transitions)==True):
                    #Si el valor que se cambia para el stack es '$' entonces lo quita y hace la transicion
                    if(stack[len(stack)-1]=='$'): 
                        stack.pop()
                        state = self.transitions[(state,'')][0]
                    else:
                        break
                #�nica manera en la que retorne 'True'
                if(len(stack)==1 and stack[0]=='' and state in self.accepts): #Unica manera en la que retorne 'True'
                    return True
            #Caso si la transici�n es por �psilon 
            elif(((state,word[contador])in self.transitions)==False and ((state,'')in self.transitions)==True):
                #Si el valor a quitar del stack por la transici�n es igual al �ltimo elemento del stack o es igual a �psilon
                if(self.transitions[(state,'')][1][0]==stack[len(stack)-1] or self.transitions[(state,'')][1][0]==''):
                    if(self.transitions[(state,'')][1][0]!=''):
                        stack.pop()
                    if(self.transitions[(state,'')][1][1]!=''):
                        stack.append(self.transitions[(state,'')][1][1])
                    state = self.transitions[(state,'')][0]
                else:
                    return False
                if(fun(state,word,stack,contador)==True):
                    return True
            #Caso en el que la transici�n sea por un s�mbolo diferente de �psilon
            elif((state,word[contador])in self.transitions):
                #Posibles estados de llegada por epsilon
                if((state,'')in self.transitions and (self.transitions[(state,'')][1][0]=='' or self.transitions[(state,'')][1][0]==stack[len(stack)-1])):
                    possible_state+=[self.transitions[(state,'')][0]]
                #Estados de llegada con el s�mbolo del String
                if(self.transitions[(state,word[contador])][1][0]==stack[len(stack)-1] or self.transitions[(state,word[contador])][1][0]==''):
                    possible_state+= [self.transitions[(state,word[contador])][0]]
                #Evaluaci�n de cada posible estado de llegada
                for i in possible_state:
                    if((i,word[contador])in self.transitions or (i,'')in self.transitions):
                        stackTemp = [] #Stack temporal para la evaluaci�n particular de cada estado
                        stackTemp+=stack
                        #Caso en el que la transici�n se hiciera con �psilon
                        if((state,'') in self.transitions and self.transitions[(state,'')][0]==i):
                            #Si el valor a quitar del stack por la transici�n es igual al �ltimo elemento del stack o es igual a �psilon
                            if(self.transitions[(state,'')][1][0]==stack[len(stack)-1] or self.transitions[(state,'')][1][0]==''):
                                if(self.transitions[(state,'')][1][0]!=''):
                                    stackTemp.pop()
                                if(self.transitions[(state,'')][1][1]!=''):
                                    stackTemp.append(self.transitions[(state,'')][1][1])
                            if(fun(i,word,stackTemp,contador)==True):
                                return True
                        #Caso en el que la transici�n se hiciera con un s�mbolo diferente de �psilon         
                        elif((state,word[contador]) in self.transitions and self.transitions[(state,word[contador])][0]==i):
                            #Si el valor a quitar del stack por la transici�n es igual al �ltimo elemento del stack o es igual a �psilon
                            if(self.transitions[(state,word[contador])][1][0]==stack[len(stack)-1] or self.transitions[(state,word[contador])][1][0]==''):
                                if(self.transitions[(state,word[contador])][1][0]!=''):
                                    stackTemp.pop()
                                if(self.transitions[(state,word[contador])][1][1]!=''):
                                    stackTemp.append(self.transitions[(state,word[contador])][1][1])
                            if(fun(i,word,stackTemp,contador+1)==True):
                                return True
        #Si la funci�n 'fun' retorna algo diferente a True entonces retorna False, en caso contrario retorna True
        if(fun(start_state,word,stack,contador)!=True):
            return False
        else:
            return True
