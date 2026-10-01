AZUL = "\033[34m"
REINICIAR_COLOR = "\033[0m"


def mostrar_matriz(matriz, diagonal_azul=False):
	for i, fila in enumerate(matriz):
		valores = []
		for j, valor in enumerate(fila):
			if diagonal_azul and i == j and valor == 1:
				valores.append(f"{AZUL}{valor}{REINICIAR_COLOR}")
			else:
				valores.append(str(valor))
		print("[" + ", ".join(valores) + "]")