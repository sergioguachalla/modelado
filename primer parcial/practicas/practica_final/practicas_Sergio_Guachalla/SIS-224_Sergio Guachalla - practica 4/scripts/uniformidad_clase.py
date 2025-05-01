import numpy as np
import pandas as pd
from scipy.stats import chi2

# ---------- DATOS ----------
datos_str = """
0.31519 0.08619 0.41177 0.79921 0.1733  0.67156 0.38659 0.50046 0.33869 0.09046
0.32058 0.54222 0.46175 0.09849 0.31895 0.36696 0.20886 0.45295 0.70768 0.89432
0.55175 0.63106 0.50499 0.88258 0.10956 0.92624 0.27487 0.08188 0.83345 0.12804
0.57113 0.71694 0.01317 0.30524 0.23735 0.10507 0.53491 0.26968 0.65895 0.9724
0.95799 0.06368 0.3556  0.7671  0.23394 0.3868  0.4041  0.24486 0.54872 0.42162
0.6035  0.29071 0.14863 0.16079 0.49599 0.84219 0.90026 0.59274 0.50326 0.40162
0.75798 0.52392 0.4617  0.61932 0.0064  0.26959 0.81892 0.14671 0.02313 0.52647
0.99649 0.60474 0.54769 0.30753 0.9014  0.30969 0.18583 0.63199 0.83952 0.49106
0.49523 0.41835 0.1751  0.15944 0.17431 0.54415 0.93388 0.02756 0.6913  0.31339
0.81974 0.51869 0.33442 0.51256 0.59468 0.71956 0.44815 0.66495 0.43603 0.37717
"""

# ---------- PREPARACIÓN ----------
valores = np.array([float(num) for num in datos_str.strip().split()])
n = len(valores)
min_val, max_val = np.min(valores), np.max(valores)

# ---------- INTERVALOS ----------
c = (max_val - min_val) / np.sqrt(n)  # amplitud
m = int(np.ceil((max_val - min_val) / c))  # número de intervalos
intervalos = [(min_val + i * c, min_val + (i + 1) * c) for i in range(m)]

# ---------- CONTEO ----------
conteos = [np.sum((valores >= a) & (valores < b)) for a, b in intervalos]
if max_val == intervalos[-1][1]:
    conteos[-1] += 1  # incluir el valor máximo en el último intervalo si es exacto

# ---------- ESTADÍSTICO CHI-CUADRADO ----------
esperado = n / m
chi_valores = [(obs - esperado) ** 2 / esperado for obs in conteos]
chi_total = sum(chi_valores)

# ---------- VALOR CRÍTICO ----------
alpha = 0.05
gl = m - 1
valor_critico = chi2.ppf(1 - alpha, df=gl)

# ---------- RESULTADOS ----------
print("=== Prueba de Uniformidad ===")
print(f"Número de datos: {n}")
print(f"Intervalos: {m}  |  Amplitud c = {c:.4f}")
print(f"Valor mínimo: {min_val:.5f}  |  Valor máximo: {max_val:.5f}")
print(f"Frecuencia esperada por intervalo: {esperado:.2f}")
print(f"Grados de libertad: {gl}")
print(f"Estadístico chi-cuadrado: {chi_total:.4f}")
print(f"Valor crítico χ²(1-α) con α={alpha}: {valor_critico:.4f}")

if chi_total < valor_critico:
    print("\n✅ No se rechaza H₀: los datos podrían provenir de una distribución uniforme.")
else:
    print("\n❌ Se rechaza H₀: los datos no provienen de una distribución uniforme.")

# ---------- TABLA RESUMEN ----------
tabla = pd.DataFrame({
    "Intervalo": [f"[{a:.4f}, {b:.4f})" for a, b in intervalos],
    "Conteo observado (n_io)": conteos,
    "n_ie (esperado)": [esperado] * m,
    "(n_io - n_ie)^2 / n_ie": chi_valores
})

print("\nTabla de resultados:")
print(tabla.to_string(index=False))
