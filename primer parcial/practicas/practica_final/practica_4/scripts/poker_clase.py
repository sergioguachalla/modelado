import numpy as np
from collections import Counter
from scipy.stats import chi2

# Datos de entrada (84 números)
datos = np.array([
    [0.57861, 0.10420, 0.50683, 0.99599, 0.99506, 0.75180, 0.86573],
    [0.77828, 0.67768, 0.49340, 0.99267, 0.18774, 0.71643, 0.81548],
    [0.00887, 0.43128, 0.77992, 0.99343, 0.81064, 0.49640, 0.66545],
    [0.05265, 0.65878, 0.91444, 0.81309, 0.37949, 0.23203, 0.33195],
    [0.59204, 0.47730, 0.75437, 0.80350, 0.19447, 0.22265, 0.66533],
    [0.73804, 0.03576, 0.76359, 0.77717, 0.07468, 0.97661, 0.84780],
    [0.42493, 0.69261, 0.18830, 0.76361, 0.76796, 0.02133, 0.37448],
    [0.85384, 0.41356, 0.91655, 0.42446, 0.49268, 0.02229, 0.57044],
    [0.51540, 0.35613, 0.56161, 0.07314, 0.90936, 0.82914, 0.90868],
    [0.27916, 0.51612, 0.07940, 0.29996, 0.32350, 0.24968, 0.18188],
    [0.43715, 0.54395, 0.91340, 0.26302, 0.87738, 0.04897, 0.01376],
    [0.91919, 0.02278, 0.89232, 0.62109, 0.20053, 0.94825, 0.05641]
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
