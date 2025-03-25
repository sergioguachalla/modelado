import numpy as np

# Paso 1: Generar números aleatorios uniformemente distribuidos entre 0 y 1
n = 1000  # Número de muestras
data = np.random.rand(n)

# Paso 2: Ordenar los datos de menor a mayor
data_sorted = np.sort(data)

# Paso 3: Calcular la función de distribución empírica F_n(x)
F_n = np.arange(1, n+1) / n  # F_n(x) = i / n, donde i es el índice de x ordenado

# Paso 4: Calcular el estadístico D_n
D_n = np.max(np.abs(F_n - data_sorted))  # D_n = max |F_n(x) - x_i|

# Paso 5: Calcular el valor crítico d_n (para una distribución uniforme)
alpha = 0.05  # Nivel de significancia
d_n = np.sqrt(-0.5 * np.log(alpha / 2) / n)  # Fórmula para el valor crítico d_n

# Paso 6: Regla de decisión
print(f"Estadístico D_n: {D_n}")
print(f"Valor crítico d_n: {d_n}")

if D_n > d_n:
    print("Rechazamos H0: Los datos no siguen una distribución uniforme.")
else:
    print("No rechazamos H0: Los datos podrían seguir una distribución uniforme.")
