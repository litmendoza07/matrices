matriz = []
for i in range(2):
    matriz.append([])
    for j in range(2):
        matriz[i].append(int(input(f"Ingrese el valor: ")))


print("Matriz ingresada:")
for fila in matriz:
    print(fila)

#Escalar
k = 5

matrizB = []
for i in range(len(matriz)):
    matrizB.append([])
    for j in range(len(matriz[i])):
        matrizB[i].append(k * matriz[i][j])

print("="*13)
print("Escalar" , k)
for fila in matrizB:
    print(fila)
