# coding=utf-8
#!/usr/bin/env python
from ndfa import DFA
            
#Número 1:
states1 = ['q0','q1','q2']
alphabet1 = list('01')
transitions1 = {
    ('q0','1'): 'q0',
    ('q0','0'): 'q1',
    ('q1','1'): 'q0',
    ('q1','0'): 'q2',
    ('q2','0'): 'q2',
    ('q2','1'): 'q2',
}
start1 = 'q0'
accepts1 = ['q0']

dfa1 = DFA(states1,alphabet1,transitions1,start1,accepts1)

#Número 2:
states2 = ['q0','q1','q2']
alphabet2 = list('01')
transitions2 = {
    ('q0','0'):'q2',
    ('q0','1'):'q1',
    ('q1','0'):'q0',
    ('q1','1'):'q2',
    ('q2','0'):'q1',
    ('q2','1'):'q0',
}
start2 = 'q0'
accepts2 = ['q1']
dfa2 = DFA(states2,alphabet2,transitions2,start2,accepts2)

#Número 3:
states3 = ['q0','q1','q2','q3']
alphabet3 = list('ab')
transitions3 = {
    ('q0','a'):'q1',
    ('q0','b'):'q0',
    ('q1','a'):'q2',
    ('q1','b'):'q3',
    ('q2','b'):'q2',
    ('q3','a'):'q3',
    ('q3','b'):'q3',
}
start3 = 'q0'
accpts3 = ['q0']

dfa3 = DFA(states3,alphabet3,transitions3,start3,accepts3)

#Número 4:
states4  = ['q0','q1','q2','q3','q4']
alphabet4 = list('ab')
transitions4 = {
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
start4  = 'q0'
accepts4 = ['q1','q3']

dfa4 = DFA(states4,alphabet4,transitions4,start4,accepts4)

#Número 5:

states5 = ['q0','q1','q2']
alphabet5 = list('ab')
transitions5 = {
    ('q0','a'):'q1',
    ('q0','b'):'q0',
    ('q1','a'):'q2',
    ('q2','a'):'q2',
    ('q2','b'):'q0',
}
start5 = 'q0'
accepts5 = ['q0','q2']

dfa5 = DFA(states5,alphabet5,transitions5,start5,accepts5)


