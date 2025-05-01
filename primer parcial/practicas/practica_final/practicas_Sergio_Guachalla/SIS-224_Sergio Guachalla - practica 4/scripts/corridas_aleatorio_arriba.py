import numpy as np

# ---------- CONFIGURACIÓN ----------
n = 100           # Número de datos aleatorios
alpha = 0.05      # Nivel de significancia
Z_critico = 1.96  # Valor crítico para alfa = 0.05 (Z_(1-α/2))

# ---------- GENERAR DATOS ALEATORIOS ----------
datos = np.random.uniform(0, 1, n)

# ---------- GENERAR SECUENCIA DE 0s y 1s ----------
secuencia = [1 if datos[i] > datos[i - 1] else 0 for i in range(1, n)]

# ---------- CONTAR CORRIDAS ----------
corridas = 1
for i in range(1, len(secuencia)):
    if secuencia[i] != secuencia[i - 1]:
        corridas += 1

# ---------- CÁLCULOS ESTADÍSTICOS ----------
mu_co = (2 * n - 1) / 3
sigma_co = np.sqrt((16 * n - 29) / 90)
Zc = abs((corridas - mu_co) / sigma_co)

# ---------- RESULTADOS ----------
print("=== Prueba de Corridas (Runs Test) ===")
print(f"Cantidad de datos: {n}")
print(f"Número de corridas observadas: {corridas}")
print(f"Media esperada de corridas (μ_co): {mu_co:.4f}")
print(f"Desviación estándar (σ_co): {sigma_co:.4f}")
print(f"Estadístico Z_c: {Zc:.4f}")
print(f"Valor crítico Z (α={alpha}): {Z_critico}")

# ---------- CONCLUSIÓN ----------
if Zc > Z_critico:
    print("\n❌ Se rechaza H₀: los datos NO son independientes.")
else:
    print("\n✅ No se rechaza H₀: los datos podrían ser independientes.")
