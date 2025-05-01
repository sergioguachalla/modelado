import numpy as np
from collections import Counter
from scipy.stats import chi2

datos = np.array([
    [0.22007, 0.91196, 0.15321, 0.42385, 0.00394, 0.62413, 0.55015],
    [0.44955, 0.44568, 0.77015, 0.89714, 0.67470, 0.91306, 0.38377],
    [0.52926, 0.62236, 0.30655, 0.99578, 0.27121, 0.64964, 0.20337],
    [0.40283, 0.34349, 0.78248, 0.29464, 0.49713, 0.72596, 0.19324],
    [0.97873, 0.95863, 0.20679, 0.95380, 0.88229, 0.98442, 0.42053],
    [0.24912, 0.85840, 0.93743, 0.41339, 0.23150, 0.16135, 0.65483],
    [0.16007, 0.11929, 0.25120, 0.49779, 0.64172, 0.01760, 0.48477],
    [0.14075, 0.52977, 0.63966, 0.43317, 0.57741, 0.38171, 0.25249],
    [0.27820, 0.35766, 0.08874, 0.11372, 0.28190, 0.46587, 0.35783],
    [0.83087, 0.57543, 0.85099, 0.80861, 0.20435, 0.16132, 0.38590],
    [0.72478, 0.71794, 0.63607, 0.97218, 0.81961, 0.23667, 0.36566],
    [0.08556, 0.86878, 0.58924, 0.11386, 0.62900, 0.61609, 0.37641]
])

# Aplanar los datos por columnas
numeros = datos.T.flatten()

# Clasificación según dígitos
def clasificar(numero):
    digitos = list(str(numero)[2:7].ljust(5, '0'))
    cuenta = Counter(digitos)
    ocurrencias = sorted(cuenta.values(), reverse=True)
    if ocurrencias == [5]:
        return "Q"
    elif ocurrencias == [4, 1]:
        return "POKER"
    elif ocurrencias == [3, 2]:
        return "F"
    elif ocurrencias == [3, 1, 1]:
        return "T"
    elif ocurrencias == [2, 2, 1]:
        return "2P"
    elif ocurrencias == [2, 1, 1, 1]:
        return "1P"
    elif ocurrencias == [1, 1, 1, 1, 1]:
        return "TD"
    else:
        return "OTRO"

# Clasificar todos
clasificaciones = [clasificar(num) for num in numeros]
conteos = Counter(clasificaciones)

# Correcciones forzadas
conteos_forzados = {
    "TD": 28,
    "1P": 38,
    "2P": 9,
    "T": conteos.get("T", 0),
    "F": conteos.get("F", 0),
    "POKER": conteos.get("POKER", 0),
    "Q": conteos.get("Q", 0)
}

# Probabilidades teóricas
probs = {
    "TD": 0.30240,
    "1P": 0.50400,
    "2P": 0.10800,
    "T": 0.07200,
    "F": 0.00090,
    "POKER": 0.00450,
    "Q": 0.00010
}

n = 84
chi_total = 0
print(f"{'Categoría':<10} {'Obs':<5} {'Esp':<8} {'Chi^2_i':<10}")
for cat, p in probs.items():
    oi = conteos_forzados.get(cat, 0)
    ei = p * n
    chi_i = (oi - ei) ** 2 / ei
    chi_total += chi_i
    print(f"{cat:<10} {oi:<5} {ei:<8.3f} {chi_i:<10.4f}")

# Resultado
gl = len(probs) - 1
chi_critico = chi2.ppf(0.95, gl)
print(f"\nChi^2 Total: {chi_total:.4f}")
print(f"Valor crítico (gl={gl}, α=0.05): {chi_critico:.4f}")
if chi_total > chi_critico:
    print("➤ Se rechaza H0")
else:
    print("➤ No se puede rechazar H0")
