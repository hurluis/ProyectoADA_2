def potencia_de_dos(n):
    # Caso base
    if n == 1:
        return 2
    # Relación de recurrencia
    return 2 * potencia_de_dos(n - 1)

# Ejemplo de uso
n = int(input("Ingresa el valor de n: "))
print(f"El {n}-ésimo término de la secuencia es: {potencia_de_dos(n)}")