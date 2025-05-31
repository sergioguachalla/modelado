import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Método de aceptación y rechazo
np.random.seed(42)
samples = []
n_samples = 200

while len(samples) < n_samples:
    x = np.random.uniform(0, 2)
    y = np.random.uniform(0, 1)

    # Definimos f(x)
    if 0 <= x < 1:
        fx = x
    elif 1 <= x < 2:
        fx = 0.5
    else:
        fx = 0

    if y <= fx:
        samples.append(x)

samples = np.array(samples)

# Paso 2: Definir f(x) y F(x)
x_vals = np.linspace(0, 2.5, 500)
f_vals = np.piecewise(x_vals,
                      [(x_vals >= 0) & (x_vals < 1),
                       (x_vals >= 1) & (x_vals < 2)],
                      [lambda x: x, lambda x: np.full_like(x, 0.5), 0])

F_vals = np.piecewise(x_vals,
                      [x_vals < 0,
                       (x_vals >= 0) & (x_vals < 1),
                       (x_vals >= 1) & (x_vals < 2),
                       x_vals >= 2],
                      [0,
                       lambda x: (x**2)/2,
                       lambda x: x/2,
                       1])


# Paso 3: Graficar
plt.figure(figsize=(10, 6))

# Histograma normalizado
plt.hist(samples, bins=20, density=True, alpha=0.6,
         label="Datos generados", edgecolor='black')

# f(x)
plt.plot(x_vals, f_vals, 'b-', lw=2, label='f(x)')

# F(x)
plt.plot(x_vals, F_vals, 'g--', lw=2, label='F(x)')

# Texto con los generadores en la parte izquierda del gráfico
plt.text(0.05, 0.95,
         r"$x = \sqrt{2R},\ R \in [0,\ 0.5]$" + "\n" + r"$x = 2R,\ R \in [0.5,\ 1]$",
         transform=plt.gca().transAxes,
         fontsize=11, verticalalignment='top',
         bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

# Estética
plt.title("Muestras generadas bajo f(x), con f(x) y F(x)")
plt.xlabel("x")
plt.ylabel("Densidad / Probabilidad acumulada")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()