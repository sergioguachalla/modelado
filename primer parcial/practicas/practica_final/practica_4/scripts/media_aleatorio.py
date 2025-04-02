import numpy as np
from scipy.stats import norm

# ===========================
# Número de datos aleatorios
# ===========================
n = 60  # ← Puedes cambiar este valor a cualquier entero positivo

# ===========================
# Generar datos aleatorios
# ===========================
datos = np.random.uniform(0, 1, n)

# ===========================
# Parámetros de la hipótesis
# ===========================
mu = 0.5                  # Media bajo H₀
x_bar = np.mean(datos)    # Media muestral
alpha = 0.05              # Nivel de significancia

# ===========================
# Cálculo del estadístico Z
# ===========================
Z_c = (x_bar - mu) * np.sqrt(n) / np.sqrt(1 / 12)
Z_critico = norm.ppf(1 - alpha / 2)

# ===========================
# Resultados
# ===========================
print("📊 Prueba de hipótesis para la media (Z)")
print(f"n = {n}")
print(f"Media muestral (x̄): {x_bar:.5f}")
print(f"Estadístico Z_c: {Z_c:.5f}")
print(f"Intervalo de aceptación: [-{Z_critico:.5f}, {Z_critico:.5f}]")

# ===========================
# Decisión
# ===========================
if abs(Z_c) <= Z_critico:
    print("✅ No se rechaza H₀: La media muestral es compatible con 0.5.")
else:
    print("❌ Se rechaza H₀: La media muestral es significativamente distinta de 0.5.")
