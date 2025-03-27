import numpy as np
from scipy.stats import chi2

# Datos del ejercicio
intervalos = [(10, 15), (15, 20), (20, 25), (25, 30), (30, 35), (35, 40), (40, 45)]
frecuencias_observadas = [30, 25, 22, 18, 19, 12, 8]
marcas_clase = [12.5, 17.5, 22.5, 27.5, 32.5, 37.5, 47.5]
n_total = sum(frecuencias_observadas)

# 1. Cálculo de la media muestral
media_muestral = sum(ni * xi for ni, xi in zip(frecuencias_observadas, marcas_clase)) / n_total

# 2. Estimación del parámetro lambda
lmbda = 1 / media_muestral

# 3. Cálculo de probabilidades y valores esperados
probabilidades = []
valores_esperados = []
for a, b in intervalos:
    P = np.exp(-lmbda * a) - np.exp(-lmbda * b)
    probabilidades.append(P)
    valores_esperados.append(n_total * P)

# 4. Cálculo del estadístico Chi-cuadrado
chi_cuadrado = sum((ni - ei) ** 2 / ei for ni, ei in zip(frecuencias_observadas, valores_esperados))

# 5. Comparación con X^2 crítico
grados_libertad = len(intervalos) - 1
chi_critico = chi2.ppf(0.95, grados_libertad)

# 6. Impresión de resultados
print(f"Media muestral: {media_muestral:.4f}")
print(f"Lambda estimado: {lmbda:.5f}")
print("\nIntervalo | Probabilidad | Valor Esperado | Observado")
for (a, b), P, ei, ni in zip(intervalos, probabilidades, valores_esperados, frecuencias_observadas):
    print(f"{a}-{b} | {P:.3f} | {ei:.2f} | {ni}")
print(f"\nChi-cuadrado calculado: {chi_cuadrado:.2f}")
print(f"Chi-cuadrado crítico (α=0.05, df={grados_libertad}): {chi_critico:.2f}")

# 7. Veredicto
if chi_cuadrado > chi_critico:
    print("\n🔴 Se rechaza H0: Los datos NO siguen una distribución exponencial.")
else:
    print("\n🟢 No se rechaza H0: Los datos pueden seguir una distribución exponencial.")
