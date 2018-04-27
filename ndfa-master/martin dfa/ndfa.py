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
            if (current_state, symbol) in self.transitions.keys():
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False
            assert current_state in self.states, \
                    'Current state must be a valid state.'
            logging.debug('New state: %s' % current_state)
        logging.debug('Final state: %s' % current_state)
        logging.info('Accepted: %s\n' % (current_state in self.accepts))
        return current_state in self.accepts

    
    
    def generateAll(self,n):
        r=[""]
        for i in range(n):
            l = len(r)
            for j in range(l):
                for a in self.alphabet:
                    if len(r[j])==i:
                        new = r[j] +a
                        r.append(new)
            #print 'Para i='+str(i)+' van:'
            #print len(r)
        return r

    
    
    def generateLanguage(self, n):
    
        todas = self.generateAll(n)
        ret = []
        for c in todas:
            if self.test(c):
                ret.append(c)
        return ret

    

    def find(self, n, k, c, l):
        ret = []
        if n in self.accepts:
            l.append(c)
        if k==0:
            return l

        for a in self.alphabet:
            if (n,a) in self.transitions.keys():
                s= self.transitions[(n,a)]
                l1 = l[:]
                ret = ret + self.find(s, k-1, c+a, l1)

        return ret

            
        












    
