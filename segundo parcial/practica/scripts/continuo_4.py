import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# ------------------------
# Definición de f(x) con valor 1 para x ≥ 10 (aunque no sea FDP válida)
# ------------------------
x_vals = np.linspace(2, 15, 600)
f_vals = np.piecewise(x_vals,
                      [x_vals < 3,
                       (x_vals >= 3) & (x_vals < 5),
                       (x_vals >= 5) & (x_vals < 8),
                       (x_vals >= 8) & (x_vals < 10),
                       x_vals >= 10],
                      [0,
                       lambda x: x/4 + 3/4,
                       1/2,
                       lambda x: -x/4 + 5/2,
                       1])  # intencionalmente incorrecto para ilustrar

# Gráfico de f(x)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, f_vals, label='f(x) (incluye 1 para x ≥ 10)', color='crimson')
plt.title("Función f(x): Incluye tramo constante igual a 1 desde x=10")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

# ------------------------
# Construcción de F(x)
# ------------------------
x = sp.Symbol('x', real=True)

f1 = x/4 + 3/4     # 3 <= x < 5
f2 = 1/2           # 5 <= x < 8
f3 = -x/4 + 5/2    # 8 <= x < 10

A1 = sp.integrate(f1, (x, 3, 5))
A2 = A1 + sp.integrate(f2, (x, 5, 8))
A3 = A2 + sp.integrate(f3, (x, 8, 10))

F1 = sp.integrate(f1, (x, 3, x))
F2 = A1 + sp.integrate(f2, (x, 5, x))
F3 = A2 + sp.integrate(f3, (x, 8, x))

F_lamb = lambda x_vals: np.piecewise(x_vals,
    [x_vals < 3,
     (x_vals >= 3) & (x_vals < 5),
     (x_vals >= 5) & (x_vals < 8),
     (x_vals >= 8) & (x_vals < 10),
     x_vals >= 10],
    [0,
     sp.lambdify(x, F1, 'numpy'),
     sp.lambdify(x, F2, 'numpy'),
     sp.lambdify(x, F3, 'numpy'),
     float(A3)])  # F(x)=constante después de 10

x_vals_cdf = np.linspace(2, 12, 500)
F_vals = F_lamb(x_vals_cdf)

plt.figure(figsize=(8, 5))
plt.plot(x_vals_cdf, F_vals, label='F(x)', color='green')
plt.title("Función de Distribución Acumulada F(x)")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.grid(True)
plt.legend()
plt.show()

# ------------------------
# Inversas por tramo (respetando rangos)
# ------------------------
u = sp.Symbol('u')
F1_expr = sp.integrate(f1, (x, 3, x))
F2_expr = A1 + sp.integrate(f2, (x, 5, x))
F3_expr = A2 + sp.integrate(f3, (x, 8, x))

inv1 = sp.solve(sp.Eq(u, F1_expr), x)[1]  # elegir la raíz positiva
inv2 = sp.solve(sp.Eq(u, F2_expr), x)[0]
inv3 = sp.solve(sp.Eq(u, F3_expr), x)[0]

# Lambdify inversas
inv1_func = sp.lambdify(u, inv1, 'numpy')
inv2_func = sp.lambdify(u, inv2, 'numpy')
inv3_func = sp.lambdify(u, inv3, 'numpy')

A1_f = float(A1)
A2_f = float(A2)
A3_f = float(A3)

# ------------------------
# Generar puntos con inversa de F
# ------------------------
def gen_x_from_u(u_vals):
    return np.piecewise(u_vals,
                        [u_vals <= A1_f,
                         (u_vals > A1_f) & (u_vals <= A2_f),
                         u_vals > A2_f],
                        [inv1_func, inv2_func, inv3_func])

# Generar u en el dominio correcto
u_vals = np.linspace(0, A3_f, 400)
x_generated = gen_x_from_u(u_vals)
F_computed = F_lamb(x_generated)

# ------------------------
# Gráfico scatter corregido (puntos sobre F(x))
# ------------------------
plt.figure(figsize=(8, 5))
plt.plot(x_vals_cdf, F_vals, label='F(x)', color='lightgray', linewidth=2)
plt.scatter(x_generated, F_computed, label='Puntos generados con F⁻¹(u)', color='purple', alpha=0.7)
plt.title("Verificación: Puntos generados con inversa F⁻¹(u) sobre F(x)")
plt.xlabel("x generado")
plt.ylabel("F(x)")
plt.grid(True)
plt.legend()
plt.show()
