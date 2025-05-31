import math
import random

# ------------------------------------------
# 1. Mostrar la resolución paso a paso
# ------------------------------------------
def mostrar_resolucion():
    print("RESOLUCIÓN DEL EJERCICIO:\n")

    print("1. f(x) por tramos:")
    print("   f(x) = x/2,                 si 0 ≤ x ≤ 1")
    print("   f(x) = 1,                   si 1 < x ≤ 2")
    print("   f(x) = -x/2 + 3/2,          si 2 < x ≤ 3\n")

    print("2. Pesos (área bajo cada tramo):")
    print("   w₁ = 1/3,   w₂ = 1/2,   w₃ = 1/4\n")

    print("3. f(x) normalizada (multiplicando por wᵢ):")
    print("   f₁(x) = 2x/3               → en [0, 1]")
    print("   f₂(x) = 1/2                → en [1, 2]")
    print("   f₃(x) = -x/2 + 3/2 * 1/4 = -x/8 + 3/8   → en [2, 3]\n")

    print("4. F(x) acumulada por tramos:")
    print("   F₁(x) = (2/3) ∫x dx = x²/3             → 0 ≤ x ≤ 1")
    print("   F₂(x) = w₁ + ∫(1/2)dx = 1/3 + (x - 1)/2 → 1 < x ≤ 2")
    print("   F₃(x) = w₁ + w₂ + ∫(-x/8 + 3/8)dx       → 2 < x ≤ 3")
    print("        = 1/3 + 1/2 + [-x²/16 + 3x/8] - [valor en x=2]\n")

    print("5. GENERADORES:\n")
    print("   X₁ = √(3R₁),                               0 ≤ R₁ < 1/3")
    print("   X₂ = 2R₂ - 2/3 + 1,                        1/3 ≤ R₂ < 5/6")
    print("   X₃ = raíz positiva de: -x²/16 + 3x/8 - C = R₃,   R₃ ≥ 5/6")
    print("       (donde C = constante de integración acumulada hasta x = 2)\n")

# ------------------------------------------
# 2. Calcular x según R usando la inversa
# ------------------------------------------
def calcular_x(r):
    if 0 <= r < 1/3:
        # F₁(x) = x² / 3 → x = √(3r)
        x = math.sqrt(3 * r)
        formula = "X₁ = √(3R₁)"
        tramo = "0 ≤ R₁ < 1/3"

    elif 1/3 <= r < 5/6:
        # F₂(x) = 1/3 + (x - 1)/2 → x = 2r - 2/3 + 1 = 2r + 1/3
        x = 2 * r + 1/3
        formula = "X₂ = 2R₂ + 1/3"
        tramo = "1/3 ≤ R₂ < 5/6"

    elif 5/6 <= r <= 1:
        # F₃(x) = -x²/16 + 3x/8 - C = r → cuadrática: -x²/16 + 3x/8 - (constante) - r = 0
        C = 1/3 + 1/2  # área acumulada hasta x = 2
        a = -1/16
        b = 3/8
        c = -(C + r)
        discriminante = b**2 - 4*a*c

        if discriminante < 0:
            x = None
        else:
            x1 = (-b + math.sqrt(discriminante)) / (2*a)
            x2 = (-b - math.sqrt(discriminante)) / (2*a)
            x = x1 if 2 <= x1 <= 3 else x2  # elegir dentro del intervalo

        formula = "X₃ = raíz de -x²/16 + 3x/8 - 5/6 = R₃"
        tramo = "R₃ ≥ 5/6"

    else:
        x = None
        formula = "Fuera de dominio"
        tramo = "-"

    return r, x, formula, tramo

# ------------------------------------------
# 3. Generar muestras aleatorias
# ------------------------------------------
def generar_muestras(n=6):
    print("6. VALORES GENERADOS:\n")
    for i in range(1, n+1):
        r = round(random.uniform(0, 1), 4)
        r, x, formula, tramo = calcular_x(r)
        print(f"{i}) r = {r}  →  x = {round(x, 4) if x is not None else 'Error'}")
        print(f"   Fórmula usada: {formula}")
        print(f"   Rango: {tramo}\n")

# ------------------------------------------
# 4. Ejecutar todo
# ------------------------------------------
if __name__ == "__main__":
    mostrar_resolucion()
    generar_muestras()
