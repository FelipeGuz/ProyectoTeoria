# coding=utf-8
#!/usr/bin/env python

import sys
import logging
from ndfa import DFA

dfas = []

def test(dfa, words):
    """Test function. Tests each word in `words` with the provided dfa."""
    for word in words:
        try:
            dfa.test(word)
        except AssertionError as e:
            logging.error('ERROR: %s\n' % e.message)


states  = ['q0','q1','q2','q3','q4']
alphabet = list('ab')
transitions = {
    ('q0','a'): 'q1',
    ('q0','b'): 'q3',
    ('q1','a'): 'q1',
    ('q1','b'): 'q2',
    ('q2','a'): 'q1',
    ('q2','b'): 'q2',
    ('q3','a'): 'q4',
    ('q3','b'): 'q3',
    ('q4','a'): 'q4',
    ('q4','b'): 'q3',
}
start  = 'q0'
accepts = ['q1','q3']

dfa = DFA(states,alphabet,transitions,start,accepts)

if __name__ == '__main__':

    # Configure logging
    args = sys.argv[1:]
    fmt = '%(message)s'
    if set(['-v', '--verbose']).isdisjoint(args):
        logging.basicConfig(level=logging.INFO, format=fmt)
    else:
        logging.basicConfig(level=logging.DEBUG, format=fmt)

    for func, words in dfas:
        print '-' * 50
        print 'TESTING %s' % func.__name__
        print '-' * 50
        dfa = DFA(*func())
        test(dfa, words)
