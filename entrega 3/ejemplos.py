from DTM import DTM

states = ['q0','q1','q2','q3','qA','qR']
alphabet = ['(',')']
gamma = ['(','(*','X','X*','_']
transitions = {
    ('q0','('):['q1','(*','R'],
    ('q1',')'):['q2','X','L'],
    ('q1','_'):['q3','_','L'],
    ('q2','('):['q1','X','R'],
    ('q2','X*'):['qR','-',None],
    ('q3','('):['qR','-',None],
    ('q3','(*'):['qR','-',None],
    ('q3','X*'):['qA','-',None],
}
start = 'q0'
accepts = ['qA']
reject = ['qR']
dtm1 = DTM(states,alphabet,gamma,transitions,start,accepts,reject)
dtm1.test("((()))")
