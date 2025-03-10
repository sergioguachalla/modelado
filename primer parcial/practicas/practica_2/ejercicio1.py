def linear_congruential(x0, a, c, m, n):
    results = [x0]
    x = x0
    for i in range(n):
        x = (a * x + c) % m
        results.append(x)
    return results

print("=== Método Congruencial Lineal ===")
x0_linear = 5
a_linear = 81
c_linear = 89
m_linear = 100  # 10²
n_linear = 5    # Generar 5 números (además de la semilla)
results_linear = linear_congruential(x0_linear, a_linear, c_linear, m_linear, n_linear)
for i, x in enumerate(results_linear):
    print(f"X_{i} = {x}")