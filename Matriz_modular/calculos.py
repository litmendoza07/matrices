from validaciones import (
	validar_matrices_misma_dimension,
	validar_matriz,
	validar_matriz_cuadrada,
	validar_multiplicacion,
)


def multiplicar_por_escalar(matriz, escalar):
	filas, columnas = validar_matriz(matriz)
	return [
		[valor * escalar for valor in fila]
		for fila in matriz
	]


def convertir_a_identidad(matriz):
	tamaño = validar_matriz_cuadrada(matriz)
	return [
		[1 if i == j else 0 for j in range(tamaño)]
		for i in range(tamaño)
	]


def sumar_matrices(matriz_a, matriz_b):
	validar_matrices_misma_dimension(matriz_a, matriz_b)
	return [
		[valor_a + valor_b for valor_a, valor_b in zip(fila_a, fila_b)]
		for fila_a, fila_b in zip(matriz_a, matriz_b)
	]


def multiplicar_matrices(matriz_a, matriz_b):
	filas_a, columnas_a, columnas_b = validar_multiplicacion(matriz_a, matriz_b)
	resultado = []
	for i in range(filas_a):
		fila = []
		for j in range(columnas_b):
			valor = 0
			for k in range(columnas_a):
				valor += matriz_a[i][k] * matriz_b[k][j]
			fila.append(valor)
		resultado.append(fila)
	return resultado