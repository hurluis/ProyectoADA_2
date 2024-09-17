def orden_par(lista):
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            for j in range(len(lista)):
                if lista[j] % 2 == 0:
                    if lista[j] > lista[i]:
                        lista[i],lista[j] = lista[j],lista[i]
    return lista


lista1 = [6,3,4,9,2,5,2]
print(lista1)
orden_par(lista1)
print(lista1)