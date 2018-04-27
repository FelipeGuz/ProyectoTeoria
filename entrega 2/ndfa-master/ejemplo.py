from ndfa import DFA
from NFAclass import NFA

states = list('01')
alphabet = list('ab')
transitions = {
    ('0','a'):'1',
    ('0','b'):'0',
    ('1','a'):['0','1'],
    ('1','b'):'1',
}
start  = '0'
accepts = list('0')

#dfa = DFA(states,alphabet,transitions,start,accepts)
#print dfa.test('b')

#print '----------------------------------'

nfa = NFA(states,alphabet,transitions,start,accepts)
#print nfa.test_nfa2('babaaba',start,0)

states2 = list('ABCD')
alphabet2 = list('01')
transitions2={
    ('A','0'):'A',
    ('A','1'):['A','B'],
    ('B','1'):'C',
    ('C','1'):'D',
    #('C','0'): 'D',
    ('D','0'):'D',
    ('D','1'):'D',
}
start2 = 'A'
accepts2 = list('D')

nfa2 = NFA(states2,alphabet2,transitions2,start2,accepts2)
#print nfa2.test_nfa2('011111',start2,0)
