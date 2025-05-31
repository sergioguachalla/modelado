import numpy as np
import matplotlib.pyplot as plt
from math import exp, factorial

# Parámetros de la distribución de Poisson
lambd = 5
x_vals = list(range(16))  # x de 0 a 15

# Paso 1: Calcular P(x) y F(x)
P_x = [(exp(-lambd) * lambd**x) / factorial(x) for x in x_vals]
F_x = np.cumsum(P_x)

# Paso 2: Imprimir tabla
print("Tabla de P(x) y F(x):")
print("x\tP(x)\t\tF(x)")
for x, p, f in zip(x_vals, P_x, F_x):
    print(f"{x}\t{p:.6f}\t{f:.6f}")

# Paso 3: Graficar F(x)
x_graf = [-1] + x_vals + [max(x_vals)+1]
F_graf = [0] + list(F_x) + [1.0]

plt.step(x_graf, F_graf, where='post', linestyle='--', marker='o')
plt.title('Distribución Acumulada F(x) - Poisson(λ=5)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True)
plt.xticks(range(0, 16))
plt.yticks(np.round(np.linspace(0, 1, 11), 2))
plt.show()

# Paso 4: Método de la inversa para generar valores
def generar_valor_poisson_inverso(R, F_vals=F_x):
    for i, f in enumerate(F_vals):
        if R < f:
            return i
    return len(F_vals) - 1

# Paso 5: Comprobación de valores R
valores_R = [0.006, 0.25, 0.52, 0.985]
print("\nComprobación de valores R:")
for R in valores_R:
    x = generar_valor_poisson_inverso(R)
    print(f"Si R = {R}, entonces x = {x}")
