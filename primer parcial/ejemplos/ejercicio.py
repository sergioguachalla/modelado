'''
Distribución normal (ejercicio 1)

'''
import numpy as np

from math import sqrt

from scipy.stats import norm, chi2




def main():
    score = ["-Inf - 10", "10-15", "15-20", "20-25", "25-30", "30-40", "40 - Inf"] #En este caso infinito es 0
    midpoint = np.array([5,12.5,17.5, 22.5, 27.5, 35, 45])
    observed_freq = np.array([24, 49, 71, 72, 37, 21, 16])
    n = sum(observed_freq)
    medium = np.sum(midpoint * observed_freq) / n
    print(f"n: {n}, frecuencia: {observed_freq}, media: {medium}")

     # Calculate variance (σ²)
    variance = np.sum(observed_freq * (midpoint - medium)**2) / n
    
    # Calculate standard deviation (σ)
    sigma = np.sqrt(variance)

    x = np.array([0, 12, 15, 20, 25, 30, 40, 50])
    z = (x - medium) / sigma

    # Calculate the probabilities using the cumulative distribution function (CDF)
    prob_upper = norm.cdf(z[1:])  # CDF for z[2:7]
    prob_lower = norm.cdf(z[:-1])  # CDF for z[1:6]
    
    # Calculate the frequencies for each range
    expected_freq = (prob_upper - prob_lower) * n
   

# Calcular el estadístico Chi-cuadrado manualmente
    chi2_stat = np.sum((observed_freq - expected_freq) ** 2 / expected_freq)
    
    # Número de intervalos (categorías)
    k = len(observed_freq)

    # Grados de libertad (df)
    df = k - 1

    # Obtener el valor crítico de Chi-cuadrado usando la distribución Chi-cuadrado
    chi2_critical = chi2.ppf(0.95, df)  # Para un nivel de significancia del 5%

    # Calcular el valor p
    p_value = 1 - chi2.cdf(chi2_stat, df)

    # Mostrar resultados
    print(f"Frecuencias observadas: {observed_freq}")
    print(f"Frecuencias esperadas: {expected_freq}")
    print(f"Estadístico Chi-cuadrado calculado: {chi2_stat}")
    print(f"Valor crítico de Chi-cuadrado: {chi2_critical}")
    print(f"Valor p: {p_value}")
    
    # Comparar el estadístico Chi-cuadrado con el valor crítico
    if chi2_stat > chi2_critical:
        print("Rechazamos la hipótesis nula: La distribución observada es significativamente diferente.")
    else:
        print("No rechazamos la hipótesis nula: No hay diferencia significativa.")

if __name__ == '__main__':
    main()