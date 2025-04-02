import numpy as np

# ---------- CONFIGURACIÓN ----------
n_datos = 100       # número de valores aleatorios
n_segmentos = 5     # número de segmentos (intervalos)
alpha = 0.05        # nivel de significancia

# ---------- GENERAR DATOS ----------
valores = np.random.uniform(0, 1, n_datos)

# ---------- PRUEBA DE FRECUENCIAS ----------
esperado = n_datos / n_segmentos
frecuencias_observadas, _ = np.histogram(valores, bins=n_segmentos, range=(0, 1))
chi_cuadrado = np.sum((frecuencias_observadas - esperado) ** 2 / esperado)

# Valor crítico para gl = n - 1
from scipy.stats import chi2
gl = n_segmentos - 1
valor_critico = chi2.ppf(1 - alpha, gl)

# ---------- RESULTADOS ----------
print("=== Prueba de Frecuencias (valores aleatorios) ===")
print(f"Número de datos: {n_datos}")
print(f"Número de segmentos: {n_segmentos}")
print(f"Frecuencia esperada por segmento: {esperado:.2f}")
print(f"Nivel de significancia: {alpha}")
print(f"Valor crítico (gl = {gl}): {valor_critico:.4f}")
print(f"Estadístico chi-cuadrado: {chi_cuadrado:.4f}\n")

for i in range(n_segmentos):
    lim_inf = i / n_segmentos
    lim_sup = (i + 1) / n_segmentos
    print(f"Segmento [{lim_inf:.1f}, {lim_sup:.1f}): Observado = {frecuencias_observadas[i]}, Esperado = {esperado}")

# ---------- CONCLUSIÓN ----------
if chi_cuadrado > valor_critico:
    print("\nSe rechaza H0: los datos NO siguen una distribución uniforme.")
else:
    print("\nNo se rechaza H0: los datos podrían provenir de una distribución uniforme.")
