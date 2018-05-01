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
                    lista = self.rules[(key)]
                    if(i in lista):
                        temp_rule.append(key)
            dicc[contador+1,contador+1] = list(sorted(set(temp_rule)))
            states.append([[contador+1,contador+1],dicc[contador+1,contador+1]])
            contador+=1

        fila = 2
        
        columna = 1
        elemento = 2
        pre_states = []
        def filasM2(fila,columna,elemento,states,pre_states,word,rules,contador):
            if (fila==len(word)+1):
                longitud = len(states)-1
                if(self.start in states[longitud][1]):
                    return True
                else:
                    return False
            elif(elemento==contador):
                states+=pre_states
                pre_states = []
                return filasM2(fila+1,1,fila+1,states,pre_states,word,self.rules,contador)
            else:
                eva_temp = [] #evaluaciones entre elementos del triangulo (Ej: q11 con q22)
                combinacion = [] #combinaciones distributiva de los elementos de eva_temp
                #Buscar elementos para eva_temp
                for i in states:
                    if(i[0][0]==columna or i[0][1]==elemento):
                        eva_temp+=[i[1]]
                #Hacer las combinaciones
                first = 0
                second = len(eva_temp)-1
                cont = 0
                while(cont<(len(eva_temp)/2)):
                    for i in eva_temp[first]:
                        for u in eva_temp[second]:
                            for node in rules:
                                if((i+u) in rules.get(node) and not(node in combinacion)):
                                    combinacion.append(node)
                    if(len(eva_temp)<=2):
                        break
                    elif(first<second):
##                        first+=1
##                        second-=1
                        temp = first
                        first=second-1
                        second=temp+1
                        cont+=1
                    else:
                        temp=first
                        first=second+1
                        second=temp-1
                        cont+=1
                pre_states.append([[columna,elemento],combinacion])
                return filasM2(fila,columna+1,elemento+1,states,pre_states,word,self.rules,contador)
        return filasM2(fila,columna,elemento,states,pre_states,word,self.rules,contador+1)
                        
            
            
            
                
        
            
            
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

####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

    def test2(self,word):
        contador = 0
        states = []
        dicc = {}
        for i in word:
            temp_rule = []
            for key in self.rules.keys():
                for eleState in self.rules[(key)]:
                    lista = self.rules[(key)]
                    if(i in lista):
                        temp_rule.append(key)
            print "Temp_rule: ",temp_rule
            dicc[contador+1,contador+1] = list(sorted(set(temp_rule)))
            states.append([[contador+1,contador+1],dicc[contador+1,contador+1]])
            print "Diccionario: ",dicc
            contador+=1

        fila = 2
        
        columna = 1
        elemento = 2
        pre_states = []
        print "---->ESTADOS: ",states
        print "---->CONTADOR: ",contador
        print "---------------------------------------------------------------------------------------------"
        def filasM2(fila,columna,elemento,states,pre_states,word,rules,contador):
            print "---------------------------------------------------------------------------------------"
            print "---------------------------------------------------------------------------------------"
            print "-------------------------------------------CAMBIOS-------------------------------------"
            print "---------------------------------------------------------------------------------------"
            print "---------------------------------------------------------------------------------------"
            print "Columna: ",columna
            print "Elemento: ",elemento
            if (fila==len(word)+1):
                longitud = len(states)-1
                if(self.start in states[longitud][1]):
                    return True
                else:
                    return False
            elif(elemento==contador):
                print "---------------------------------------------------------------------------------------"
                print "---------------------------------------------------------------------------------------"
                print "Pre_states: ",pre_states
                states+=pre_states
                pre_states = []
                return filasM2(fila+1,1,fila+1,states,pre_states,word,self.rules,contador)
            else:
                print "Ingresando a ELSE:"
                eva_temp = [] #evaluaciones entre elementos del triangulo (Ej: q11 con q22)
                combinacion = [] #combinaciones distributiva de los elementos de eva_temp
                #Buscar elementos para eva_temp
                for i in states:
                    print "Elemento de los estados: ",i
                    if(i[0][0]==columna or i[0][1]==elemento):
                        print "Elemento que cumple: ",i[1]
                        eva_temp+=[i[1]]
                print "Eva_temp es: ",eva_temp
                #Hacer las combinaciones
                first = 0
                second = len(eva_temp)-1
                cont = 0
                while(cont<(len(eva_temp)/2)):
                    print "First: ",first
                    print "Second: ",second
                    for i in eva_temp[first]:
                        print "-->",eva_temp[first]
                        print "i: ",i
                        for u in eva_temp[second]:
                            print "-->",eva_temp[second]
                            print "u: ",u
                            for node in rules:
                                print "Intento enlace: ",(i+u)
                                if((i+u) in rules.get(node) and not(node in combinacion)):
                                    print "-------------------->Enlace: %r con %r" %(i+u,node)
                                    combinacion.append(node)
                    if(len(eva_temp)<=2):
                        break
                    elif(first<second):
##                        first+=1
##                        second-=1
                        temp = first
                        first=second-1
                        second=temp+1
                        cont+=1
                    else:
                        temp=first
                        first=second+1
                        second=temp-1
                        cont+=1

                print "Combinacion: ",combinacion
                pre_states.append([[columna,elemento],combinacion])
                return filasM2(fila,columna+1,elemento+1,states,pre_states,word,self.rules,contador)
        return filasM2(fila,columna,elemento,states,pre_states,word,self.rules,contador+1)
