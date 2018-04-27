def eliminarCaracter(word,valor):
    l=list(word)
    inicio=0
    if(len(word)<valor+1):
        return None
    else:
        for k in range(valor+1):
            print ""
            print "----->Palabra: ",word
            print "----->Valor de k: ",k
            l.pop(valor-k)
        print "----->Palabra sin algo: ",l
        palabra=""
        for i in l:
            palabra=palabra+i
        return palabra
    

                       
