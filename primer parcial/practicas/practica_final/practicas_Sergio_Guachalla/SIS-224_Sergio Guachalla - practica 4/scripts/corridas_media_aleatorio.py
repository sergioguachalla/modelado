import numpy as np

# ---------- CONFIGURACIÓN ----------
n = 100             # Cantidad de números aleatorios
media = 0.5         # Valor de referencia (media teórica)
alpha = 0.05        # Nivel de significancia
Z_critico = 1.96    # Valor crítico para α = 0.05 (Z_(1-α/2))

# ---------- GENERAR DATOS ----------
datos = np.random.uniform(0, 1, n)

# ---------- BINARIZACIÓN RESPECTO A LA MEDIA ----------
binarios = np.array([1 if x > media else 0 for x in datos])
n1 = np.sum(binarios)
n0 = n - n1

# ---------- CONTAR CORRIDAS ----------
corridas = 1
for i in range(1, n):
    if binarios[i] != binarios[i - 1]:
        corridas += 1

# ---------- ESTADÍSTICOS ----------
mu_co = (2 * n0 * n1) / n + 0.5
var_co = (2 * n0 * n1 * (2 * n0 * n1 - n)) / (n**2 * (n - 1))
sigma_co = np.sqrt(var_co)
Zc = (corridas - mu_co) / sigma_co

# ---------- RESULTADOS ----------
print("=== Prueba de Corridas respecto a la Media ===")
print(f"Números generados: {n}")
print(f"Media de comparación: {media}")
print(f"Cantidad de 1s (> media): {n1}")
print(f"Cantidad de 0s (<= media): {n0}")
print(f"Corridas observadas: {corridas}")
print(f"Media esperada (μ_co): {mu_co:.4f}")
print(f"Desviación estándar (σ_co): {sigma_co:.4f}")
print(f"Estadístico Zc: {Zc:.4f}")
print(f"Valor crítico Z (α = {alpha}): ±{Z_critico}")

# ---------- CONCLUSIÓN ----------
if abs(Zc) > Z_critico:
    print("\n❌ Se rechaza H₀: los datos NO son independientes respecto a la media.")
else:
    print("\n✅ No se rechaza H₀: los datos podrían ser independientes respecto a la media.")
