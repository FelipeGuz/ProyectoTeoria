# -*- coding: cp1252 -*-
from copy import deepcopy
import itertools
class PDA(object):

    def __init__(self,states,alphabet,gamma,transitions,start,accepts):
        self.states = states
        self.alphabet = alphabet
        self.gamma = gamma
        self.transitions = transitions
        self.start = start
        self.accepts = accepts

##    def CStack(self,elemento,stack):
##        if(elemento[1][0] != ''):
##            print "--------->Son iguales (%r y %r)" %(elemento[1][0],stack[len(stack)-1])
##            if(elemento[1][0] == stack[len(stack)-1]):
##                print "--------->Ultimo elemento: ",stack[len(stack)-1]
##                stack.pop()
##                if(elemento[1][1]!=''):
##                    stack.append(elemento[1][1])
##            else:
##                return False
##            print "ENTRO AL STACK"
##        else:
##            print "--------->Ultimo elemento: ",stack[len(stack)-1]
##            stack.append('')
##            stack.pop()
##            stack.append(elemento[1][1])

    def generateLenguage(self, b):
        lista_total=[] #lista donde están todos los string posibles de longitud menor a "b" y mayor o igual a cero
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
                #print string
                evaluacion = self.test(string) #Evalúa si el string es un camino aceptado
                if(evaluacion==True):#Si el string es aceptado lo agrega a la lista lista_aceptada
                    lista_aceptada.append(string)
                string=""
        totalAceptado = len(lista_aceptada)
        print lista_aceptada
        print "De %r elementos evaluados, solo %r son caminos aceptados" %(elementosTotales,totalAceptado)


####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
#TEST ITERATIVO: ------------------>NO SIRVE
        
    def testI(self, word):
        print "Palabra a leer: ",word
        current_state = [self.start]
        #stack = ['']
        stack = ['']
        for symbol in word:
            possible_states = []
            #stackPru = []
            for s in current_state:
                #stack = ['']
                print "-------------------------------------------"
                print "-------------------------------------------"
                print "CURRENT_STATE: ",current_state
                print "1)TRANSICION: (%r,%r)" %(s,symbol)
                print "1)STACK: ",stack
                while(((s,symbol) in self.transitions)==False and ((s,'')in self.transitions)):
                    print "----->Atajo por vacio"
                    if(self.transitions[(s,'')][1][0])==stack[len(stack)-1]:
                        print "----->Norma de cambio: (%r)" %self.transitions[(s,'')][1][0]
                        print "----->Ultimo valor del stack: ",stack[len(stack)-1]
                        stack.pop()
                        if(self.transitions[(s,'')][1][1]!=''):
                            stack.append(self.transitions[(s,'')][1][1])
                        s = self.transitions[(s,'')][0]
                        print "----->Nuevo s: ",s
                        print "----->Stack: ",stack
                    else:
                        print "------------------------"
                        print "No existe la transicion"
                        return False
##                if(len(possible_states)>1):
##                    stack = stackPru
                if((s,symbol) in self.transitions):
                    print "2)TRANSICION: (%r,%r)" %(s,symbol)
                    print "possible_states: ",possible_states
                    assert symbol in self.alphabet
                    print "Norma de cambio: (%r)" %self.transitions[(s,symbol)][1][0]
                    print "Ultimo valor del stack: ",stack[len(stack)-1]
                    print "Se cumple la igualdad? ",self.transitions[(s,symbol)][1][0]==stack[len(stack)-1]
                    if((self.transitions[(s,symbol)][1][0]==stack[len(stack)-1]) or self.transitions[(s,symbol)][1][0]==''):
                        possible_states += [self.transitions[(s, symbol)][0]]
                        if((s,'') in self.transitions):
                            possible_states+=[self.transitions[(s,'')][0]]
                        print "possible_states: ",possible_states
                        if(self.transitions[(s,symbol)][1][0]!=''):
                            stack.pop()
                        if(self.transitions[(s,symbol)][1][1]!=''):
                            stack.append(self.transitions[(s,symbol)][1][1])
                        print "2)STACK: ",stack
                    else:
                        print "------------------------"
                        print "No existe la transicion"
                        return False
