import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Paso 1: Definir y graficar f(x)
x_vals = np.linspace(-1, 3, 400)
f_vals = np.piecewise(x_vals,
                      [x_vals < 0,
                       (x_vals >= 0) & (x_vals < 2),
                       x_vals >= 2],
                      [0,
                       lambda x: -x/2 + 1,
                       0])

plt.figure(figsize=(8, 5))
plt.plot(x_vals, f_vals, label='f(x) = -x/2 + 1 (para 0 ≤ x < 2)', color='blue')
plt.title("Gráfico de la Función de Densidad de Probabilidad f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.show()

# Paso 2: Verificar que es una FDP (área bajo la curva = 1)
x = sp.Symbol('x', real=True)
f_expr = -x/2 + 1
integral = sp.integrate(f_expr, (x, 0, 2))
print("Integral de f(x) de 0 a 2:", integral)  # Debe imprimir 1

# Paso 3: Construir y graficar F(x)
F_expr = -x**2/4 + x
F_lambdified = sp.lambdify(x, F_expr, 'numpy')

x_vals_fx = np.linspace(-1, 3, 400)
F_vals = np.piecewise(x_vals_fx,
                      [x_vals_fx < 0,
                       (x_vals_fx >= 0) & (x_vals_fx < 2),
                       x_vals_fx >= 2],
                      [0,
                       lambda x: F_lambdified(x),
                       1])

plt.figure(figsize=(8, 5))
plt.plot(x_vals_fx, F_vals, label='F(x) = -x²/4 + x (para 0 ≤ x < 2)', color='green')
plt.title("Gráfico de la Función de Distribución Acumulada F(x)")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.show()

# Paso 4: Despejar x en F(x) = u
u = sp.Symbol('u')
inv_eq = sp.solve(sp.Eq(u, F_expr), x)
print("Despeje simbólico de F(x) = u => x(u):", inv_eq)

# Escoger solución válida en [0, 2]
F_inv_expr = inv_eq[0]  # x = 2 - 2*sqrt(1 - u)
F_inv_func = sp.lambdify(u, F_inv_expr, 'numpy')

# Paso 5: Generar números aleatorios a partir de F⁻¹(u) y graficar sobre F(x)
u_vals = np.linspace(0, 1, 100)
x_gen = F_inv_func(u_vals)
F_gen = F_lambdified(x_gen)

plt.figure(figsize=(8, 5))
plt.plot(x_vals_fx, F_vals, label='F(x)', color='lightgray', linewidth=2)
plt.scatter(x_gen, F_gen, label='Puntos generados con inversa F⁻¹(u)', color='purple', alpha=0.7)
plt.title("Verificación: Puntos generados por F⁻¹(u) sobre F(x)")
plt.xlabel("x generado")
plt.ylabel("F(x)")
plt.grid(True)
plt.legend()
plt.show()
