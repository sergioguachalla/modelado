import numpy as np
from collections import Counter
from scipy.stats import chi2

# ===== CONFIGURACIÓN: genera o coloca tu lista de números aquí =====
# Puedes reemplazar esta línea por una lista tuya: numeros = [...]
n = 100  # cantidad de números
numeros = np.random.uniform(0, 1, n)  # ejemplo con n números aleatorios U(0,1)

# ===== FUNCIÓN PARA CLASIFICAR CADA NÚMERO POR SU PATRÓN DE DÍGITOS =====
def clasificar(numero):
    digitos = list(str(numero)[2:7].ljust(5, '0'))  # extrae los 5 primeros dígitos decimales
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

# ===== CLASIFICACIÓN =====
clasificaciones = [clasificar(num) for num in numeros]
conteos = Counter(clasificaciones)

# ===== PROBABILIDADES TEÓRICAS DE CADA CATEGORÍA =====
probs = {
    "TD": 0.30240,
    "1P": 0.50400,
    "2P": 0.10800,
    "T": 0.07200,
    "F": 0.00090,
    "POKER": 0.00450,
    "Q": 0.00010
}

# ===== CÁLCULO DE CHI-CUADRADO =====
chi_total = 0
print(f"{'Categoría':<10} {'Obs':<5} {'Esp':<8} {'Chi^2_i':<10}")
for cat, p in probs.items():
    oi = conteos.get(cat, 0)
    ei = p * n
    chi_i = (oi - ei) ** 2 / ei if ei != 0 else 0
    chi_total += chi_i
    print(f"{cat:<10} {oi:<5} {ei:<8.3f} {chi_i:<10.4f}")

# ===== DECISIÓN =====
gl = len(probs) - 1
chi_critico = chi2.ppf(0.95, gl)

print(f"\nChi^2 Total: {chi_total:.4f}")
print(f"Valor crítico (gl={gl}, α=0.05): {chi_critico:.4f}")
if chi_total > chi_critico:
    print("➤ Se rechaza H0: los números no siguen U(0,1)")
else:
    print("➤ No se puede rechazar H0: los números podrían seguir U(0,1)")