##                stackPru = stack
##                print "--------------------------->stackPru: ",stackPru
            current_state = possible_states

        print "------------------------------"
        print "------------------------------"
        print "FINAL"
        print "------------------------------"
        print "EVALUACION DE EL ELEMENTO EPSILON FINAL: "
        print "CURRENT_STATE: ",current_state
        while(current_state != self.accepts and ((current_state)[0],'') in self.transitions):
            print "----->Entro a evaluar"
            print "----->STACK: ",stack
            print "Norma de cambio: (%r)" %self.transitions[(s,symbol)][1][0]
            print "Ultimo valor del stack: ",stack[len(stack)-1]
            print "Se cumple la igualdad? ",self.transitions[(s,symbol)][1][0]==stack[len(stack)-1]
            if(self.transitions[((current_state)[0],'')][1][0]==stack[len(stack)-1] or self.transitions[((current_state)[0],'')][1][0]==''):
                current_state = [self.transitions[((current_state)[0],'')][0]]
                if(self.transitions[(s,symbol)][1][0]!=''):
                    stack.pop()
                if(self.transitions[(s,symbol)][1][1]!=''):
                    stack.append(self.transitions[(s,symbol)][1][1])
            else:
                print "------------------------"
                print "No existe la transicion"
                return False
            print "---->STACK: ",stack
        if(len(stack)==0 and set(self.accepts) & set(current_state) != set([])):
            return True
        else:
            return False

####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
#TEST RECURSIVO: ------------------>SI SIRVE

    def testR(self,word):
        start_state = self.start
        stack = ['']
        word = list(word)
        contador = 0
        lista = []
        def fun(state,word,stack,contador):
            print "State: ",state
            print "Word: ",word
            print "Contador: ",contador
            print "STACK: ",stack
            possible_state = []
            #if(self.transitions[(state,'')][1][0]=='$' or contador==len(word)):
            if(contador==len(word)):
                print "------>Ingreso a la condicion"
                print "----> Stack: ",stack
                while((state in self.accepts)==False and ((state,'') in self.transitions)==True):
                    if(stack[len(stack)-1]=='$'):
                        stack.pop()
                        print "State: ",state
                        state = self.transitions[(state,'')][0]
                        print "Nuevo state: ",state
                    else:
                        break
                if(len(stack)==1 and stack[0]=='' and state in self.accepts):
                #if(state in self.accepts):
                    return True
                else:
                    print "No cumple con la condicion"
            elif(((state,word[contador])in self.transitions)==False and ((state,'')in self.transitions)==True):
                print "------>Ingreso a camino epsilon:"
                print "Camino de intento: (%r,%r)" %(state,word[contador])
                print "Stack inicial: ",stack
                if(self.transitions[(state,'')][1][0]==stack[len(stack)-1] or self.transitions[(state,'')][1][0]==''):
                    if(self.transitions[(state,'')][1][0]!=''):
                        stack.pop()
                    if(self.transitions[(state,'')][1][1]!=''):
                        if((self.transitions[(state,'')][1][1])>1):
                            for i in self.transitions[(state,'')][1][1]:
                                stack.append(self.transitions[(state,'')][1][1])
                        else:
                            stack.append(self.transitions[(state,'')][1][1])
                    state = self.transitions[(state,'')][0]
                else:
                    return False
                print "Nueva transicion: (%r,%r)" %(state,word[contador])
                print "Nuevo stack: ",stack
                print "-------------------------------"
                print "-------------------------------"
                if(fun(state,word,stack,contador)==True):
                    return True
