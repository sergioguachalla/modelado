import numpy as np

# ---------- DATOS ----------
datos_str = """
0.31519 0.08619 0.41177 0.79921 0.1733  0.67156 0.38659 0.50046
0.32058 0.54222 0.46175 0.09849 0.31895 0.36696 0.20886 0.45295
0.55175 0.63106 0.50499 0.88258 0.10956 0.92624 0.27487 0.08188
0.57113 0.71694 0.01317 0.30524 0.23735 0.10507 0.53491 0.26968
0.95799 0.06368 0.3556  0.7671  0.23394 0.3868  0.4041  0.24486
0.6035  0.29071 0.14863 0.16079 0.49599 0.84219 0.90026 0.59274
0.75798 0.52392 0.4617  0.61932 0.0064  0.26959 0.81892 0.14671
0.99649 0.60474 0.54769 0.30753 0.9014  0.30969 0.18583 0.63199
0.49523 0.41835 0.1751  0.15944 0.17431 0.54415 0.93388 0.02756
0.81974 0.51869 0.33442 0.51256 0.59468 0.71956 0.44815 0.66495
"""

# ---------- CONVERSIÓN ----------
datos = np.array([float(num) for num in datos_str.strip().split()])
n = len(datos)

# ---------- GENERAR SECUENCIA DE SUBIDAS (1) Y BAJADAS (0) ----------
secuencia = [1 if datos[i] > datos[i - 1] else 0 for i in range(1, n)]

# ---------- CONTAR CORRIDAS ----------
corridas = 1
for i in range(1, len(secuencia)):
    if secuencia[i] != secuencia[i - 1]:
        corridas += 1

# ---------- ESTADÍSTICOS ----------
mu_co = (2 * n - 1) / 3
sigma_co = np.sqrt((16 * n - 29) / 90)
Zc = abs((corridas - mu_co) / sigma_co)
Z_critico = 1.96  # para α = 0.05

# ---------- RESULTADOS ----------
print("=== Prueba de Corridas (Runs Test) ===")
print(f"Total de datos (n): {n}")
print(f"Número de corridas observadas (C_o): {corridas}")
print(f"Media esperada de corridas (μ_co): {mu_co:.4f}")
print(f"Desviación estándar (σ_co): {sigma_co:.4f}")
print(f"Estadístico Z_c: {Zc:.4f}")
print(f"Valor crítico Z_crit (α=0.05): {Z_critico}")

# ---------- CONCLUSIÓN ----------
if Zc > Z_critico:
    print("\n❌ Se rechaza H₀: los datos NO son independientes.")
else:
    print("\n✅ No se rechaza H₀: los datos podrían ser independientes.")
