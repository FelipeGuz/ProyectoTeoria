import logging
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
            current_state = self.transitions[(current_state, symbol)]
            assert current_state in self.states, \
                    'Current state must be a valid state.'
            logging.debug('New state: %s' % current_state)
        logging.debug('Final state: %s' % current_state)
        logging.info('Accepted: %s\n' % (current_state in self.accepts))
        return current_state in self.accepts







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
                assert symbol in self.alphabet
                possible_states = possible_states + self.transitions[(s, symbol)]
            current_state = possible_states
  
        return (set(self.accepts) & set(current_state) != set([]))

    def convert(self):
        start = self.start
        alphabet = self.alphabet
        accepts = []
        states = [self.start]
        transitions = {}
        dfa = DFA(states,alphabet, transitions, start, accepts)
        return dfa    


class CFG(object):

    def __init__(self,variables, alphabet, rules, initial):
        assert initial in variables
        self.variables = variables
        self.alphabet = alphabet
        self.rules = rules
        self.initial = initial

    def test(self, word):
        l = len(word)
        #Inicializar la matriz
        X = []
        for i in range(l):
            X.append([['']])
            for j in range(l-1):
                X[i].append([''])

        
        # Llenar primera fila de la piramide
        for i in range(l):
            for var in self.rules.keys():
                for rule in self.rules[var]:
                    if rule == word[i]:
                        X[i][i].append(var)
            X[i][i] = list(set(X[i][i]))
            
        for i in range(l-1):
            for var1 in X[i][i]:
                for var2 in X[i+1][i+1]:
                    for var in self.rules.keys():
                        for rule in self.rules[var]:
                            if rule == var1+var2:
                                X[i][i+1].append(var)           
            X[i][i+1] = list(set(X[i][i+1]))

        print 'Primera fila:' 
        for i in range(l):
            print X[i][i]         

        print 'Segunda fila:'
        
        for i in range(l-1):
            print X[i][i+1]    

        return True

    def generateLanguage(self,n):
        return True 
