def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def ordenar_fila(matriz, fila):
    if fila < 0 or fila >= len(matriz):
        print("Índice de fila fuera de rango.")
        return matriz
    bubble_sort(matriz[fila])
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
matriz = [
    [9, 5, 1],
    [4, 8, 6],
    [3, 7, 2]
]

print("Matriz original:")
mostrar_matriz(matriz)

fila_a_ordenar = int(input("Introduce la fila que deseas ordenar en la matriz (0, 1 o 2): "))

matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

print(f"\nMatriz después de ordenar la fila {fila_a_ordenar}:")
mostrar_matriz(matriz_ordenada)