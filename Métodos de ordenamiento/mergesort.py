def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    middle = len(arr) // 2
    left_array = arr[:middle]
    right_array = arr [middle:]

    sorted_left_array = mergeSort(left_array)
    sorted_right_array = mergeSort(right_array)

    return Merge(sorted_left_array, sorted_right_array)


def Merge(left_arr, right_arr):
    arr_resultado = []

    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] > right_arr[0]:
            arr_resultado.append(right_arr[0])
            right_arr.pop(0)

        else:
            arr_resultado.append(left_arr[0])
            left_arr.pop(0)

    while len(left_arr) > 0:
        arr_resultado.append (left_arr[0])
        left_arr.pop(0)

    while len(right_arr) > 0:
        arr_resultado. append(right_arr [0])
        right_arr.pop(0)

    return arr_resultado


lista1 = [4,7,2,11,8,9,5,10]
lista2 = [1,12,14,16,11,21,19,10]
lista = lista1 + lista2 
print(lista)
resultado=mergeSort(lista)
print(resultado)