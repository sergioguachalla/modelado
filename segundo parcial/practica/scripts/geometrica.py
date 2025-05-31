import numpy as np
import matplotlib.pyplot as plt

# Parámetro de éxito
p = 0.3
q = 1 - p

# Valores de x: número de intentos hasta el primer éxito
x_vals = list(range(1, 13))

# Paso 1: Calcular P(x) y F(x)
P_x = [(q**(x-1)) * p for x in x_vals]
F_x = np.cumsum(P_x)

# Paso 2: Imprimir tabla
print("Tabla de P(x) y F(x):")
print("x\tP(x)\t\tF(x)")
for x, p_val, f_val in zip(x_vals, P_x, F_x):
    print(f"{x}\t{p_val:.6f}\t{f_val:.6f}")

# Paso 3: Graficar F(x)
x_graf = [0] + x_vals + [x_vals[-1]+1]
F_graf = [0] + list(F_x) + [1.0]

plt.step(x_graf, F_graf, where='post', linestyle='--', marker='o')
plt.title('Función de Distribución Acumulada F(x) - Geométrica (p = 0.3)')
plt.xlabel('x (número de llamadas)')
plt.ylabel('F(x)')
plt.grid(True)
plt.xticks(range(1, 13))
plt.yticks(np.round(np.linspace(0, 1, 11), 2))
plt.show()

# Paso 4: Generador por el método de la inversa
def generar_geom_inversa(R, F_vals=F_x):
    for i, f in enumerate(F_vals):
        if R < f:
            return i + 1  # porque x comienza en 1
    return len(F_vals)  # en caso R ≈ 1

# Paso 5: Comprobación de valores R
valores_R = [0.2, 0.51, 0.7599, 0.85]
print("\nComprobación de valores R:")
for R in valores_R:
    x = generar_geom_inversa(R)
    print(f"Si R = {R}, entonces x = {x}")
