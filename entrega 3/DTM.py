class DTM(object):

    def __init__(self,states,alphabet,gamma,transitions,start,accepts,reject):
        self.states = states
        self.alphabet = alphabet
        self.gamma = gamma
        self.transitions = transitions
        self.start = start
        self.accepts = accepts
        self.reject = reject

    def printDTM(self):
        print self.states
        print "---------------------"
        print self.alphabet
        print "---------------------"
        print self.gamma
        print "---------------------"
        print self.transitions
        print "---------------------"
        print self.start
        print "---------------------"
        print self.accepts
        print "---------------------"
        print self.reject

    def testN(self,word):
        W = list(word)
        position = 0
        state = self.start
        symbol = ''
        direction = ''
        for delta in self.transitions:
            posibleTransition = []
            print "----------------------"
            print delta
            print "delta[1]: ",delta[1]
            print "W[0]: ",W[0]
            if delta[1]==W[0]:
                if delta[0]==state:
                    print "delta[0]: ",delta[0]
                    print "State: ",state
                    temp = delta[1]
                    symbol = delta[1]
                    print W[W.index(temp)]
                    print symbol
                    W[W.index(temp)] = symbol
                    print W
                    direction = (self.transitions[state,symbol])[2]
        print W

    def test(self,word):
        W = list(word)
        position = 0
        state = 'q1'
        #state = self.start
        symbol = ''
        direction = ''
        posibleTransition = []
        lista = []
        for delta in self.transitions:
            if delta[0]==state:
                posibleTransition = posibleTransition+list([delta])
##                temp = delta[1]
##                symbol = delta[1]
##                W[W.index(temp)] = symbol
##                direction = (self.transitions[state,symbol])[2]
            print posibleTransition
        for le in range(len(posibleTransition)):
            lista.append(word.index((posibleTransition[le])[1]))
        for ri in lista:
            
        print W
        


    
