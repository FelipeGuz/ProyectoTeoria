from NFA import DFA,NDFA
import time

startTime = time.time()
tiempo = 21 #Cantidad maxima que hacen los cuatro en menos de 10 minutos

#Numero 1:
print "Numero 1:"


states1 = ['q0','q1','q2','q3','q4']
alphabet1 = list('ab')
transitions1 = {
    ('q0','a'):['q1','q3'],
    ('q0','b'):['q3'],
    ('q1','a'):['q2'],
    ('q1','b'):['q2'],
    ('q2','a'):['q1'],
    ('q3','b'):['q4'],
    ('q4','a'):['q3'],
    ('q4','b'):['q3'],
}
start1 = 'q0'
accepts1 = ['q0','q1','q2','q3','q4']

word = 'abaaabaa'
ndfa1 = NDFA(states1,alphabet1,transitions1,start1,accepts1)
print "Es acpetado abaabbaa?: ",ndfa1.test(word) 
dfa1 = ndfa1.convertToDFA()
print "Pasandolo a determinista acepta el string abaabbaa?: ",dfa1.test(word)
startTime = time.time()
#Maximo tiempo alcansado para 21 es: 576.243000031
dfa1.generateLenguage(tiempo)
print time.time()-startTime

#Numero 2:
print '----------------------------------'
print "Numero 2:"

states2 = ['q0','q1','q2','q3']
alphabet2 = list('01')
transitions2 = {
    ('q0','0'):['q0','q3'],
    ('q0','1'):['q1'],
    ('q1','0'):['q0','q1'],
    ('q1','1'):['q2'],
    ('q2','0'):['q0'],
    ('q2','1'):['q3'],
    ('q3','0'):['q3'],
    ('q3','1'):['q3'],
}
start2 = 'q0'
accepts2 = ['q3']

word2 = '0100111'
ndfa2 = NDFA(states2,alphabet2,transitions2,start2,accepts2)

print "Es acpetado 0100111?: ",ndfa2.test(word2) 
dfa2 = ndfa2.convertToDFA()
print "Pasandolo a determinista acepta el string 0100111?: ",dfa2.test(word2)
startTime = time.time()
#Maximo tiempo alcansado para 21 es: 525.120999813
dfa2.generateLenguage(tiempo)
print time.time()-startTime

#Numero 3:
print '-----------------------'
print "Numero 3:"

states3 = ['0','1','2']
alphabet3 = list('ab')
transitions3 = {
    ('0','a'):['0','1'],
    ('1','b'):['2'],
}
start3 = '0'
accepts3 = ['0','2']

word3 = 'abaaabaa'
ndfa3 = NDFA(states3,alphabet3,transitions3,start3,accepts3)

print "Es acpetado abaaabaa?: ",ndfa3.test(word3) 
dfa3 = ndfa3.convertToDFA()
print "Pasandolo a determinista acepta el string abaaabaa?: ",dfa3.test(word3)
startTime = time.time()
#Maximo tiempo alcansado para 21 es: 505.171999931
dfa3.generateLenguage(tiempo)
print time.time()-startTime


#Numero 4:
print '----------------------------------------------'
print "Numero 4:"

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

word4 = '0100111'
ndfa4 = NDFA(states4,alphabet4,transitions4,start4,accepts4)

print "Es acpetado 0100111?: ",ndfa4.test(word4) 
dfa4 = ndfa4.convertToDFA()
print "Pasandolo a determinista acepta el string 0100111?: ",dfa4.test(word4)
startTime = time.time()
#Maximo tiempo alcansado para 21 es: 518.855000019
dfa4.generateLenguage(tiempo)
print time.time()-startTime
