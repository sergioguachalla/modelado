import numpy as np
import math

# Lista de valores dados (copiados del mensaje)
valores = np.array([
    0.00778, 0.02608, 0.04445, 0.04888, 0.07660, 0.07822, 0.11497, 0.14562,
    0.17303, 0.19817, 0.21271, 0.24070, 0.25917, 0.27090, 0.28606, 0.29883,
    0.30151, 0.36044, 0.36232, 0.37095, 0.41554, 0.42872, 0.45802, 0.46146,
    0.46151, 0.46925, 0.55003, 0.56523, 0.57221, 0.57378, 0.57444, 0.57447,
    0.57550, 0.57577, 0.57747, 0.59322, 0.62229, 0.65980, 0.68322, 0.70453,
    0.78237, 0.78374, 0.80480, 0.80555, 0.83323, 0.91140, 0.92261, 0.96076,
    0.99243, 0.99584
])

# Paso 1: Ordenar los datos
valores_ordenados = np.sort(valores)

# Paso 2: Calcular F_n(x) = i/n
n = len(valores_ordenados)
Fn = np.arange(1, n + 1) / n

# Paso 3: Calcular |F_n(x_i) - x_i|
diferencias = np.abs(Fn - valores_ordenados)

# Paso 4: Calcular Dn
Dn = np.max(diferencias)

# Paso 5: Calcular el valor crítico d_n para α dado (por ejemplo α = 0.05)
alpha = 0.05
dn_critico = np.sqrt(-np.log(alpha / 2) / (2 * n))

# Mostrar resultados
print("=== Prueba de Kolmogorov-Smirnov ===")
print(f"N = {n}")
print(f"Nivel de significancia α = {alpha}")
print(f"Estadístico Dn = {Dn:.5f}")
print(f"Valor crítico d_n = {dn_critico:.5f}")

# Conclusión
if Dn < dn_critico:
    print("\nNo se rechaza H0: los datos podrían provenir de una distribución uniforme U(0,1).")
else:
    print("\nSe rechaza H0: los datos NO provienen de una distribución uniforme.")
