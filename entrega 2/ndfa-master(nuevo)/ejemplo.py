from NFA import NDFA,DFA
import time

startTime = time.time()

states = list('01')
alphabet = list('ab')
transitions = {
        ('0', 'a'): ['1'],
        ('0', 'b'): ['0'],
        ('1', 'a'): ['1','0'],
        ('1', 'b'): ['1'],
    }
start = '0'
accepts = list('0')

ndfa = NDFA(states, alphabet, transitions, start, accepts)
#print ndfa.test('aaba')
#print ndfa.convert()

states2 = ['q0','q1','q2']
alphabet2 = list('01')
transitions2 = {
    ('q0','1'): ['q0'],
    ('q0','0'): ['q1'],
    ('q1','1'): ['q1','q2'],
    ('q1','0'): ['q1'],
    ('q2','1'): ['q2'],
    ('q2','0'): ['q2'],
}
start2 = 'q0'
accepts2 = ['q2']

ndfa2 = NDFA(states2,alphabet2,transitions2,start2,accepts2)
#print ndfa2.convert()

states3 = ['q0','q1','q2','q3']
alphabet3 = list('01')
transitions3 = {
    ('q0','0'):['q0','q3'],
    ('q0','1'):['q1'],
    ('q1','0'):['q0','q1'],
    ('q1','1'):['q2'],
    ('q2','0'):['q0'],
    ('q2','1'):['q3'],
    ('q3','0'):['q3'],
    ('q3','1'):['q3'],
}
start3 = 'q0'
accepts3 = ['q3']

ndfa3 = NDFA(states3,alphabet3,transitions3,start3,accepts3)
#print ndfa3.convert()

states4 = ['q0','q1','q2','q3']
alphabet4 = list('01')
transitions4={
    ('q0','0'):['q0'],
    ('q0','1'):['q0','q1'],
    ('q1','1'):['q2'],
    ('q2','1'):['q3'],
    ('q3','0'):['q3'],
    ('q3','1'):['q3'],
}
start4 = 'q0'
accepts4 = ['q3']

ndfa4 = NDFA(states4,alphabet4,transitions4,start4,accepts4)
#print ndfa4.test('010')
#print ndfa4.convert()
dfa = ndfa4.convert()
#print dfa.test('10110')
#print dfa.generateLenguage(5)


states5 = list('01')
alphabet5 = list('ab')
transitions5 = {
    ('0','a'): ['0','1'],
    ('0','b'): ['1'],
    ('1','b'): ['0','1'],
    }
start5 = '0'
accepts5 = list('0')

ndfa5 = NDFA(states5,alphabet5,transitions5,start5,accepts5)
#print ndfa5.test('bb')
#print ndfa5.convert()
###################################3
#dfa = ndfa5.convert()
#print dfa.test('ba')


states6 = ['0','1','2']
alphabet6 = list('ab')
transitions6 = {
    ('0','a'):['0','1'],
    ('1','b'):['2'],
}
start6 = '0'
accepts6 = ['0','2']

ndfa6 = NDFA(states6,alphabet6,transitions6,start6,accepts6)
#print ndfa6.convert()
dfa = ndfa6.convert()
#print dfa.test('baaaaa')
print dfa.generateLenguage(15)
print time.time()-startTime


