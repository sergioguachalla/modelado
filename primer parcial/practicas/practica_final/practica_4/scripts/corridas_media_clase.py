import numpy as np

# ---------- DATOS ----------
datos_str = """
0.60799 0.64321 0.25740 0.90224 0.74812 0.47996 0.35863 0.75790 0.84894
0.00869 0.26415 0.98708 0.08103 0.01446 0.50198 0.42302 0.59192 0.20433
0.16715 0.74372 0.63674 0.46023 0.81686 0.88819 0.14834 0.86696 0.02872
0.15214 0.40297 0.57138 0.69443 0.71004 0.64070 0.01106 0.32332 0.32905
0.32693 0.50517 0.59499 0.00119 0.72162 0.18144 0.32300 0.11043 0.11549
0.05380 0.87939 0.93001 0.14612 0.20553 0.26105 0.74055 0.35157 0.02482
0.43303 0.93784 0.87000 0.70457 0.56869 0.88889 0.91355 0.66990 0.64143
0.12980 0.99859 0.13118 0.13361 0.37336 0.04285 0.56304 0.42526 0.40534
0.04255 0.33511 0.44856 0.94541 0.79972 0.81088 0.14088 0.07312 0.95719
0.86010 0.87021 0.91532 0.51084 0.31955 0.10994 0.78898 0.96135 0.27321
0.34401 0.57978 0.92887 0.41412 0.05088 0.93111 0.58407 0.83300 0.44500
"""

# ---------- PREPARACIÓN ----------
datos = np.array([float(x) for x in datos_str.strip().split()])
n = len(datos)

# Convertir a binario según si el valor es mayor a 0.5
binarios = np.array([1 if x > 0.5 else 0 for x in datos])
n1 = np.sum(binarios)
n0 = n - n1

# ---------- CONTAR CORRIDAS ----------
corridas = 1
for i in range(1, n):
    if binarios[i] != binarios[i - 1]:
        corridas += 1

# ---------- ESTADÍSTICOS ----------
mu_co = (2 * n0 * n1) / n + 0.5
var_co = (2 * n0 * n1 * (2 * n0 * n1 - n)) / (n**2 * (n - 1))
sigma_co = np.sqrt(var_co)
Zc = (corridas - mu_co) / sigma_co
Z_critico = 1.96  # para α = 0.05

# ---------- RESULTADOS ----------
print("=== Prueba de Corridas respecto a la Media ===")
print(f"Cantidad de datos: {n}")
print(f"Cantidad de 1s (> 0.5): {n1}")
print(f"Cantidad de 0s (<= 0.5): {n0}")
print(f"Corridas observadas: {corridas}")
print(f"Media esperada (μ_co): {mu_co:.4f}")
print(f"Desviación estándar (σ_co): {sigma_co:.4f}")
print(f"Z calculado (Zc): {Zc:.4f}")
print(f"Z crítico (α = 0.05): ±{Z_critico}")

# ---------- CONCLUSIÓN ----------
if abs(Zc) > Z_critico:
    print("\n❌ Se rechaza H₀: los datos NO son independientes respecto a la media.")
else:
    print("\n✅ No se rechaza H₀: los datos podrían ser independientes respecto a la media.")
