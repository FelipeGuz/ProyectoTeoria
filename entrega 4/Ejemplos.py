from CFG import CFG

##nonterminals = ['s']
##terminals = ['(',')']
##rules = {
##    ('s'):('(s)','ss','e'),
##}
##start = 's'

nonterminals = ['S','A','B']
terminals = ['a','b']
start = 'S'
rules = {
        'S' : ['AB','a'],
        'A': ['BB','AB','a'],
        'B' : ['a','b'],
}

cfg = CFG(nonterminals,terminals,rules,start)
print cfg.test('aba')
