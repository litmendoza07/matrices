"""
Dada una matriz de Identidad n x n, mostrar en color azul solo la diagonal 1
"""
def leer_entero(mensaje):
	while True:
		try:
			return int(input(mensaje))
		except ValueError:
			print("Entrada no válida. Ingrese un número entero.")


tamaño = leer_entero("Ingrese el tamaño de la matriz cuadrada: ")
while tamaño <= 0:
	print("El tamaño debe ser mayor que cero.")
	tamaño = leer_entero("Ingrese el tamaño de la matriz cuadrada: ")

matriz = []
print("Ingrese los valores de la matriz:")
for i in range(tamaño):
	matriz.append([])
	for j in range(tamaño):
		matriz[i].append(leer_entero(f"Ingrese el valor [{i}][{j}]: "))

azul = "\033[34m"
reiniciar_color = "\033[0m"
print("Matriz ingresada:")
for i, fila in enumerate(matriz):
	valores = []
	for j, valor in enumerate(fila):
		if i == j and valor == 1:
			valores.append(f"{azul}{valor}{reiniciar_color}")
		else:
			valores.append(str(valor))
	print("[" + ", ".join(valores) + "]")
