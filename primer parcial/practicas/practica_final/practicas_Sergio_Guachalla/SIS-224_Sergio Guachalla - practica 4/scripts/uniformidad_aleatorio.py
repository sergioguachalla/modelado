import numpy as np
import pandas as pd
from scipy.stats import chi2

# ---------- CONFIGURACIÓN ----------
n = 100               # Número de datos aleatorios
alpha = 0.05          # Nivel de significancia

# ---------- GENERAR DATOS ----------
valores = np.random.uniform(0, 1, n)
min_val, max_val = np.min(valores), np.max(valores)

# ---------- INTERVALOS ----------
c = (max_val - min_val) / np.sqrt(n)           # Amplitud del intervalo
m = int(np.ceil((max_val - min_val) / c))      # Número de intervalos
intervalos = [(min_val + i * c, min_val + (i + 1) * c) for i in range(m)]

# ---------- CONTEO POR INTERVALO ----------
conteos = [np.sum((valores >= a) & (valores < b)) for a, b in intervalos]
if max_val == intervalos[-1][1]:
    conteos[-1] += 1  # incluir el máximo si coincide

# ---------- PRUEBA CHI-CUADRADO ----------
esperado = n / m
chi_valores = [(obs - esperado) ** 2 / esperado for obs in conteos]
chi_total = sum(chi_valores)

# ---------- VALOR CRÍTICO ----------
gl = m - 1
valor_critico = chi2.ppf(1 - alpha, df=gl)

# ---------- RESULTADOS ----------
print("=== Prueba de Uniformidad ===")
print(f"Datos generados: {n}")
print(f"Intervalos creados: {m}  |  Amplitud c = {c:.4f}")
print(f"Min: {min_val:.4f}  |  Max: {max_val:.4f}")
print(f"Esperado por intervalo: {esperado:.2f}")
print(f"Grados de libertad: {gl}")
print(f"Estadístico χ²: {chi_total:.4f}")
print(f"Valor crítico χ² (1 - α) con α={alpha}: {valor_critico:.4f}")

# ---------- CONCLUSIÓN ----------
if chi_total < valor_critico:
    print("\n✅ No se rechaza H₀: los datos podrían provenir de una distribución uniforme.")
else:
    print("\n❌ Se rechaza H₀: los datos no provienen de una distribución uniforme.")

# ---------- TABLA ----------
tabla = pd.DataFrame({
    "Intervalo": [f"[{a:.4f}, {b:.4f})" for a, b in intervalos],
    "Conteo observado": conteos,
    "Esperado (n_ie)": [esperado] * m,
    "Chi individual": chi_valores
})

print("\nTabla de frecuencias por intervalo:")
print(tabla.to_string(index=False))
