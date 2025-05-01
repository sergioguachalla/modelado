import numpy as np
from scipy.stats import norm

# Datos extraídos de la imagen
datos = np.array([
    0.80555149, 0.57378059, 0.41554419, 0.91139712, 0.37094581, 0.19791155,
    0.36043851, 0.57221209, 0.57747008, 0.55003321, 0.78236974, 0.16479045,
    0.46925151, 0.80479765, 0.28605795, 0.42872352, 0.68322144, 0.8345696,
    0.46145806, 0.57550346, 0.83323214, 0.21271133, 0.99583636, 0.98586461,
    0.46150812, 0.99243393, 0.57576697, 0.04887623, 0.36231551, 0.02978227,
    0.0444463,  0.70452674, 0.30151397, 0.07822412, 0.14562158, 0.42315536,
    0.92261371, 0.6597978,  0.198173,   0.00778438, 0.17302566, 0.29687015,
    0.02608443, 0.2709028,  0.62229451, 0.24069806, 0.25917165, 0.28549629,
    0.78373774, 0.29883055, 0.07659808, 0.45801943, 0.57443899, 0.37020996,
    0.96076284, 0.56523397, 0.59322245, 0.57447067, 0.11497205, 0.65664531
])

# Parámetros
mu = 0.5                  # Hipótesis nula
n = len(datos)            # Tamaño de la muestra
x_bar = np.mean(datos)    # Media muestral
alpha = 0.05              # Nivel de significancia

# Estadístico de prueba Z
Z_c = (x_bar - mu) * np.sqrt(n) / np.sqrt(1/12)

# Valor crítico Z para una prueba bilateral
Z_critico = norm.ppf(1 - alpha / 2)

# Resultados
print(f"Media muestral (x̄): {x_bar:.5f}")
print(f"Estadístico Z_c: {Z_c:.5f}")
print(f"Intervalo de aceptación: [-{Z_critico:.5f}, {Z_critico:.5f}]")

# Decisión
if abs(Z_c) <= Z_critico:
    print("✅ No se rechaza H₀: La media muestral es estadísticamente compatible con 0.5.")
else:
    print("❌ Se rechaza H₀: La media muestral es significativamente diferente de 0.5.")
