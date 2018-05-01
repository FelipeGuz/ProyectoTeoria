from CFG import CFG

##nonterminals = ['s']
##terminals = ['(',')']
##rules = {
##    ('s'):('(s)','ss','e'),
##}
##start = 's'

nonterminals1 = ['S','A','B']
terminals1 = ['a','b']
start1 = 'S'
rules1 = {
        'S' : ['AB','a'],
        'A': ['BB','AB','a'],
        'B' : ['a','b'],
}

cfg1 = CFG(nonterminals1,terminals1,rules1,start1)
#print cfg1.test('aba')

nonterminals2 = ['S','A','B','C']
terminals2 = ['a','b']
start2 = 'S'
rules2 = {
    'S' : ['AB','AC','AA'],
    'A' : ['CB','a'],
    'B' : ['AC','b'],
    'C' : ['CC','b'],
}
cfg2 = CFG(nonterminals2,terminals2,rules2,start2)
#print cfg2.test('bbabb')

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
print cfg3.test('aaba')
