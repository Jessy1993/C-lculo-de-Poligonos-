def quicksort(arreglo, izquierda, derecha):
    if izquierda < derecha:
        indiceParticion = particion(arreglo, izquierda, derecha)
        quicksort(arreglo, izquierda, indiceParticion)
        quicksort(arreglo, indiceParticion + 1, derecha)

def particion(arreglo, izquierda, derecha):
    pivote = arreglo[izquierda]
    while True:
        while arreglo[izquierda] < pivote:
            izquierda += 1
        while arreglo[derecha] > pivote:
            derecha -= 1
        if izquierda >= derecha:
            return derecha
        else:
            arreglo[izquierda], arreglo[derecha] = arreglo[derecha], arreglo[izquierda]
            izquierda += 1
            derecha -= 1

def burbuja(arregloB):
    n = len(arregloB)
    for i in range(n-1):
        intercambio = False
        for j in range(n-1-i):
            if arregloB[j] > arregloB[j+1] :
                arregloB[j], arregloB[j+1] = arregloB[j+1], arregloB[j]
                intercambio = True
        if intercambio == False:
            break

# ordenar lista
arreglo = [[8, 3, 1, 19, 14],[ 5, 1, 5, 1, 234, 12, 121,312, 312, 31, 23, 12, 3123, 123],[55,16,77]]
print("------------------------")
print("El arreglo es: " + str(arreglo))
print("------------------------")
fila = int(input("Ingrese el numero de lista [0],[1],[2]"))
orden = input("[S]ort, [R]everse, [B]ubbleSort, [Q]uicksort")
print("------------------------")
if orden == "S":
    arreglo[fila].sort()
if orden == "R":
    arreglo[fila].sort(reverse=True)
if orden == "B":
  burbuja(arreglo[fila])
if orden == "Q":
  quicksort(arreglo[fila], 0, len(arreglo[fila]) - 1)
print("El nuevo arreglo es: " + str(arreglo))
print("------------------------")