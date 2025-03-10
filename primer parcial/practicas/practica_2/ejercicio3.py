def middle_square_method(x0, a, D, n):
    results = []
    x = x0
    for i in range(n):
        Y = a * x
        Y_str = str(Y)
        # Para obtener los dígitos centrales según el enunciado:
        # - En la primera iteración (Y₀ con 8 dígitos) se toma a partir del índice 3
        # - En las siguientes iteraciones se toma a partir del índice 2
        if i == 0 and len(Y_str) == 8:
            start = 3
        else:
            start = 2
        substring = Y_str[start:start+D]
        # Si la cadena obtenida tiene menos de D dígitos, se rellena con ceros a la izquierda.
        if len(substring) < D:
            substring = substring.zfill(D)
        x = int(substring)
        R = x / (10**D)
        results.append((x, R))
    return results

print("\n=== Algoritmo de Cuadrados Medios ===")
x0_ms = 9803
a_ms = 6965
D_ms = 4
n_ms = 5
results_ms = middle_square_method(x0_ms, a_ms, D_ms, n_ms)
for i, (x, R) in enumerate(results_ms, start=1):
    # Se muestra X con D dígitos (rellenando con ceros si es necesario)
    x_str = str(x).zfill(D_ms)
    print(f"X_{i} = {x_str}, R_{i} = {R:.4f}")