##                return fun(state,word,stack,contador)
            elif((state,word[contador])in self.transitions):
                print "------>Ingreso a segunda opcion:"
                print "State: ",state
                print "STACK: ",stack
                if((state,'')in self.transitions and (self.transitions[(state,'')][1][0]=='' or self.transitions[(state,'')][1][0]==stack[len(stack)-1])):
                    print "---->Existe camino por epsilon para state=%r que llega a: %r " %(state,self.transitions[(state,'')][0])
                    possible_state+=[self.transitions[(state,'')][0]]
                if(self.transitions[(state,word[contador])][1][0]==stack[len(stack)-1] or self.transitions[(state,word[contador])][1][0]==''):
                    print "---->Por la transicion (%r,%r) llego a %r" %(state,word[contador],self.transitions[(state,word[contador])][0])
                    possible_state+= [self.transitions[(state,word[contador])][0]]
                print "Possible_state: ",possible_state
                for i in possible_state:
                    if((i,word[contador])in self.transitions or (i,'')in self.transitions):
                        #if((state,word[contador])in self.transitions):
                        #stackTemp = deepcopy(stack) #Evitar que al analisar los casos de possible_state cambie el stack
                        #stackTemp = stack
                        stackTemp = []
                        stackTemp+=stack
                        lista.append([stackTemp,contador])
                        print "stackTemp: ",stackTemp
                        if((state,'') in self.transitions and self.transitions[(state,'')][0]==i):
                            print "--->Opcion vacio"
                            print "i=",i
                            print "Contador: ",contador
                            print "STACK: ",stack
                            print "--->LISTA IMPORTANTE: ",lista
                            print "---->stackTemp: ",stackTemp
                            if(self.transitions[(state,'')][1][0]==stack[len(stack)-1] or self.transitions[(state,'')][1][0]==''):
                                if(self.transitions[(state,'')][1][0]!=''):
                                    stackTemp.pop()
                                if(self.transitions[(state,'')][1][1]!=''):
                                    stackTemp.append(self.transitions[(state,'')][1][1])
                            print "---->stackTempResul: ",stackTemp
                            print "-------------------------------"
                            print "-------------------------------"
                            #lista.append(stack)
                            if(fun(i,word,stackTemp,contador)==True):
                                return True
                            else:
                                print "No funciono por opcion vacio"
                                print "stackTemp: ",stackTemp
                                print "stack: ",stack
                                #stack = stackTemp
                            #stackTemp = deepcopy(stack)
                                
                        elif((state,word[contador]) in self.transitions and self.transitions[(state,word[contador])][0]==i):
                            print "--->Opcion no vacio"
                            print "i=",i
                            print "Contador: ",contador
                            print "STACK: ",stack
                            print "--->LISTA IMPORTANTE: ",lista
                            print "---->stackTemp: ",stackTemp
                            if(self.transitions[(state,word[contador])][1][0]==stack[len(stack)-1] or self.transitions[(state,word[contador])][1][0]==''):
                                if(self.transitions[(state,word[contador])][1][0]!=''):
                                    stackTemp.pop()
                                if(self.transitions[(state,word[contador])][1][1]!=''):
                                    stackTemp.append(self.transitions[(state,word[contador])][1][1])
                            print "---->stackTempResul: ",stackTemp        
                            print "-------------------------------"
                            print "-------------------------------"
                            if(fun(i,word,stackTemp,contador+1)==True):
                                return True
                            else:
                                print "No funciono por opcion no vacio"
                                print "stackTemp: ",stackTemp
                                print "stack: ",stack
                                #stackTemp = stack
                                #stack = stackTemp
                            #stackTemp = deepcopy(stack)
                        print "TERMINO UNO DE LOS PROCESOS"
        if(fun(start_state,word,stack,contador)!=True):
            return False
        else:
            return True

####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
#TEST RECURSIVO SIN COMENTARIOS:------------------>SI SIRVE

    def test(self,word):
        start_state = self.start
        stack = ['']
        word = list(word)
        contador = 0
        lista = []
        def fun(state,word,stack,contador):
            possible_state = []
            #if(self.transitions[(state,'')][1][0]=='$' or contador==len(word)):
            if(contador==len(word)):
                while((state in self.accepts)==False and ((state,'') in self.transitions)==True):
                    if(stack[len(stack)-1]=='$'):
                        stack.pop()
                        state = self.transitions[(state,'')][0]
                    else:
                        break
                if(len(stack)==1 and stack[0]=='' and state in self.accepts):
                #if(state in self.accepts):
                    return True
            elif(((state,word[contador])in self.transitions)==False and ((state,'')in self.transitions)==True):
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
##                return fun(state,word,stack,contador)
            elif((state,word[contador])in self.transitions):
                if((state,'')in self.transitions and (self.transitions[(state,'')][1][0]=='' or self.transitions[(state,'')][1][0]==stack[len(stack)-1])):
                    possible_state+=[self.transitions[(state,'')][0]]
                if(self.transitions[(state,word[contador])][1][0]==stack[len(stack)-1] or self.transitions[(state,word[contador])][1][0]==''):
                    possible_state+= [self.transitions[(state,word[contador])][0]]
                for i in possible_state:
                    if((i,word[contador])in self.transitions or (i,'')in self.transitions):
                        #if((state,word[contador])in self.transitions):
                        #stackTemp = deepcopy(stack) #Evitar que al analisar los casos de possible_state cambie el stack
                        #stackTemp = stack
                        stackTemp = []
                        stackTemp+=stack
                        lista.append([stackTemp,contador])
                        if((state,'') in self.transitions and self.transitions[(state,'')][0]==i):
                            if(self.transitions[(state,'')][1][0]==stack[len(stack)-1] or self.transitions[(state,'')][1][0]==''):
                                if(self.transitions[(state,'')][1][0]!=''):
                                    stackTemp.pop()
                                if(self.transitions[(state,'')][1][1]!=''):
                                    stackTemp.append(self.transitions[(state,'')][1][1])
                            #lista.append(stack)
                            if(fun(i,word,stackTemp,contador)==True):
                                return True
                                
                        elif((state,word[contador]) in self.transitions and self.transitions[(state,word[contador])][0]==i):
                            if(self.transitions[(state,word[contador])][1][0]==stack[len(stack)-1] or self.transitions[(state,word[contador])][1][0]==''):
                                if(self.transitions[(state,word[contador])][1][0]!=''):
                                    stackTemp.pop()
                                if(self.transitions[(state,word[contador])][1][1]!=''):
                                    stackTemp.append(self.transitions[(state,word[contador])][1][1])
                            if(fun(i,word,stackTemp,contador+1)==True):
                                return True
        if(fun(start_state,word,stack,contador)!=True):
            return False
        else:
            return True

