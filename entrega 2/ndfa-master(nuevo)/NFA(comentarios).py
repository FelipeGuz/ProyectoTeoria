def convertN(self):
        transitions = {}
        white_state = []
        start = self.start
        alphabet = self.alphabet
        states = [[start]]
        acceptNDFA = self.accepts
        accepts = []
        for element in states:
            print '-----------------------'
            print '-----------------------'
            print "ESTADOS: ",states
            print "Element: ",element
            current_state = [element]
            print "Current_state: ",current_state
            print '------------------------'
            state_llegada = [] ####Estados de llegada
            for i in alphabet: #{a,b}
                print "Alphabet element: ",i
                posible_state = []
                for state in current_state:
                    for ele in state:
                        print "State: ",ele
                        if((ele,i) in self.transitions):
                            print "SI ESTA EN LAS TRANSICIONES"
                            print "(%r,%r):%r" %(ele,i,self.transitions[(ele,i)])
                            posible_state = posible_state+self.transitions[(ele,i)]
                            print "Posible_state: ",posible_state
                        else:
                            print "No esta en la transicion"
                            white_state.append((ele,i))
                            print white_state
                if(posible_state!= []):
                    temp_lis = set(posible_state)
                    print "Set temp_lis: ",temp_lis
                    lista = []
                    for p in temp_lis:
                        lista.append(p)
                    print "Posible_state final: ",lista
                    state_llegada = lista #####Lista de llegada
                    print '---------------------------'
                    #######################################
                    string = ''
                    string2 = ''
                    for k in state:
                        stringTemp = ''.join(k)
                        string = string+stringTemp
                    for element in lista:
                        src = ''.join(element)
                        string2 = string2+src
                    #print string
                    print "---->Transicion: (%r,%r):%r" %(string,i,lista)
                    transitions[(string,i)] = string2
                    #######################################
                    if(states.count(lista)==0):
                        states.append(lista)
                        posible_state=[]
                    else:
                        print "El elemento %r ya esta" %(lista)
                        posible_state = []
        statesCon = []
        for i in states:
            src = ''.join(i)
            statesCon = statesCon+[src]
            src = ''
        for letra in alphabet:
            for state in statesCon:
                if(not((state,letra)in transitions)):
                    transitions[(state,letra)] = ['']
        print acceptNDFA
        for state in states:
            print "Estado: ",state
            for u in acceptNDFA:
                print u
                if(u in state):
                    accepts = accepts+[state]
        return "RESPUESTA: ",transitions
