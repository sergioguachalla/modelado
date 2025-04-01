def cuadrados_medios(semilla, a, d, n):
    numeros = []  # Lista para almacenar los valores generados
    x = semilla  # Inicializamos con la semilla

    for _ in range(n):
        y = a * x  # Multiplicamos por la constante
        y_str = str(y).zfill(2 * d)  # Aseguramos que tenga suficientes dígitos con ceros a la izquierda
        centro = y_str[len(y_str)//2 - d//2 : len(y_str)//2 + d//2]  # Extraemos los dígitos centrales
        x = int(centro)  # Convertimos a entero para la siguiente iteración
        r = x / (10 ** d)  # Normalizamos el número
        
        numeros.append((x, r))  # Guardamos la tupla (X_n, R_n)

    return numeros  # Retorna la lista de valores generados


# Parámetros del problema
semilla = 9803
a = 6965
d = 4  # Número de dígitos a considerar
n = 5  # Cantidad de números a generar

# Generamos los números aleatorios
numeros_generados = cuadrados_medios(semilla, a, d, n)

# Mostramos los resultados en formato de tabla
print("| n  | X_n  | R_n   |")
print("|----|------|------|")
for i, (x, r) in enumerate(numeros_generados, start=1):
    print(f"| {i}  | {x:04} | {r:.4f} |")  # Asegura el formato exacto de 4 dígitos
