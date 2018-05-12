from CFG import CFG
from time import time

#Ejemplo 1
nonterminals1 = ['S','A','B']
terminals1 = ['a','b']
start1 = 'S'
rules1 = {
        'S' : ['AB','a'],
        'A': ['BB','AB','a'],
        'B' : ['a','b'],
}
cfg1 = CFG(nonterminals1,terminals1,rules1,start1)

# start = time()
# n = 14
# cfg1.generateLenguage(n)
# time = time() - start
# print  "for n = ", n,"|", "time in s: ", time, "time in min : ",time/60 

# Para este ejemplo el n maximo es 14, despues de este numero el programa se demora mas de 10 min.



#Ejemplo 2
nonterminals2 = ['S','A','B','C']
terminals2 = ['a','b']
start2 = 'S'
rules2 = {
    'S':['AA'],
    'A':['AB','a'],
    'B':['CA','b'],
    'C':['AB','b'],
}
cfg2 = CFG(nonterminals2,terminals2,rules2,start2)
#print cfg2.test('bbabb')
# start = time()
# n = 16
# cfg2.generateLenguage(n)
# time = time() - start
# print  "for n = ", n,"|", "time in s: ", time, "time in min : ",time/60 

#Pare este ejemplo el n maximo es 15, despues de este numero el programa se demora mas de 10 min.

#Ejemplo 3
nonterminals3 = ['S','A','B','C']
terminals3 = ['a','b']
start3 = 'S'
rules3 = {
    'S':['AA'],
    'A':['AB','a'],
    'B':['CA','b'],
    'C':['AB','b'],
}
cfg3 = CFG(nonterminals3,terminals3,rules3,start3)
#print cfg3.test('baaba')
#start = time()
#n = 16
#cfg3.generateLenguage(n)
#time = time() - start
#print  "for n = ", n, "time : ", time, "time in min : ",time/60

#El n maximo para este ejemplo es 15, despues de este el programa tarda mas de 10 minutos


#Ejemplo 4
nonterminals4= ['S','A','B','C']
terminals4= ['a','b']
start4 = 'S'
rules4= {
    'S':['BA','AC'],
    'A':['CC','b'],
    'B':['AB','a'],
    'C':['BA','a'],
}
cfg4 = CFG(nonterminals4,terminals4,rules4,start4)
#print cfg4.test('bbab')
n = 16
start = time()
cfg4.generateLenguage(n)
time = time() - start
print  "for n = ", n, "time : ", time, "time in min : ",time/60

#Para este ejemeplo el n maximo es 15

