

def funT(n):
    lista = []
    def fun(n,lista):
        if(n==0):
            return lista
        else:
            if n==5:
                listaP = [1,2,3,4,5,6,7,8,9,10]
                lista = listaP
            if n<0:
                #return fun(n+1,lista)
                return fun(n+1,lista)
                    
    return fun(n,lista)

print funT(5)
print funT(-5)