####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
#PRUEBA DE TEST NO DETERMINISTA:------------------>NO SIRVE

    def test2(self,word):
        start_state = self.start
        stack = ['']
        word = list(word)
        contador = 0
        def fun(state,word,stack,contador):
            print "State: ",state
            print "Word: ",word
            print "Contador: ",contador
            print "STACK: ",stack
            possible_state = []
            #if(self.transitions[(state,'')][1][0]=='$' or contador==len(word)):
            if(contador==len(word)):
                print "---->Ingreso a la condicion"
                print "----> Stack: ",stack
                while((state in self.accepts)==False and ((state,'') in self.transitions)==True):
                    if(stack[len(stack)-1]=='$'):
                        stack.pop()
                        print "State: ",state
                        state = self.transitions[(state,'')][0]
                        print "Nuevo state: ",state
                    else:
                        break
                if(len(stack)==1 and stack[0]=='' and state in self.accepts):
                #if(state in self.accepts):
                    return True
                else:
                    print "No cumple con la dondicion"
            elif(((state,word[contador])in self.transitions)==False and ((state,'')in self.transitions)==True):
                print "---->Ingreso a camino epsilon:"
                print "Camino de intento: (%r,%r)" %(state,word[contador])
                print "Stack inicial: ",stack
                if(self.transitions[(state,'')][1][0]==stack[len(stack)-1] or self.transitions[(state,'')][1][0]==''):
                    if(self.transitions[(state,'')][1][0]!=''):
                        stack.pop()
                    if(self.transitions[(state,'')][1][1]!=''):
                        stack.append(self.transitions[(state,'')][1][1])
                    state = self.transitions[(state,'')][0]
                print "Nueva transicion: (%r,%r)" %(state,word[contador])
                print "Nuevo stack: ",stack
                print "-------------------------------"
                print "-------------------------------"
                if(fun(state,word,stack,contador)==True):
                    return True
            else:
                print "Ingreso a segunda opcion:"
                print "STACK: ",stack
                if((state,'')in self.transitions and (self.transitions[(state,'')][1][0]=='' or self.transitions[(state,'')][1][0]==stack[len(stack)-1])):
                    print "---->Existe camino por epsilon para state=",state
                    print "---->Con vacio llego a: ",self.transitions[(state,'')][0]
                    possible_state+=[self.transitions[(state,'')][0]]
                if(self.transitions[(state,word[contador])][1][0]==stack[len(stack)-1] or self.transitions[(state,word[contador])][1][0]==''):
                    print "Por la transicion (%r,%r) llego a %r" %(state,word[contador],self.transitions[(state,word[contador])][0])
                    possible_state+= [self.transitions[(state,word[contador])][0]]
                print "Possible_state: ",possible_state
                for i in possible_state:
                    if((i,word[contador])in self.transitions):
                    #if((state,word[contador])in self.transitions):
                        stackTemp = stack #Evitar que al analisar los casos de possible_state cambie el stack
                        if((state,'') in self.transitions and self.transitions[(state,'')][0]==i):
                            print "--->Opcion vacio"
                            print "i=",i
                            print "---->stackTemp: ",stackTemp
                            if(self.transitions[(state,'')][1][0]==stackTemp[len(stackTemp)-1] or self.transitions[(state,'')][1][0]==''):
                                if(self.transitions[(state,'')][1][0]!=''):
                                    stackTemp.pop()
                                if(self.transitions[(state,'')][1][1]!=''):
                                    stackTemp.append(self.transitions[(state,'')][1][1])
                            print "---->stackTempResul: ",stackTemp
                            print "-------------------------------"
                            print "-------------------------------"
                            if(fun(i,word,stackTemp,contador)==True):
                                return True
                        else:
                            print "Opcion no vacio"
                            print "i=",i
                            print "---->stackTemp: ",stackTemp
                            if(self.transitions[(state,word[contador])][1][0]==stackTemp[len(stackTemp)-1] or self.transitions[(state,word[contador])][1][0]==''):
                                if(self.transitions[(state,word[contador])][1][0]!=''):
                                    stackTemp.pop()
                                if(self.transitions[(state,word[contador])][1][1]!=''):
                                    stackTemp.append(self.transitions[(state,word[contador])][1][1])
                                #i = self.transitions[(state,word[contador])][0]
                            print "---->stackTempResul: ",stackTemp
                            print "-------------------------------"
                            print "-------------------------------"
                            if(fun(i,word,stackTemp,contador+1)==True):
                                return True
        if(fun(start_state,word,stack,contador)!=True):
            return False
        else:
            return True


