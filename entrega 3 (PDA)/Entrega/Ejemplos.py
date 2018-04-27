# -*- coding: cp1252 -*-
from PDA import PDA

####################################################################
#NÚMERO UNO:
#PDA que acepta: {0^n,1^n | n>=0}
states = ['q0','q1','q2','q4']
alphabet = list('01')
gamma = list('0$')
transitions = {
    ('q0',''):['q1',['','$']],
    ('q1','0'):['q1',['','0']],
    ('q1','1'):['q2',['0','']],
    ('q2','1'):['q2',['0','']],
    ('q2',''):['q3',['$','']],
}
start = 'q0'
accepts = ['q0','q3']
pda1 = PDA(states,alphabet,gamma,transitions,start,accepts)
#print pda1.test('0011')
#print pda1.generateLenguage(6)

####################################################################
#NÚMERO DOS:
#PDA que acepta: {w.w^R | R pertenece {0,1}*}
states2 = ['q1','q2','q3','q4']
alphabet2 = list('01')
gamma2 = list('01$')
transitions2 = {
    ('q1',''):['q2',['','$']],
    ('q2','0'):['q2',['','0']],
    ('q2','1'):['q2',['','1']],
    ('q2',''):['q3',['','']],
    ('q3','0'):['q3',['0','']],
    ('q3','1'):['q3',['1','']],
    ('q3',''):['q4',['$','']],
}
start2 = 'q1'
accepts2 = ['q1','q4']
pda2 = PDA(states2,alphabet2,gamma2,transitions2,start2,accepts2)
#print pda2.test('0000')
#print pda2.generateLenguage(5)

####################################################################
#NÚMERO TRES:
states3 = ['q0','q1','q2','q3','q4','q5']
alphabet3 = list('01')
gamma3 = ['A$']
transitions3 = {
    ('q0','1'):('q1',['','$']),
    ('q1','0'):('q2',['','A']),
    ('q1','1'):('q3',['','']),
    ('q2','0'):('q2',['','A']),
    ('q2','1'):('q4',['A','']),
    ('q3','0'):('q3',['','A']),
    ('q3','1'):('q4',['A','']),
    ('q4','1'):('q4',['A','']),
    ('q4',''):('q5',['$','']),
}
start3 = 'q0'
accepts3 = ['q5']
pda3 = PDA(states3,alphabet3,gamma3,transitions3,start3,accepts3)
#print pda3.generateLenguage(7)
#print pda3.test('1101')

####################################################################
#NÚMERO CUATRO:
#PDA que acepta: (0+1)* - {ww | w pertenece {0,1}*}
states4 = ['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9']
alphabet4 = list('*01')
gamma4 = list('$A')
transitions4 = {
    ('q0',''):['q1',['','$']],
    ('q0','*'):['q8',['','']],
    ('q1','*'):['q1',['','A']],
    ('q1','0'):['q2',['','']],
    ('q1','1'):['q3',['','']],
    ('q2','*'):['q2',['A','']],
    ('q2',''):['q5',['$','$']],
    ('q3','*'):['q3',['A','']],
    ('q3',''):['q4',['$','$']],
    ('q4','*'):['q4',['','A']],
    ('q4','0'):['q6',['','']],
    ('q5','*'):['q5',['','A']],
    ('q5','1'):['q6',['','']],
    ('q6','*'):['q6',['A','']],
    ('q6',''):['q7',['$','']],
    ('q8','*'):['q9',['','']],
    ('q9','*'):['q8',['','']],
}
start4 = 'q0'
accepts4 = ['q7','q8']
pda4 = PDA(states4,alphabet4,gamma4,transitions4,start4,accepts4)
#print pda4.generateLenguage(4)
#print pda4.test('01')
