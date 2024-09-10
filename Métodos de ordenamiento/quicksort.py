def quick_sort(lista, menor, mayor):
  if menor < mayor:
    # Dividir y acomodar pivote
    pivote = partir_lista(lista, menor, mayor)
  
    quick_sort(lista, menor, pivote - 1)
    quick_sort(lista, pivote + 1, mayor)
 
def partir_lista(lista, menor, mayor):  
  # Pivote el de la derecha
  pivote = lista[mayor]
  
  # Apuntador del último elemento más pequeño
  i = menor - 1
 
  for j in range(menor, mayor):
    if lista[j] <= pivote:
      # Avanzar apuntador
      i = i + 1
      # Intercambiar elementos
      (lista[i], lista[j]) = (lista[j], lista[i])
  
  # Al final intercambiar el pivote
  (lista[i + 1], lista[mayor]) = (lista[mayor], lista[i + 1])
  
  # Regresa la posición final del pivote
  return i + 1
 
lista1 = [4,7,2,11,8,9,5,10]
lista2 = [1,12,14,16,11,21,19,10]
lista = lista1 + lista2 
print(lista)
quick_sort(lista, 0, len(lista)-1)
print(lista)