def metodo_congruencial_multiplicativo(a, m, x0, n):
    numeros = [x0]  # Lista para almacenar la secuencia generada

    for _ in range(n):
        xn = (a * numeros[-1]) % m  # Aplicar la fórmula
        numeros.append(xn)  # Guardar el nuevo valor

    return numeros  # Retornar la lista de números generados


# Parámetros del problema
a = 211
m = 10**8  # 10^8
x0 = 13
n = 5  # Cantidad de números a generar

# Generar los números aleatorios
numeros_aleatorios = metodo_congruencial_multiplicativo(a, m, x0, n)

# Mostrar los resultados en formato "0, número"
print("| n  | X_n    |")
print("|----|--------|")
for i, num in enumerate(numeros_aleatorios):
    print(f"| {i}  | 0,{num} |")  # Agregamos "0," antes del número
