class NFA(object):

    def __init__(self,states,alphabet,transitions,start,accepts):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start = start
        self.accepts = accepts
        

    def test_nfa(self,word):
        lis = []
        current_state = self.start
        for tran in self.transitions:
            print tran
        for symbol in word:
            print "Cada simbolo del string: ",symbol
            for i in self.transitions[(current_state,symbol)]:
                current_state = self.transitions[(current_state,symbol)]
        return current_state in self.accepts


    
