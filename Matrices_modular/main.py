from calculos import (
	convertir_a_identidad,
	multiplicar_matrices,
	multiplicar_por_escalar,
	sumar_matrices,
)
from presentacion import mostrar_matriz
from validaciones import leer_dimension, leer_entero, leer_matriz


def operar_escalar():
	filas = leer_dimension("Ingrese la cantidad de filas: ")
	columnas = leer_dimension("Ingrese la cantidad de columnas: ")
	matriz = leer_matriz(filas, columnas, "la matriz")
	escalar = leer_entero("Ingrese el escalar: ")
	print("Matriz multiplicada por el escalar:")
	mostrar_matriz(multiplicar_por_escalar(matriz, escalar))


def operar_suma():
	filas = leer_dimension("Ingrese la cantidad de filas: ")
	columnas = leer_dimension("Ingrese la cantidad de columnas: ")
	matriz_a = leer_matriz(filas, columnas, "la primera matriz")
	matriz_b = leer_matriz(filas, columnas, "la segunda matriz")
	print("Resultado de la suma:")
	mostrar_matriz(sumar_matrices(matriz_a, matriz_b))


def operar_multiplicacion():
	filas_a = leer_dimension("Ingrese las filas de la primera matriz: ")
	columnas_a = leer_dimension("Ingrese las columnas de la primera matriz: ")
	filas_b = leer_dimension("Ingrese las filas de la segunda matriz: ")
	columnas_b = leer_dimension("Ingrese las columnas de la segunda matriz: ")
	matriz_a = leer_matriz(filas_a, columnas_a, "la primera matriz")
	matriz_b = leer_matriz(filas_b, columnas_b, "la segunda matriz")
	try:
		resultado = multiplicar_matrices(matriz_a, matriz_b)
	except ValueError as error:
		print(f"No se pueden multiplicar las matrices: {error}")
		return
	print("Resultado de la multiplicacion:")
	mostrar_matriz(resultado)


def mostrar_diagonal_azul():
	tamaño = leer_dimension("Ingrese el tamaño de la matriz cuadrada: ")
	matriz = leer_matriz(tamaño, tamaño, "la matriz")
	print("Matriz con los unos de la diagonal principal en azul:")
	mostrar_matriz(matriz, diagonal_azul=True)


def convertir_matriz_a_identidad():
	tamaño = leer_dimension("Ingrese el tamaño de la matriz cuadrada: ")
	matriz = leer_matriz(tamaño, tamaño, "la matriz")
	print("Matriz identidad resultante:")
	mostrar_matriz(convertir_a_identidad(matriz))


def ejecutar():
	while True:
		print("\nMENU DE OPERACIONES CON MATRICES")
		print("1. Multiplicar una matriz por un escalar")
		print("2. Sumar dos matrices")
		print("3. Multiplicar dos matrices")
		print("4. Mostrar en azul los unos de la diagonal")
		print("5. Convertir matriz cuadrada a identidad")
		print("0. Salir")
		opcion = leer_entero("Seleccione una opcion: ")

		if opcion == 0:
			print("Programa finalizado.")
			break
		elif opcion == 1:
			operar_escalar()
		elif opcion == 2:
			operar_suma()
		elif opcion == 3:
			operar_multiplicacion()
		elif opcion == 4:
			mostrar_diagonal_azul()
		elif opcion == 5:
			convertir_matriz_a_identidad()
		else:
			print("Opcion no valida.")


if __name__ == "__main__":
	ejecutar()