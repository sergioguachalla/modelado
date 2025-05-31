import matplotlib.pyplot as plt
import numpy as np
from math import comb

# Parámetros del experimento binomial
n = 10
p = 1/4
q = 1 - p

# Paso 1: Calcular P(x) y F(x)
valores_x = list(range(n + 1))
P_x = [comb(n, x) * (p ** x) * (q ** (n - x)) for x in valores_x]
F_x = np.cumsum(P_x)

# Paso 2: Imprimir tabla
print("Tabla de P(x) y F(x):")
print("x\tP(x)\t\tF(x)")
for x, p_val, f_val in zip(valores_x, P_x, F_x):
    print(f"{x}\t{p_val:.6f}\t{f_val:.6f}")

# Paso 3: Graficar F(x)
x_graf = [-1] + valores_x + [n+1]
F_graf = [0] + list(F_x) + [1.0]

plt.step(x_graf, F_graf, where='post', linestyle='--', marker='o')
plt.title('Función de Distribución Acumulada F(x) - Binomial(n=10, p=0.25)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True)
plt.xticks(valores_x)
plt.yticks(np.round(np.linspace(0, 1, 11), 2))
plt.show()

# Paso 4: Generador inverso
def generar_valor_discreto_binomial(R, F_vals=F_x):
    for i, f in enumerate(F_vals):
        if R < f:
            return i
    return len(F_vals) - 1  # Por si R ≈ 1

# Comprobación de algunos valores R
valores_R = [0.05, 0.3, 0.72, 0.99]
print("\nComprobación de valores R:")
for R in valores_R:
    x = generar_valor_discreto_binomial(R)
    print(f"Si R = {R}, entonces x = {x}")
