def orden(ListaP, lista):
    comparativa=[]
    for e in lista:
            if e %2==0:
                comparativa.append(e)
    if ListaP==comparativa:
        return lista
    else:
        ordenar(lista)
        return orden(ListaP, lista)


def ordenar(lista):
    temp=0
    i=-1
    for j in range (len(lista)):
        if lista[j]%2==0:
            i+=1
            if temp==0:
                temp=(lista[j],j)
            if lista[i]> lista[j] and temp[0]<lista[j]:
                lista[i], lista[j]=lista[j], lista[i]
            if temp[0]>lista[j]:
                lista[j], lista[temp[1]] = lista[temp[1]], lista[j]
    return lista


lista=[1,4,8,6,3,5,2,11]
ListaP=[]
print(lista)
for e in lista:
    if e %2==0:
        ListaP.append(e)
ListaP.sort()
resultado=orden(ListaP, lista)
print(resultado)