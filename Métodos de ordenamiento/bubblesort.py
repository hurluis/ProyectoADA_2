def bubble_sort(arr, n):
    i = 0
    counter = 0

    while i < n:
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1
            continue
        counter += 1
        i += 1
    
    if counter == n:
        return
    else:
        bubble_sort(arr, n)

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print(arr)
bubble_sort(arr, len(arr)-1)
print(arr)