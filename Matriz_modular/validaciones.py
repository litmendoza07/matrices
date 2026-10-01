def leer_entero(mensaje):
	while True:
		try:
			return int(input(mensaje))
		except ValueError:
			print("Entrada no valida. Ingrese un numero entero.")


def leer_dimension(mensaje):
	while True:
		valor = leer_entero(mensaje)
		if valor > 0:
			return valor
		print("La dimension debe ser mayor que cero.")


def leer_matriz(filas, columnas, nombre):
	matriz = []
	print(f"Ingrese los valores de {nombre}:")
	for i in range(filas):
		fila = []
		for j in range(columnas):
			fila.append(leer_entero(f"Ingrese el valor [{i}][{j}]: "))
		matriz.append(fila)
	return matriz


def validar_matriz(matriz):
	if not matriz or not matriz[0]:
		raise ValueError("La matriz no puede estar vacia.")

	columnas = len(matriz[0])
	if any(len(fila) != columnas for fila in matriz):
		raise ValueError("Todas las filas deben tener la misma cantidad de columnas.")

	return len(matriz), columnas


def validar_matriz_cuadrada(matriz):
	filas, columnas = validar_matriz(matriz)
	if filas != columnas:
		raise ValueError("La matriz debe ser cuadrada.")
	return filas


def validar_matrices_misma_dimension(matriz_a, matriz_b):
	dimensiones_a = validar_matriz(matriz_a)
	dimensiones_b = validar_matriz(matriz_b)
	if dimensiones_a != dimensiones_b:
		raise ValueError("Las matrices deben tener las mismas dimensiones.")


def validar_multiplicacion(matriz_a, matriz_b):
	filas_a, columnas_a = validar_matriz(matriz_a)
	filas_b, columnas_b = validar_matriz(matriz_b)
	if columnas_a != filas_b:
		raise ValueError("Las columnas de la primera matriz deben coincidir con las filas de la segunda.")
	return filas_a, columnas_a, columnas_b