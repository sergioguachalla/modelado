def multiplicative_congruential(x0, a, c, m, n):
    results = [x0]
    x = x0
    for i in range(n):
        x = (a * x * c) % m
        results.append(x)
    return results

print("\n=== Método Congruencial Multiplicativo ===")
x0_mult = 13
a_mult = 211
c_mult = 16
m_mult = 10**8
n_mult = 5
results_mult = multiplicative_congruential(x0_mult, a_mult, c_mult, m_mult, n_mult)
for i, x in enumerate(results_mult):
    R = x / m_mult  # Número normalizado (entre 0 y 1)
    print(f"X_{i} = {x}, R_{i} = {R:.5f}")