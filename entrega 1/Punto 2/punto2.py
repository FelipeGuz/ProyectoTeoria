import sys
import logging
from ndfa import DFA



def test(dfa, words):
    """Test function. Tests each word in `words` with the provided dfa."""
    for word in words:
        try:
            dfa.test(word)
        except AssertionError as e:
            logging.error('ERROR: %s\n' % e.message)


            

states = ['q0','q1','q2']
alphabet = list('01') #Punto importante de la funcion
transitions = {
    ('q0','1'): 'q0',
    ('q0','0'): 'q1',
    ('q1','1'): 'q0',
    ('q1','0'): 'q2',
    ('q2','0'): 'q2',
    ('q2','1'): 'q2',
}
start = 'q0'
accepts = ['q0']

dfa = DFA(states,alphabet,transitions,start,accepts)


                
