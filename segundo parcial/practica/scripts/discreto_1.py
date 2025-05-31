import matplotlib.pyplot as plt
import numpy as np

# Paso 1: Definir la distribución de probabilidad discreta
valores_x = [0, 1, 2]
probabilidades = [0.5, 0.3, 0.2]  # P(x)

# Calcular F(x)
F_x = [probabilidades[0]]
for i in range(1, len(probabilidades)):
    F_x.append(F_x[-1] + probabilidades[i])

# Mostrar tabla con P(x) y F(x)
print("Tabla de P(x) y F(x):")
print("x\tP(x)\tF(x)")
for x, p, f in zip(valores_x, probabilidades, F_x):
    print(f"{x}\t{p}\t{f}")

# Paso 2: Graficar F(x)
x_vals_completos = [-1, 0, 1, 2, 3]
F_x_completo = [0, 0.5, 0.8, 1, 1]   # F(x) incluyendo valores extremos

plt.step(x_vals_completos, F_x_completo, where='post', linestyle='--', marker='o')
plt.title('Función de Distribución Acumulada F(x)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True)
plt.xticks(valores_x)
plt.yticks([0, 0.5, 0.8, 1])
plt.show()

# Paso 3: Función generadora (inversa de F)
def generar_valor_discreto(R):
    if R <= 0.5:
        return 0
    elif R <= 0.8:
        return 1
    else:
        return 2

# Paso 4: Comprobación con valores dados de R
valores_R = [0.2384, 0.7956, 0.9500]
print("\nComprobación de valores R:")
for R in valores_R:
    x = generar_valor_discreto(R)
    print(f"Si R = {R}, entonces x = {x}")
