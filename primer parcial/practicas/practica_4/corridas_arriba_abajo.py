import numpy as np
from math import sqrt
from scipy.stats import norm

# Copiamos los datos (ya con punto decimal) en una sola cadena:
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

# Convertimos el bloque de texto a una lista de floats:
datos = []
for linea in datos_str.strip().split('\n'):
    for valor in linea.split():
        datos.append(float(valor))

# Verificamos que tengamos 100 datos
assert len(datos) == 100, f"Se esperaban 100 datos, pero se encontraron {len(datos)}."

##############################################################################
# 1) Calcular las diferencias consecutivas y los signos
##############################################################################
signos = []
for i in range(len(datos)-1):
    d = datos[i+1] - datos[i]
    if d > 0:
        signos.append(1)   # arriba
    elif d < 0:
        signos.append(-1)  # abajo
    else:
        signos.append(0)   # empate

# Opcional: omitimos los empates (signo 0)
signos = [s for s in signos if s != 0]

n_menos = signos.count(-1)
n_mas   = signos.count(1)
n_ast   = len(signos)  # n^* = total de signos (sin empates)

##############################################################################
# 2) Contar el número de corridas (runs) en la secuencia de signos
##############################################################################
def contar_corridas(seq):
    """
    Dada una secuencia de 1/-1 (sin ceros), cuenta cuántas "corridas" hay.
    """
    if not seq:
        return 0
    runs = 1
    for i in range(1, len(seq)):
        if seq[i] != seq[i-1]:
            runs += 1
    return runs

R = contar_corridas(signos)

##############################################################################
# 3) Calcular la media y varianza esperadas para R
##############################################################################
# Fórmulas clásicas:
# E[R] = 1 + 2*n_mas*n_menos / (n_mas + n_menos)
# Var(R) = [2*n_mas*n_menos*(2*n_mas*n_menos - (n_mas+n_menos))] 
#          / [ (n_mas+n_menos)^2 * (n_mas+n_menos - 1) ]
if n_ast < 2:
    # Con menos de 2 signos, la prueba no tiene sentido.
    print("No hay suficientes diferencias para aplicar la prueba de corridas.")
else:
    E_R = 1 + (2*n_mas*n_menos)/(n_mas + n_menos)
    Var_R = (2*n_mas*n_menos*(2*n_mas*n_menos - (n_mas+n_menos))) / \
            ((n_mas+n_menos)**2 * (n_mas+n_menos - 1))

    # 4) Estadístico Z
    Z = (R - E_R)/sqrt(Var_R) if Var_R>0 else 0.0

    # 5) p-value (bicaudal) usando distribución normal
    p_value = 2 * (1 - norm.cdf(abs(Z)))  # bicaudal

    # Mostramos resultados
    print("===========================================")
    print("    PRUEBA DE CORRIDAS (ARRIBA Y ABAJO)    ")
    print("===========================================")
    print(f"N total de datos           = {len(datos)}")
    print(f"N de diferencias analizadas= {n_ast} (se omitieron empates si había)")
    print(f"n_+ = {n_mas}, n_- = {n_menos}")
    print(f"Corridas observadas (R)    = {R}")
    print(f"Valor esperado E[R]        = {E_R:.4f}")
    print(f"Var(R)                     = {Var_R:.4f}")
    print(f"Estadístico Z              = {Z:.4f}")
    print(f"p-value (bicaudal)         = {p_value:.4f}")

    alpha = 0.05
    if p_value < alpha:
        print(f"\nConclusión: Se RECHAZA H0 al nivel α={alpha}.")
        print("  → Hay evidencia de no aleatoriedad en las subidas/bajadas.")
    else:
        print(f"\nConclusión: No se rechaza H0 al nivel α={alpha}.")
        print("  → No hay evidencia suficiente para negar la aleatoriedad en las subidas/bajadas.")
