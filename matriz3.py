#Suma de matrices 
"""Leer 2 matrices 3 x 3 y sumar en una matriz"""

matrizA = []
matrizB = []

print("Ingrese los valores de la primera matriz")
for i in range(3):
	matrizA.append([])
	for j in range(3):
		valor = int(input(f"Ingrese el valor: "))
		matrizA[i].append(valor)

print("Ingrese los valores de la segunda matriz")
for i in range(3):
	matrizB.append([])
	for j in range(3):
		valor = int(input(f"Ingrese el valor:"))
		matrizB[i].append(valor)

matrizSuma = []
for i in range(3):
	matrizSuma.append([])
	for j in range(3):
		matrizSuma[i].append(matrizA[i][j] + matrizB[i][j])

print("Matriz resultante de la suma:")
for fila in matrizSuma:
	print(fila)
