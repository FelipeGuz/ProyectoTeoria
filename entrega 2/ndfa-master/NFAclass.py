class NFA(object):
    
    def __init__(self,states,alphabet,transitions,start,accepts):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.accepts = accepts
        

    def eliminarCaracter(self,word,valor):
        l=list(word)
        inicio=0
        if(len(word)<valor): #Para una solucion regresando None se puede colocar len(word)<valor+1
            return ""
        else:
            for k in range(valor+1):
                #print ""
                #print "----->Palabra: ",word
                #print "----->Valor de k: ",k
                l.pop(valor-k)
            #print "----->Palabra sin algo: ",l
            palabra=""
            for i in l:
                palabra=palabra+i
            return palabra

    
##    def test_nfa(self,word,estado,contador):
##        if(len(word)==0):
##            return False
##        else:
##            print "---------------->WORD DE INGRESO: ",word
##            temp = word
##            contador = 0
##            lis = []
##            current_state = estado
##            for tran in self.transitions:
##                print tran
##            print "---------------------------------"
##            for symbol in temp:
##                print "Estado actual: ",current_state
##                print "Simbolo del string: ",symbol
##                for i in self.transitions[(current_state,symbol)]:
##                    if(len(self.transitions[(current_state,symbol)])>1):
##                        print "Transi: ",self.transitions[(current_state,symbol)]
##                        print "------>Su tamano es mayor a 1"
##                        for transicion in self.transitions[(current_state,symbol)]:
##                            if(current_state in self.accepts==True):
##                                return True
##                            else:
##                                return self.test_nfa(self.eliminarCaracter(word,contador),transicion,contador)
##                                contador=contador+1
##                    else:
##                        contador=contador+1
##                        print "Cambio de estado a: ",self.transitions[(current_state,symbol)]
##                        current_state = self.transitions[(current_state,symbol)]
##                    print "CONTADOR: ",contador
##                    print "-------------------------------------------------"
##                    print "-------------------------------------------------"
##            return current_state in self.accepts


    def test_nfa2(self,stringW,estadoInicial,posicion):
        temp = posicion
        estadoActual=estadoInicial
        tempStrWR = ""
        for letra in stringW:
            print "Estado actual: ",estadoActual
            print "Posicion por letra ",posicion
            print "---------->Del estado actual %r va a leer %r" %(estadoActual,posicion)
            if(len(self.transitions[(estadoActual,letra)])>1):
                posicion = posicion+1
                print "POSICION SUPER IMPORTANTE: ",posicion
                print "INGRESO A LA RECURSION"
                for estadollegada in self.transitions[(estadoActual,letra)]:
                    estadoActualR=estadollegada
                    #stringWR=self.eliminarCaracter(stringW,posicion)
                    print "------------------------>Analisis de la posicion: ",posicion
                    print "------------------------>Analisis del stringW: ",stringW
                    stringWR = stringW[posicion:]
                    print "------------------------>Analisis del stringWR: ",stringWR
                    tempString = stringWR
                    print "Estado de la recursion: ",estadoActualR
                    print "String de la recurion: ",stringWR
                    #print len(stringWR)
                    prueba = self.test_nfa2(stringWR,estadoActualR,posicion)
                    print "Posicion por recursion: ",posicion
                    if(prueba==True): return True
                    if(prueba==False):
                        print "------------------------------->ES FALSO"
                        posicion=posicion-1
                        stringWR = tempString
                        print "Este debe ser el string a leer: ",stringWR
                    
            else:
                estadoActual = self.transitions[(estadoActual,letra)]
                posicion=posicion+1
                print "Simbolo: ",letra
                print "Estado de llegada sin recursion: ",estadoActual
        return estadoActual in self.accepts


##    def test_nfa3(self,stringW,estadoInicial,posicion):
##        temp = posicion
##        estadoActual=estadoInicial
##        for letra in stringW:
##            print "Estado actual: ",estadoActual
##            print "Posicion por letra ",posicion
##            print "---------->Del estado actual %r va a leer %r" %(estadoActual,posicion)
##            if(len(self.transitions[(estadoActual,letra)])>1):
##                posicion = posicion+1
##                print "POSICION SUPER IMPORTANTE: ",posicion
##                print "INGRESO A LA RECURSION"
##                for estadollegada in self.transitions[(estadoActual,letra)]:
##                    estadoActualR=estadollegada
##                    #stringWR=self.eliminarCaracter(stringW,posicion)
##                    print "------------------------>Analisis de la posicion: ",posicion
##                    print "------------------------>Analisis del stringW: ",stringW
##                    stringWR = stringW[1:]
##                    print "------------------------>Analisis del stringWR: ",stringWR
##                    tempString = stringWR
##                    print "Estado de la recursion: ",estadoActualR
##                    print "String de la recurion: ",stringWR
##                    #print len(stringWR)
##                    prueba = self.test_nfa3(stringWR,estadoActualR,posicion)
##                    print "Posicion por recursion: ",posicion
##                    if(prueba==True): return True
##                    if(prueba==False):
##                        print "------------------------------->ES FALSO"
##                        posicion=posicion-1
##                        stringWR = tempString
##                        print "Este debe ser el string a leer: ",stringWR
##                    
##            else:
##                estadoActual = self.transitions[(estadoActual,letra)]
##                stringW = stringW[1:]
##                posicion=posicion+1
##                print "Simbolo: ",letra
##                print "Estado de llegada sin recursion: ",estadoActual
##        return estadoActual in self.accepts
    


            
        


    