##    def funLis(self,word):
##        current_state = [self.start]
##        stack = ['']
##        word = list(word)
##        contador = 0
##        def fun(current_state,stack,word,contador):
##            for i in word:
##                possible_state = []
##                for state in current_state:
##                    print state
##                    print i
##                    if(contador==len(word)): #if recursion
##                        if(state in self.accepts):
##                            return True
##                        else:
##                            return False
##                        
##                    elif(((state,i) in self.transitions)==False and (state,'') in self.transitions):
##                        print "Existe el vacio"
##                        possible_state+=[self.transitions[(state,'')][0]]
##                        current_state = possible_state
##                        print "CurrentState: ",current_state
##                        return fun(current_state,stack,word,contador)
##                        
##                    else:
##                        print "Busqueda: ",self.transitions[(state,i)][0][0]
##                        if(len(self.transitions[(state,i)][0][0])>1):
##                            for p in range(len(self.transitions[(state,word[contador])])):
##                                possible_state+=[self.transitions[(state,i)][p][0]]
##                        else:
##                            possible_state+=self.transitions[(state,i)]
##                        current_state = possible_state
##                        word.pop(0)
##                        return fun(current_state,stack,word,contador)
##        return fun(current_state,stack,word,contador)
                        

####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
#TEST VARIAS FUNCIONES: ------------------>NO SIRVE 
        

    def testRVF(self,word):
        start_state = self.start
        stack = ['']
        word = list(word)
        contador = 0
        lista = []
        def fun(state,word,stack,contador):
            print "State: ",state
            print "Word: ",word
            print "Contador: ",contador
            print "STACK: ",stack
            possible_state = []
            #if(self.transitions[(state,'')][1][0]=='$' or contador==len(word)):
            if(contador==len(word)):
                print "------>Ingreso a la condicion"
                print "----> Stack: ",stack
                while((state in self.accepts)==False and ((state,'') in self.transitions)==True):
                    if(stack[len(stack)-1]=='$'):
                        stack.pop()
                        print "State: ",state
                        state = self.transitions[(state,'')][0]
                        print "Nuevo state: ",state
                    else:
                        break
                if(len(stack)==1 and stack[0]=='' and state in self.accepts):
                #if(state in self.accepts):
                    return True
                else:
                    print "No cumple con la condicion"
            elif(((state,word[contador])in self.transitions)==False and ((state,'')in self.transitions)==True):
                print "------>Ingreso a camino epsilon:"
                print "Camino de intento: (%r,%r)" %(state,word[contador])
                print "Stack inicial: ",stack
                if(self.transitions[(state,'')][1][0]==stack[len(stack)-1] or self.transitions[(state,'')][1][0]==''):
                    if(self.transitions[(state,'')][1][0]!=''):
                        stack.pop()
                    if(self.transitions[(state,'')][1][1]!=''):
                        stack.append(self.transitions[(state,'')][1][1])
                    state = self.transitions[(state,'')][0]
                else:
                    return False
                print "Nueva transicion: (%r,%r)" %(state,word[contador])
                print "Nuevo stack: ",stack
                print "-------------------------------"
                print "-------------------------------"
                if(fun(state,word,stack,contador)==True):
                    return True
