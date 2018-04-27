# coding=utf-8
#!/usr/bin/env python

import sys
import logging
from ndfa import DFA,NDFA,CFG


##states = list('01')
##alphabet = list('ab')
##transitions = {
##        ('0', 'a'): ['1','0'],
##        ('0', 'b'): ['1'],
##        ('1', 'a'): ['0'],
##        ('1', 'b'): ['1'],
##    }
##start = '0'
##accepts = list('0')
##
##ndfa = NDFA(states, alphabet, transitions, start, accepts)

##w = 'aa'
#print ndfa.test(w)
##print ndfa.convert()

#dfa = ndfa.convert()

variables = ['S','A','B']
alphabet = ['a','b']
initial = 'S'
rules = {
        'S' : ['AB','a'],
        'A': ['BB','AB','a'],
        'B' : ['a','b']
}

cfg = CFG(variables, alphabet, rules, initial)
w='aba'
cfg.test(w)

##states2 = list('ABCD')
##alphabet2 = list('01')
##transitions2={
##    ('A','0'):['A'],
##    ('A','1'):['A','B'],
##    ('B','1'):['C'],
##    ('C','1'):['D'],
##    ('D','0'):['D'],
##    ('D','1'):['D'],
##}
##start2 = 'A'
##accepts2 = list('D')
##
##ndfa2 = NDFA(states2,alphabet2,transitions2,start2,accepts2)
##
##w2 = "110"
#print ndfa2.test(w2) 


