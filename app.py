import numpy as np

def obtener_menor(matriz, fila, columna):
    """Obtiene la submatriz eliminando una fila y columna específicas."""
    return [row[:columna] + row[columna + 1:] for i, row in enumerate(matriz) if i != fila]

def calcular_determinante(matriz, nivel=0):
    """Calcula el determinante de una matriz mediante cofactores."""
    n = len(matriz)
    if n == 2:  # Caso base
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    determinante = 0
    for columna in range(n):
        menor = obtener_menor(matriz, 0, columna)
        signo = (-1) ** columna  # Alterna el signo
        cofactor = matriz[0][columna] * calcular_determinante(menor, nivel + 1)
        determinante += signo * cofactor
        
        # Mostrar pasos
        print(f"Nivel {nivel + 1}: Cofactor para elemento {matriz[0][columna]} = {cofactor} (signo: {signo})")
    return determinante

def regla_de_cramer(matriz, vector):
    """Resuelve un sistema de ecuaciones lineales por la regla de Cramer."""
    n = len(matriz)
    det_a = calcular_determinante(matriz)
    if det_a == 0:
        raise ValueError("El determinante de la matriz es cero. El sistema no tiene solución única.")
    
    soluciones = []
    for i in range(n):
        matriz_modificada = [row[:] for row in matriz]
        for j in range(n):
            matriz_modificada[j][i] = vector[j]
        
        det_mod = calcular_determinante(matriz_modificada)
        solucion = det_mod / det_a
        soluciones.append(solucion)
        
        print(f"Paso {i + 1}: Determinante modificado = {det_mod}, Solución x{i + 1} = {solucion}")
    
    return soluciones

def calcular_inversa(matriz):
    """Calcula la inversa de una matriz utilizando numpy."""
    det_a = calcular_determinante(matriz)
    if det_a == 0:
        raise ValueError("El determinante de la matriz es cero. La matriz no es invertible.")
    
    print("\nCalculando la matriz inversa paso a paso...")
    inversa = np.linalg.inv(np.array(matriz))
    return inversa

# Métodos principales
def metodo_cofactores():
    print("\nMétodo de Cofactores: Cálculo del determinante")
    n = int(input("Ingresa la dimensión de la matriz (n): "))
    
    matriz = []
    print("Ingresa los elementos de la matriz fila por fila:")
    for i in range(n):
        fila = list(map(float, input(f"Fila {i + 1}: ").split()))
        matriz.append(fila)
    
    print("\nMatriz ingresada:")
    for fila in matriz:
        print(fila)
    
    det = calcular_determinante(matriz)
    print(f"\nDeterminante de la matriz: {det}")

def metodo_cramer():
    print("\nRegla de Cramer: Resolución de sistemas de ecuaciones")
    n = int(input("Ingresa la dimensión de la matriz (n): "))
    
    matriz = []
    print("Ingresa los elementos de la matriz coeficientes fila por fila:")
    for i in range(n):
        fila = list(map(float, input(f"Fila {i + 1}: ").split()))
        matriz.append(fila)
    
    vector = list(map(float, input("\nIngresa los términos independientes (separados por espacios): ").split()))
    
    print("\nMatriz ingresada:")
    for fila in matriz:
        print(fila)
    print("Vector de términos independientes:", vector)
    
    soluciones = regla_de_cramer(matriz, vector)
    print("\nSoluciones del sistema:")
    for i, sol in enumerate(soluciones, 1):
        print(f"x{i} = {sol}")

def metodo_inversa():
    print("\nMétodo de Inversas: Cálculo de la matriz inversa")
    n = int(input("Ingresa la dimensión de la matriz (n): "))
    
    matriz = []
    print("Ingresa los elementos de la matriz fila por fila:")
    for i in range(n):
        fila = list(map(float, input(f"Fila {i + 1}: ").split()))
        matriz.append(fila)
    
    print("\nMatriz ingresada:")
    for fila in matriz:
        print(fila)
    
    try:
        inversa = calcular_inversa(matriz)
        print("\nMatriz inversa:")
        print(inversa)
    except ValueError as e:
        print(f"Error: {e}")

# Programa principal
def main():
    print("Resolución de matrices (3 métodos)")
    print("1. Método de Cofactores (Determinante)")
    print("2. Regla de Cramer (Sistemas de ecuaciones)")
    print("3. Método de Inversas (Matriz inversa)")
    
    opcion = int(input("Elige un método (1-3): "))
    
    if opcion == 1:
        metodo_cofactores()
    elif opcion == 2:
        metodo_cramer()
    elif opcion == 3:
        metodo_inversa()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
