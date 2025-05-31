import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Paso 1: Definir f(x)
x_vals = np.linspace(7, 11, 400)
f_vals = np.piecewise(x_vals,
                      [x_vals < 8,
                       (x_vals >= 8) & (x_vals < 9),
                       (x_vals >= 9) & (x_vals < 10),
                       x_vals >= 10],
                      [0,
                       lambda x: x/2 - 15/4,
                       lambda x: -x/2 + 21/4,
                       0])

# Graficar f(x)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, f_vals, label=r'$f(x)$ por tramos', color='blue')
plt.title("Función de Densidad de Probabilidad f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.legend()
plt.show()

# Paso 2: Verificar que f(x) sea una FDP (área = 1)
x = sp.Symbol('x', real=True)

f1 = x/2 - 15/4
f2 = -x/2 + 21/4

int1 = sp.integrate(f1, (x, 8, 9))
int2 = sp.integrate(f2, (x, 9, 10))
total_area = int1 + int2

print("Área bajo f(x) entre 8 y 10:", total_area)  # Debe ser 1

# Paso 3: Definir y graficar F(x)
F1 = sp.integrate(f1, (x, 8, x))  # entre 8 y x < 9
F2 = int1 + sp.integrate(f2, (x, 9, x))  # entre 9 y x < 10

F_lamb = lambda x_vals: np.piecewise(x_vals,
    [x_vals < 8,
     (x_vals >= 8) & (x_vals < 9),
     (x_vals >= 9) & (x_vals < 10),
     x_vals >= 10],
    [0,
     sp.lambdify(x, F1, 'numpy'),
     sp.lambdify(x, F2, 'numpy'),
     1]
)

x_vals_cdf = np.linspace(7, 11, 400)
F_vals = F_lamb(x_vals_cdf)

plt.figure(figsize=(8, 5))
plt.plot(x_vals_cdf, F_vals, label="F(x): función de distribución acumulada", color='green')
plt.title("Función de Distribución Acumulada F(x)")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.grid(True)
plt.legend()
plt.show()

# Paso 4: Despejar F⁻¹(u) para los dos tramos

u = sp.Symbol('u')

# Primer tramo: F1 = x**2/4 - (15/4)*x + C
F1_expr = sp.integrate(f1, (x, 8, x))  # Usado arriba
inv1 = sp.solve(sp.Eq(u, F1_expr), x)
print("Inversa primer tramo (8 ≤ x < 9):", inv1)

# Segundo tramo: F2 = area1 + ∫f2
F2_expr = int1 + sp.integrate(f2, (x, 9, x))
inv2 = sp.solve(sp.Eq(u, F2_expr), x)
print("Inversa segundo tramo (9 ≤ x < 10):", inv2)

# Paso 5: Generar valores aleatorios por inversa
# Seleccionar funciones válidas por dominio
F1_inv_func = sp.lambdify(u, inv1[0], 'numpy')  # válido para u in [0, 0.5]
F2_inv_func = sp.lambdify(u, inv2[1], 'numpy')  # válido para u in (0.5, 1]

# Unimos ambos en función por tramos
def gen_x_from_u(u_vals):
    return np.piecewise(u_vals,
                        [u_vals <= 0.5, u_vals > 0.5],
                        [F1_inv_func, F2_inv_func])

# Generar u y x
u_vals = np.linspace(0, 1, 300)
x_generated = gen_x_from_u(u_vals)
F_computed = F_lamb(x_generated)

# Graficar scatter de puntos generados sobre F(x)
plt.figure(figsize=(8, 5))
plt.plot(x_vals_cdf, F_vals, label='F(x)', color='lightgray', linewidth=2)
plt.scatter(x_generated, F_computed, label='Puntos generados: inversa F⁻¹(u)', color='purple', alpha=0.7)
plt.title("Verificación: Puntos generados con F⁻¹(u) sobre F(x)")
plt.xlabel("x generado")
plt.ylabel("F(x)")
plt.grid(True)
plt.legend()
plt.show()
