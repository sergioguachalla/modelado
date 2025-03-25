import numpy as np
from scipy.stats import chi2

# Parámetros
N = 1000  # Número de elementos en la secuencia
n = 10    # Número de intervalos
alpha = 0.05  # Nivel de significancia

# Paso 1: Generar números aleatorios uniformemente distribuidos
data = np.random.rand(N)

# Paso 2: Dividir el rango [0, 1] en n intervalos
intervalos = np.linspace(0, 1, n+1)

# Paso 3: Contar cuántos números caen en cada intervalo
counts, _ = np.histogram(data, bins=intervalos)

# Paso 4: Calcular las frecuencias esperadas (en una distribución uniforme)
expected = np.full(n, N / n)

# Paso 5: Calcular el estadístico chi-cuadrado
chi_squared = np.sum((counts - expected) ** 2 / expected)

# Paso 6: Calcular el valor crítico de chi-cuadrado para n-1 grados de libertad
chi_critical = chi2.ppf(1 - alpha, df=n-1)

# Paso 7: Comparar y tomar decisión
print(f"Estadístico chi-cuadrado: {chi_squared}")
print(f"Valor crítico: {chi_critical}")

if chi_squared > chi_critical:
    print("Rechazamos H0: La secuencia no es uniforme.")
else:
    print("No rechazamos H0: La secuencia parece uniforme.")

# Mostrar la distribución observada
print(f"Frecuencias observadas: {counts}")
print(f"Frecuencias esperadas: {expected}")
