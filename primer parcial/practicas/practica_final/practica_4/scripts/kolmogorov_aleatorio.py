import numpy as np
import math

# ===============================
# Paso 1: Generar n datos aleatorios entre 0 y 1
# ===============================
n = 50  # ← Cambia este valor a cualquier número que desees
valores = np.random.uniform(0, 1, n)

# ===============================
# Paso 2: Ordenar los datos
# ===============================
valores_ordenados = np.sort(valores)

# ===============================
# Paso 3: Calcular F_n(x) = i/n
# ===============================
Fn = np.arange(1, n + 1) / n

# ===============================
# Paso 4: Calcular |F_n(x_i) - x_i|
# ===============================
diferencias = np.abs(Fn - valores_ordenados)

# ===============================
# Paso 5: Estadístico Dn
# ===============================
Dn = np.max(diferencias)

# ===============================
# Paso 6: Valor crítico para α dado
# ===============================
alpha = 0.05
dn_critico = np.sqrt(-np.log(alpha / 2) / (2 * n))

# ===============================
# Resultados
# ===============================
print("=== Prueba de Kolmogorov-Smirnov ===")
print(f"n = {n}")
print(f"Nivel de significancia α = {alpha}")
print(f"Estadístico Dn = {Dn:.5f}")
print(f"Valor crítico d_n = {dn_critico:.5f}")

# ===============================
# Conclusión
# ===============================
if Dn < dn_critico:
    print("\n✅ No se rechaza H₀: los datos podrían provenir de una distribución uniforme U(0,1).")
else:
    print("\n❌ Se rechaza H₀: los datos NO provienen de una distribución uniforme.")
