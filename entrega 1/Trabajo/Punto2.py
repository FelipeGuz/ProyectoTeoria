from ndfa_Punto2 import DFA

states = ['q0','q1','q2']
alphabet = list('01')
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

print dfa.generateLenguage(5)
#print dfa.generateLenguage(10)
#print dfa.generateLenguage(30)
#print dfa.generateLenguage(50)


