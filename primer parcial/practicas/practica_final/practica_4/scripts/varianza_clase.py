import numpy as np
from scipy.stats import chi2

# Datos proporcionados (25 valores)
r = np.array([
    0.78349, 0.93508, 0.49143, 0.00619, 0.97379,
    0.34502, 0.70355, 0.11511, 0.41094, 0.16409,
    0.33920, 0.57085, 0.97383, 0.10109, 0.25996,
    0.87541, 0.29462, 0.72856, 0.55390, 0.56153,
    0.24145, 0.05968, 0.60783, 0.58777, 0.62322
])

# Número de datos
n = len(r)

print(f"Datos utilizados: {r}")

# Hipótesis nula y alterna
H_0 = 1/12  # Hipótesis nula sobre la varianza

# Calcular la media muestral
x_bar = np.mean(r)

# Calcular la varianza muestral
V_r = np.sum((r - x_bar)**2) / (n - 1)
print(f"Varianza muestral: {V_r}")

# Grados de libertad
df = n - 1

# Nivel de significancia
alpha = 0.05

# Límites de la distribución chi-cuadrado
chi2_LS = chi2.ppf(alpha/2, df)       # Límite inferior
chi2_LI = chi2.ppf(1 - alpha/2, df)   # Límite superior

# Límite teórico para la varianza
limite_inferior = chi2_LS / (12 * df)
limite_superior = chi2_LI / (12 * df)

print(f"Límite Inferior (LI): {limite_inferior}")
print(f"Límite Superior (LS): {limite_superior}")

# Comparar la varianza muestral con los límites
if limite_inferior <= V_r <= limite_superior:
    print("✅ No se rechaza la hipótesis nula: La varianza muestral está dentro del rango aceptable.")
else:
    print("❌ Se rechaza la hipótesis nula: La varianza muestral está fuera del rango aceptable.")
