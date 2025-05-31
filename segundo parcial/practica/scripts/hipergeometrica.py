import matplotlib.pyplot as plt
import numpy as np
from math import comb

# Parámetros
N = 25  # población total
K = 10  # número de éxitos (bolas rojas)
n = 5   # tamaño de muestra

# Paso 1: calcular P(x) y F(x)
x_vals = list(range(0, 6))  # posibles valores de bolas rojas (0 a 5)
P_x = [comb(K, x) * comb(N - K, n - x) / comb(N, n) for x in x_vals]
F_x = np.cumsum(P_x)

# Paso 2: imprimir tabla
print("Tabla de P(x) y F(x):")
print("x\tP(x)\t\tF(x)")
for x, p, f in zip(x_vals, P_x, F_x):
    print(f"{x}\t{p:.6f}\t{f:.6f}")

# Paso 3: graficar F(x)
x_graf = [-1] + x_vals + [x_vals[-1] + 1]
F_graf = [0] + list(F_x) + [1.0]

plt.step(x_graf, F_graf, where='post', linestyle='--', marker='o')
plt.title('Función de Distribución Acumulada F(x) - Hipergeométrica')
plt.xlabel('x (bolas rojas extraídas)')
plt.ylabel('F(x)')
plt.grid(True)
plt.xticks(x_vals)
plt.yticks(np.round(np.linspace(0, 1, 11), 2))
plt.show()

# Paso 4: Generador por método de la inversa
def generar_hipergeometrica(R, F_vals=F_x):
    for i, f in enumerate(F_vals):
        if R < f:
            return i
    return len(F_vals) - 1

# Paso 5: Comprobación de valores R
valores_R = [0.02, 0.3, 0.65, 0.94, 0.97]
print("\nComprobación de valores R:")
for R in valores_R:
    x = generar_hipergeometrica(R)
    print(f"Si R = {R}, entonces x = {x}")
