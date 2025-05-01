import numpy as np
import pandas as pd
from scipy.stats import chi2

# ---------- Datos ----------
datos_str = """
0.720565261 0.430713663 0.859623287 0.078149916 0.468333024 0.824485349
0.926715375 0.682216894 0.318670786 0.032777711 0.399389077 0.23905402
0.710246587 0.442667524 0.932940273 0.03252574 0.787136661 0.567425684
0.138171222 0.790303913 0.188998825 0.204918784 0.846519646 0.735342195
0.964034852 0.7968877   0.213710849 0.731398657 0.39878551  0.258130941
0.836468033 0.391698112 0.005887629 0.514147561 0.12936163  0.828968648
0.572754333 0.531905174 0.636752376 0.554063126 0.048001152 0.545236833
0.276891099 0.166348052 0.77943564  0.06171125  0.761148323 0.540635962
0.939009059 0.981679517 0.629338139 0.722697257 0.045466848 0.598312018
0.168496083 0.2812208   0.278225721 0.6805342   0.362273162 0.116450682
0.539925887 0.29869546  0.722560838 0.400949068 0.800996344 0.809190325
0.838728732 0.547139785 0.767274499 0.680169212 0.379912555 0.73520559
0.903234171 0.89903242  0.631687951 0.143295656 0.583885352 0.825416498
"""

# ---------- Preparar datos ----------
datos = np.array([float(num) for num in datos_str.strip().split()])
pares = np.array(list(zip(datos[:-1], datos[1:])))  # pares (xi, xi+1)

# ---------- Parámetros ----------
n = 5  # número de divisiones del intervalo [0,1]
N = len(pares)
esperado = (N - 1) / (n ** 2)
cuentas = np.zeros((n, n))  # matriz a_ij

# ---------- Contar ocurrencias en celdas ----------
for x, y in pares:
    i = min(int(x * n), n - 1)
    j = min(int(y * n), n - 1)
    cuentas[i][j] += 1

# ---------- Chi-cuadrado ----------
chi_cuadrado = (n ** 2 / (N - 1)) * np.sum((cuentas - esperado) ** 2)

# ---------- Valor crítico ----------
alpha = 0.05
gl = n**2 - 1
valor_critico = chi2.ppf(1 - alpha, gl)

# ---------- Mostrar resultados ----------
print("=== Prueba de Series ===")
print(f"N pares = {N}")
print(f"Divisiones n = {n} → Total celdas: {n}x{n}")
print(f"Grados de libertad: {gl}")
print(f"Frecuencia esperada por celda: {esperado:.4f}")
print(f"Estadístico χ² = {chi_cuadrado:.4f}")
print(f"Valor crítico χ²(1 - α) con α={alpha}: {valor_critico:.4f}")

# ---------- Conclusión ----------
if chi_cuadrado > valor_critico:
    print("\nSe rechaza H₀: los datos NO son independientes (no uniformes).")
else:
    print("\nNo se rechaza H₀: los datos podrían ser independientes y uniformes.")

# ---------- Mostrar tabla de frecuencias ----------
tabla = pd.DataFrame(cuentas, 
                    index=pd.Index([f"i={i+1}" for i in range(n)]),
                    columns=pd.Index([f"j={j+1}" for j in range(n)]))

print("\nTabla de frecuencias aᵢⱼ (conteo de pares en cada celda):")
print(tabla.to_string())
