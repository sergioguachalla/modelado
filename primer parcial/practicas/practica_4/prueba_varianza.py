import numpy as np
from scipy.stats import chi2

# Datos (los mismos 100 números usados anteriormente)
datos_str = """
0.22007 0.91196 0.15321 0.42385 0.00394 0.62413 0.55015 0.44955 0.44568 0.77015
0.89714 0.67470 0.91306 0.38377 0.52926 0.62236 0.30655 0.99578 0.27121 0.64964
0.20337 0.40283 0.34349 0.78248 0.29464 0.49713 0.72596 0.19324 0.97873 0.95863
0.20679 0.95380 0.88229 0.98442 0.42053 0.24912 0.85840 0.93743 0.41339 0.23150
0.16135 0.65483 0.16007 0.11929 0.25120 0.49779 0.64172 0.01760 0.48477 0.14075
0.52977 0.63966 0.43317 0.57741 0.38171 0.25249 0.27820 0.35766 0.08874 0.11372
0.28190 0.46587 0.35783 0.83087 0.57543 0.85099 0.80861 0.20435 0.16132 0.38590
0.72478 0.71794 0.63607 0.97218 0.81961 0.23667 0.36566 0.08556 0.86878 0.58924
0.11386 0.62900 0.61609 0.37641 0.97121 0.71532 0.00482 0.96702 0.95287 0.30823
0.33887 0.65388 0.08570 0.33943 0.03985 0.00514 0.05950 0.07925 0.54867 0.28632
"""

# Convertir los datos a una lista de floats:
datos = []
for linea in datos_str.strip().split('\n'):
    for valor in linea.split():
        datos.append(float(valor))

# Verificamos que tengamos 100 datos
n = len(datos)
assert n == 100, f"Se esperaban 100 datos, pero se encontraron {n}."

# Calcular la varianza muestral (usamos ddof=1 para la estimación insesgada)
s2 = np.var(datos, ddof=1)

# Varianza teórica para U(0,1) es 1/12
sigma2_0 = 1/12

# Estadístico de contraste:
chi2_stat = (n - 1) * s2 / sigma2_0

# Grados de libertad:
gl = n - 1

# Nivel de significación
alpha = 0.05

# Cuantiles de la distribución chi-cuadrado:
chi2_lower = chi2.ppf(alpha/2, gl)
chi2_upper = chi2.ppf(1 - alpha/2, gl)

# p-value (prueba bicaudal)
# p-value es la probabilidad de obtener un valor más extremo que el estadístico
if chi2_stat < chi2_lower:
    p_value = 2 * chi2.cdf(chi2_stat, gl)
elif chi2_stat > chi2_upper:
    p_value = 2 * (1 - chi2.cdf(chi2_stat, gl))
else:
    # Si el estadístico está entre los cuantiles críticos, el p-value será mayor que alpha
    p_value = 1 - alpha

print("===========================================")
print("    PRUEBA DE LA VARIANZA (U(0,1))         ")
print("===========================================")
print(f"Número de datos (n): {n}")
print(f"Varianza muestral (s²): {s2:.6f}")
print(f"Varianza teórica σ²₀: {sigma2_0:.6f}")
print(f"Estadístico χ²: {chi2_stat:.4f}")
print(f"Grados de libertad: {gl}")
print(f"Cuantil inferior (α/2): {chi2_lower:.4f}")
print(f"Cuantil superior (1-α/2): {chi2_upper:.4f}")
print(f"p-value: {p_value:.4f}")

if chi2_stat < chi2_lower or chi2_stat > chi2_upper:
    print(f"\nConclusión: Se RECHAZA H₀ al nivel de significancia α={alpha}.")
    print("La varianza de los datos difiere de 1/12.")
else:
    print(f"\nConclusión: No se rechaza H₀ al nivel de significancia α={alpha}.")
    print("No hay evidencia suficiente para decir que la varianza difiere de 1/12.")
