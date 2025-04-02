def metodo_congruencial_lineal(a, c, m, x0, n):
    numeros = [x0]  # Lista para almacenar los números generados

    for _ in range(n):
        xn = (a * numeros[-1] + c) % m  # Aplicar la fórmula
        numeros.append(xn)  # Guardar el nuevo valor

    return numeros  # Retornar la lista de números generados


# Parámetros del problema
a = 81
c = 89
m = 100  # 10^2
x0 = 5
n = 5  # Cantidad de números aleatorios a generar


# Mostrar los resultados en formato de tabla


if __name__ == "__main__":
    print("Ejercicio 1")
    print("Metodo Congruencial Lineal")
    print("a = 81, c = 89, m = 100, x0 = 5, n = 5")
    numeros_aleatorios = metodo_congruencial_lineal(a, c, m, x0, n)
    print("| n  | X_n |")
    print("|----|-----|")
    for i, num in enumerate(numeros_aleatorios):
      print(f"| {i}  | {num} |")