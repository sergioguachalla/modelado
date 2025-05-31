import math
import random

# ------------------------------------------
# 1. f(x) por tramos original (NO normalizada)
# ------------------------------------------
def f_original(x):
    if 0 <= x <= 2:
        return -x/8 + 1/2
    elif 2 < x <= 4:
        return 1/4
    elif 4 < x <= 6:
        return -x/8 + 3/4
    else:
        return 0

# ------------------------------------------
# 2. f(x) normalizada (dividiendo todo entre 1.5)
# ------------------------------------------
def f(x):
    if 0 <= x <= 2:
        return -x/12 + 1/3
    elif 2 < x <= 4:
        return 1/6
    elif 4 < x <= 6:
        return x/12 - 1/2
    else:
        return 0

# ------------------------------------------
# 3. F(x): Función de distribución acumulada
# ------------------------------------------
def F(x):
    if 0 <= x <= 2:
        return (2 * x) / 3 - (x ** 2) / 12
    elif 2 < x <= 4:
        return 1/2
    elif 4 < x <= 6:
        return -x ** 2 / 4 + 3 * x - 8
    elif x < 0:
        return 0
    else:
        return 1

# ------------------------------------------
# 4. Mostrar procedimiento y generadores
# ------------------------------------------
def mostrar_resolucion():
    print("RESOLUCIÓN DEL EJERCICIO:\n")

    print("1. f(x) original por tramos:")
    print("   f(x) = -x/8 + 1/2,      si 0 ≤ x ≤ 2")
    print("   f(x) = 1/4,             si 2 < x ≤ 4")
    print("   f(x) = -x/8 + 3/4,      si 4 < x ≤ 6\n")

    print("2. Área total = 0.5 + 0.5 + 0.5 = 1.5 → Normalizamos dividiendo entre 1.5:\n")

    print("3. f(x) normalizada:")
    print("   f(x) = -x/12 + 1/3,     si 0 ≤ x ≤ 2")
    print("   f(x) = 1/6,             si 2 < x ≤ 4")
    print("   f(x) = x/12 - 1/2,      si 4 < x ≤ 6\n")

    print("4. F(x) acumulada:")
    print("   F(x) = 2x/3 - x²/12,              si 0 ≤ x ≤ 2")
    print("   F(x) = 1/2,                       si 2 < x ≤ 4")
    print("   F(x) = -x²/4 + 3x - 8,            si 4 < x ≤ 6\n")

    print("5. GENERADORES (resolviendo F(x) = R):\n")
    print("   X₁ = 4 - √(4/9 - R₁/3),           0 ≤ R₁ < 1/2")
    print("   X₂ = √(4R₂ + 4),                  1/2 ≤ R₂ < 5/6")
    print("   X₃ = 6 - 2√(1 - R₃),              R₃ ≥ 5/6\n")

# ------------------------------------------
# 5. Generar valor a partir de r
# ------------------------------------------
def calcular_x(r):
    if 0 <= r < 1/2:
        x = 4 - math.sqrt(4/9 - r/3)
        formula = "X₁ = 4 - √(4/9 - R₁/3)"
        tramo = "0 ≤ R₁ < 1/2"
    elif 1/2 <= r < 5/6:
        x = math.sqrt(4*r + 4)
        formula = "X₂ = √(4R₂ + 4)"
        tramo = "1/2 ≤ R₂ < 5/6"
    elif 5/6 <= r <= 1:
        x = 6 - 2 * math.sqrt(1 - r)
        formula = "X₃ = 6 - 2√(1 - R₃)"
        tramo = "R₃ ≥ 5/6"
    else:
        x = None
        formula = "Fuera de dominio"
        tramo = "-"
    return r, x, formula, tramo

# ------------------------------------------
# 6. Generar muestras aleatorias
# ------------------------------------------
def generar_muestras(n=6):
    print("6. VALORES GENERADOS:\n")
    for i in range(1, n+1):
        r = round(random.uniform(0, 1), 4)
        r, x, formula, tramo = calcular_x(r)
        print(f"{i}) r = {r}  →  x = {round(x, 4)}")
        print(f"   Fórmula usada: {formula}")
        print(f"   Rango: {tramo}\n")

# ------------------------------------------
# 7. Ejecutar todo
# ------------------------------------------
if __name__ == "__main__":
    mostrar_resolucion()
    generar_muestras()
