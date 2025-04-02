import numpy as np
from scipy.stats import chi2

# Datos originales
datos_str = """
0.86748 0.39731 0.27452 0.01569 0.96505 0.37446
0.98332 0.30716 0.31265 0.23300 0.04068 0.41391
0.38715 0.37894 0.18494 0.77374 0.18088 0.51509
0.46433 0.55130 0.69458 0.02231 0.86824 0.88297
0.98759 0.81414 0.98338 0.46493 0.30734 0.87109
0.65812 0.59761 0.08390 0.55088 0.39372 0.70502
0.83906 0.61277 0.36415 0.25156 0.34907 0.49806
0.65261 0.47923 0.29507 0.75287 0.68987 0.66905
0.16118 0.25195 0.85003 0.18613 0.81657 0.48364
0.17370 0.16930 0.69620 0.15393 0.77326 0.22930
0.00171 0.43160 0.01284 0.49030 0.75881 0.47318
"""

# Convertir los datos a arreglo de floats
datos = np.array([[float(num) for num in line.split()] for line in datos_str.strip().split('\n')])
valores = datos.flatten()

# Parámetros de la prueba
N = len(valores)
n = 5  # número de segmentos
gl = n - 1  # grados de libertad
esperado = N / n  # frecuencia esperada por segmento
alpha = 0.14  # nivel de significancia

# Frecuencias observadas en los segmentos
frecuencias_observadas, _ = np.histogram(valores, bins=n, range=(0, 1))

# Estadístico chi-cuadrado
chi_cuadrado = np.sum((frecuencias_observadas - esperado) ** 2 / esperado)

# Valor crítico usando scipy
valor_critico = chi2.ppf(1 - alpha, gl)

# Mostrar resultados
print("=== Prueba de Frecuencias ===")
print(f"H0: x ~ U(0,1)")
print(f"Nivel de significancia α = {alpha}")
print(f"n = {n} segmentos | N = {N} datos")
print(f"Frecuencia esperada por segmento: {esperado:.2f}")
print(f"Grados de libertad: {gl}")
print(f"Valor crítico chi^2 (1 - α): {valor_critico:.4f}")
print(f"Estadístico chi-cuadrado calculado: {chi_cuadrado:.4f}\n")

# Mostrar tabla de segmentos
for i in range(n):
    lim_inf = i / n
    lim_sup = (i + 1) / n
    print(f"Segmento [{lim_inf:.1f}, {lim_sup:.1f}): Observado = {frecuencias_observadas[i]}, Esperado = {esperado:.2f}")

# Conclusión
if chi_cuadrado > valor_critico:
    print("\nSe rechaza H0: los datos NO siguen una distribución uniforme.")
else:
    print("\nNo se rechaza H0: los datos podrían provenir de una distribución uniforme.")