##                return fun(state,word,stack,contador)
            elif((state,word[contador])in self.transitions):
                print "------>Ingreso a segunda opcion:"
                print "State: ",state
                print "STACK: ",stack
                if((state,'')in self.transitions and (self.transitions[(state,'')][1][0]=='' or self.transitions[(state,'')][1][0]==stack[len(stack)-1])):
                    print "---->Existe camino por epsilon para state=%r que llega a: %r " %(state,self.transitions[(state,'')][0])
                    possible_state+=[self.transitions[(state,'')][0]]
                if(self.transitions[(state,word[contador])][1][0]==stack[len(stack)-1] or self.transitions[(state,word[contador])][1][0]==''):
                    print "---->Por la transicion (%r,%r) llego a %r" %(state,word[contador],self.transitions[(state,word[contador])][0])
                    possible_state+= [self.transitions[(state,word[contador])][0]]
                print "Possible_state: ",possible_state
###################################################################################################################################################
                def stackHelp1(state,word,stackTemp,contador):
                        print "--->Opcion vacio"
                        print "i=",i
                        print "Contador: ",contador
                        print "STACK: ",stack
                        print "---->stackTemp: ",stackTemp
                        if(self.transitions[(state,'')][1][0]==stack[len(stack)-1] or self.transitions[(state,'')][1][0]==''):
                            if(self.transitions[(state,'')][1][0]!=''):
                                stackTemp.pop()
                            if(self.transitions[(state,'')][1][1]!=''):
                                stackTemp.append(self.transitions[(state,'')][1][1])
                        print "---->stackTempResul: ",stackTemp
                        print "-------------------------------"
                        print "-------------------------------"
                        #lista.append(stack)
                        if(fun(i,word,stackTemp,contador)==True):
                            return True
                        else:
                            print "No funciono por opcion vacio"
                            print "stackTemp: ",stackTemp
                            print "stack: ",stack
                
                def stackHelp2(state,word,stackTemp,contador): 
                    print "--->Opcion no vacio"
                    print "i=",i
                    print "Contador: ",contador
                    print "STACK: ",stack
                    print "LISTA IMPORTANTE: ",lista
                    print "---->stackTemp: ",stackTemp
                    if(self.transitions[(state,word[contador])][1][0]==stack[len(stack)-1] or self.transitions[(state,word[contador])][1][0]==''):
                        if(self.transitions[(state,word[contador])][1][0]!=''):
                            stackTemp.pop()
                        if(self.transitions[(state,word[contador])][1][1]!=''):
                            stackTemp.append(self.transitions[(state,word[contador])][1][1])
                    print "---->stackTempResul: ",stackTemp        
                    print "-------------------------------"
                    print "-------------------------------"
                    if(fun(i,word,stackTemp,contador+1)==True):
                        return True
                    else:
                        print "No funciono por opcion no vacio"
                        print "stackTemp: ",stackTemp
                        print "stack: ",stack
                        stackTemp = stack
###################################################################################################################################################                
                for i in possible_state:
                    if((i,word[contador])in self.transitions):
                        print "stackTemp: ",stack
                        if((state,'') in self.transitions and self.transitions[(state,'')][0]==i):
                            stackHelp1(state,word,stack,contador)
                        if((state,word[contador]) in self.transitions and self.transitions[(state,word[contador])][0]==i):
                            stackHelp2(state,word,stack,contador)
                        print "TERMINO UNO DE LOS PROCESOS"

##                    if(fun(i,word,stackTemp,contador+1)==True):
##                        return True
##                    else:
##                        print "No funciono"
##                        print "stackTemp: ",stackTemp
##                        print "stack: ",stack
##                        stackTemp = stack
        if(fun(start_state,word,stack,contador)!=True):
            return False
        else:
            return True






        

                        
                    
                        








                
        
