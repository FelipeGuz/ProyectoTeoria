from ndfa import DFA
import time


states = ['0','1']
alphabet = list('ab')
transitions = {
    ('0', 'a'): '1',
    #('0', 'b'): '0',
    #('1', 'a'): '0',
    ('1', 'b'): '0',
}
start = '0'
accepts = ['0']

dfa = DFA(states, alphabet, transitions, start, accepts)

print 'Probando cadena vacia'
print dfa.test('')
print 'Probando aababa'
print dfa.test('aababa')
print 'Probando baaa'
print dfa.test('baaa')
#print dfa.test('foo')
print 'Probando generateLanguage'


n = 50
#BF
start = time.time()
#todas1 = dfa.generateLanguage(n)
#print todas1
end = time.time()
#print end - start

start = time.time()
#Busqueda
todas2 = dfa.find(dfa.start,n,"",[])
todas2 = list(set(todas2))
print todas2
#print todas2
end = time.time()
print end - start

#print set(todas2) == set(todas1)












