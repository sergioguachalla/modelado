import numpy as np
from collections import Counter
from math import comb
from scipy.stats import chi2

# 1) Copiamos los datos como strings, reemplazando comas por puntos para manejarlos en Python.
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

# Convirtiendo el bloque de texto a una lista de floats:
datos = []
for linea in datos_str.strip().split('\n'):
    for valor in linea.split():
        datos.append(float(valor))

# Verificamos que tengamos 100 datos
assert len(datos) == 100, f"Se esperaban 100 datos, pero se encontraron {len(datos)}."

##############################################################################
# 2) FUNCIONES AUXILIARES PARA LA PRUEBA DE PÓKER
##############################################################################

def clasificar_poker_5dig(num):
    """
    Dado un número en [0,1), obtiene sus 5 primeros dígitos y
    determina la categoría de póker:
      - TD (todos diferentes)
      - 1P (un par)
      - 2P (dos pares)
      - T  (tercia)
      - FH (full house)
      - P  (póker)
      - Q  (quintilla)
    """
    # Convertimos el número a cadena con 5 dígitos decimales.
    # Usamos zfill para forzar que tenga al menos 5 dígitos tras la coma.
    s = f"{num:.5f}"
    
    # Extraemos exactamente los 5 dígitos decimales (ignorando el "0." inicial)
    # s = "0.12345" => s[2:] = "12345"
    digitos = s[2:]
    
    # Contar cuántas veces aparece cada dígito
    conteo = Counter(digitos)
    # Ej: digitos = "11345" => conteo = {'1':2, '3':1, '4':1, '5':1}
    
    # Ordenamos por la frecuencia (p.ej. [2,1,1,1] para un par)
    freqs = sorted(conteo.values(), reverse=True)
    
    if freqs == [1,1,1,1,1]:
        return "TD"   # todos diferentes
    elif freqs == [2,1,1,1]:
        return "1P"   # un par
    elif freqs == [2,2,1]:
        return "2P"   # dos pares
    elif freqs == [3,1,1]:
        return "T"    # tercia
    elif freqs == [3,2]:
        return "FH"   # full house
    elif freqs == [4,1]:
        return "P"    # póker
    elif freqs == [5]:
        return "Q"    # quintilla
    else:
        # No debería suceder en 5 dígitos
        return "???"


##############################################################################
# 3) CLASIFICAMOS TODOS LOS NÚMEROS Y OBTENEMOS LAS FRECUENCIAS OBSERVADAS
##############################################################################

categorias_posibles = ["TD","1P","2P","T","FH","P","Q"]
conteo_categorias = {cat: 0 for cat in categorias_posibles}

for x in datos:
    cat = clasificar_poker_5dig(x)
    conteo_categorias[cat] += 1

# Frecuencias observadas
observadas = np.array([conteo_categorias[cat] for cat in categorias_posibles])

##############################################################################
# 4) FRECUENCIAS ESPERADAS Y ESTADÍSTICO CHI-CUADRADO
##############################################################################

# Probabilidades teóricas (ordenadas en el mismo orden que categorias_posibles)
p_teoricas = {
    "TD": 0.3024,
    "1P": 0.5040,
    "2P": 0.1080,
    "T":  0.0720,
    "FH": 0.0090,
    "P":  0.0045,
    "Q":  0.0001
}

esperadas = np.array([100 * p_teoricas[cat] for cat in categorias_posibles])  # Para n=100

# Chi-cuadrado
chi2_val = np.sum((observadas - esperadas)**2 / esperadas)

# Grados de libertad
# Normalmente, gl = (numero_categorias - 1) = 7 - 1 = 6
# (Asumiendo que no estimamos parámetros adicionales)
gl = len(categorias_posibles) - 1

# p-value
p_val = 1 - chi2.cdf(chi2_val, gl)

##############################################################################
# 5) MOSTRAR RESULTADOS
##############################################################################

print("==========================================")
print("        PRUEBA DE PÓKER (5 dígitos)       ")
print("==========================================")

print("Frecuencias observadas:")
for cat in categorias_posibles:
    print(f"  {cat}: {conteo_categorias[cat]}")
    
print("\nFrecuencias esperadas (n=100):")
for cat in categorias_posibles:
    print(f"  {cat}: {100*p_teoricas[cat]:.4f}")

print("\nEstadístico Chi-cuadrado =", chi2_val)
print("Grados de libertad =", gl)
print("p-value =", p_val)

alpha = 0.05
if p_val < alpha:
    print(f"\nConclusión: Se RECHAZA H0 al nivel de significancia α={alpha}.")
    print("Los datos no se ajustan a la distribución de póker esperada.")
else:
    print(f"\nConclusión: No se rechaza H0 al nivel de significancia α={alpha}.")
    print("No hay evidencia suficiente para negar que sigan la distribución de póker.")
