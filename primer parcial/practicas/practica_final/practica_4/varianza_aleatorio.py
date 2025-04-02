import numpy as np
from scipy.stats import chi2

# Definir el tamaño de la muestra
n = int(input("Ingrese el tamaño de la muestra (n): "))  # Tamaño de la muestra

# Generar n números aleatorios entre un rango definido (por ejemplo, entre 0 y 10)
r = np.random.uniform(0, 10, n)  # Genera números aleatorios entre 0 y 10
print(f"Datos generados aleatoriamente: {r}")

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
chi2_LS = chi2.ppf(alpha/2, df)  # Límite inferior
chi2_LI = chi2.ppf(1 - alpha/2, df)  # Límite superior

# Límite teórico para la varianza
limite_inferior = chi2_LS / (12 * (n - 1))
limite_superior = chi2_LI / (12 * (n - 1))

print(f"Limite Inferior (LI): {limite_inferior}")
print(f"Limite Superior (LS): {limite_superior}")

# Comparar la varianza muestral con los límites
if limite_inferior <= V_r <= limite_superior:
    print("No se rechaza la hipótesis nula: La varianza muestral está dentro del rango aceptable.")
else:
    print("Se rechaza la hipótesis nula: La varianza muestral está fuera del rango aceptable.")
