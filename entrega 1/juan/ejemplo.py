from ndfa import DFA


states1 = list('01')
alphabet1 = list('ab')
transitions1 = {
    ('0', 'a'): '1',
    ('0','b') : '1',
    ('1','a') : '0',
    ('1','b') : '1',
    }
start1 = '0';
accepts1 = list('0')
dfa = DFA(states1, alphabet1, transitions1, start1, accepts1)

states2 = ['q0','q1','q2']
alphabet2 = list('01')
transitions2 = {
    ('q0','1'): 'q0',
    ('q0','0'): 'q1',
    ('q1','1'): 'q0',
    ('q1','0'): 'q2',
    ('q2','0'): 'q2',
    ('q2','1'): 'q2',
}
start2 = 'q0'
accepts2 = ['q2']

dfa2 = DFA(states2,alphabet2,transitions2,start2,accepts2)

states3 = list("ABC")
alphabet3 = list("12")
transitions3 = {
    ('A','2'):'A',
    ('A','1'):'B',
    ('B','1'):'A',
    ('B','2'):'C',
    ('C','1'):'C',
    ('C','2'):'B',
}
start3 = 'A'
accepts3 = list('ABC')

dfa3 = DFA(states3,alphabet3,transitions3,start3,accepts3)


print dfa3.generateLenguage(3)
    
