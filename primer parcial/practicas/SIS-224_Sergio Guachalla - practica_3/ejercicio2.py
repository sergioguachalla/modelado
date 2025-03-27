import numpy as np
from scipy.stats import chi2
import math

# Datos observados
observed = np.array([36, 146, 342, 350, 320, 158, 48])
x_values = np.array([0, 1, 2, 3, 4, 5, 6])
n = 1400           # Número total de lanzamientos
m = 6              # Número de monedas (ensayos por experimento)

# Paso 1: Estimación de p
# La media muestral se calcula como: bar(x) = sum(x * n_i) / n
sample_mean = np.sum(x_values * observed) / n
# Para la binomial, la media es: bar(x) = m * p, de donde:
p_est = sample_mean / m

print("Media muestral:", sample_mean)
print("p estimado:", p_est)

# Paso 2: Cálculo de las probabilidades teóricas
# Fórmula: P(x) = (m choose x) * p^x * (1-p)^(m-x)
theoretical_probabilities = np.array([
    math.comb(m, x) * (p_est ** x) * ((1 - p_est) ** (m - x))
    for x in x_values
])

# Cálculo de los valores esperados E_i = n * P(x)
expected = n * theoretical_probabilities

print("\nValores teóricos y esperados:")
for x, prob, exp_val, obs in zip(x_values, theoretical_probabilities, expected, observed):
    print(f"x = {x:>1} | P(x) = {prob:.4f} | E_i = {exp_val:6.2f} | Observado = {obs}")

# Paso 3: Cálculo del estadístico Chi-cuadrado
# Chi-cuadrado: X^2 = sum((n_i - E_i)^2 / E_i)
chi_square_stat = np.sum((observed - expected) ** 2 / expected)
print("\nEstadístico Chi-cuadrado: {:.2f}".format(chi_square_stat))

# Paso 4: Comparación con el valor crítico
# Grados de libertad: k - 1, donde k es el número de categorías (7 en este caso)
df = len(x_values) - 1
chi_square_critical = chi2.ppf(0.95, df)
print("Valor crítico Chi-cuadrado (α=0.05, df={}): {:.2f}".format(df, chi_square_critical))

# Conclusión
if chi_square_stat > chi_square_critical:
    print("\nConclusión: Se rechaza H0. Los datos NO siguen una distribución binomial.")
else:
    print("\nConclusión: No se rechaza H0. Los datos pueden seguir una distribución binomial.")
