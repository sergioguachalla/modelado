import numpy as np
import pandas as pd
from scipy.stats import chi2

# ---------- CONFIGURACIÓN ----------
n_datos = 100  # Número total de datos aleatorios
n_divisiones = 5  # Divisiones del intervalo [0,1]
alpha = 0.05  # Nivel de significancia

# ---------- Generar datos aleatorios ----------
datos = np.random.uniform(0, 1, n_datos)
pares = np.array(list(zip(datos[:-1], datos[1:])))  # pares (xi, xi+1)
N = len(pares)

# ---------- Inicializar matriz a_ij ----------
cuentas = np.zeros((n_divisiones, n_divisiones))
esperado = (N - 1) / (n_divisiones ** 2)

# ---------- Contar pares en celdas ----------
for x, y in pares:
    i = min(int(x * n_divisiones), n_divisiones - 1)
    j = min(int(y * n_divisiones), n_divisiones - 1)
    cuentas[i][j] += 1

# ---------- Estadístico chi-cuadrado ----------
chi_cuadrado = (n_divisiones ** 2 / (N - 1)) * np.sum((cuentas - esperado) ** 2)

# ---------- Valor crítico ----------
gl = n_divisiones**2 - 1
valor_critico = chi2.ppf(1 - alpha, gl)

# ---------- Resultados ----------
print("=== Prueba de Series con números aleatorios ===")
print(f"Cantidad de datos: {n_datos}")
print(f"N pares considerados: {N}")
print(f"Divisiones n = {n_divisiones} → Total celdas: {n_divisiones} x {n_divisiones}")
print(f"Grados de libertad: {gl}")
print(f"Frecuencia esperada por celda: {esperado:.4f}")
print(f"Estadístico χ² = {chi_cuadrado:.4f}")
print(f"Valor crítico χ²(1 - α) con α={alpha}: {valor_critico:.4f}")

# ---------- Conclusión ----------
if chi_cuadrado > valor_critico:
    print("\nSe rechaza H₀: los datos NO son independientes (no uniformes).")
else:
    print("\nNo se rechaza H₀: los datos podrían ser independientes y uniformes.")

# ---------- Tabla de frecuencias ----------
tabla = pd.DataFrame(cuentas, 
                     index=pd.Index([f"i={i+1}" for i in range(n_divisiones)]),
                     columns=pd.Index([f"j={j+1}" for j in range(n_divisiones)]))

print("\nTabla de frecuencias aᵢⱼ:")
print(tabla.to_string())
