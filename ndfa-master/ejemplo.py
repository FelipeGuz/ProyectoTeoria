from ndfa import DFA
from NFAclass import NFA

states = list('01')
alphabet = list('ab')
transitions = {
    ('0','a'):'1',
    ('0','b'):'0',
    ('1','a'):'0',
    ('1','b'):['1','1'],
}
start  = '0'
accepts = list('0')

dfa = DFA(states,alphabet,transitions,start,accepts)
print dfa.test('b')

print '----------------------------------'

nfa = NFA(states,alphabet,transitions,start,accepts)
print nfa.test_nfa('aaba')
