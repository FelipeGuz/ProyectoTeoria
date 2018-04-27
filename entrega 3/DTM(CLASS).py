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
        


    
