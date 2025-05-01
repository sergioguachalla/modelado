import numpy as np
from scipy.stats import chi2
import pandas as pd

# -----------------------------
# Parámetros iniciales
# -----------------------------
alpha = 0.5
beta = 0.6
h = beta - alpha
nivel_significancia = 0.05

# -----------------------------
# Datos de ejemplo
# -----------------------------
datos = np.random.uniform(0, 1, 100)  # O reemplaza con tus datos

# -----------------------------
# Clasificación en 0s y 1s
# -----------------------------
marcado = [1 if alpha <= x <= beta else 0 for x in datos]

# -----------------------------
# Localizar huecos
# -----------------------------
huecos = []
contador = 0
dentro = False

for m in marcado:
    if m == 1:
        if dentro:
            huecos.append(contador)
        contador = 0
        dentro = True
    elif dentro:
        contador += 1

# -----------------------------
# Agrupar huecos en categorías
# -----------------------------
huecos_categ = ["5+" if h >= 5 else str(h) for h in huecos]
categorias = ["0", "1", "2", "3", "4", "5+"]

# Frecuencias observadas
fo = pd.value_counts(huecos_categ, sort=False).reindex(categorias, fill_value=0)

# -----------------------------
# Frecuencias esperadas
# -----------------------------
n = len(huecos)
fe_values = [n * h * ((1 - h)**i) for i in range(5)]
fe_values.append(n * ((1 - h)**5))  # categoría "5+"
fe = pd.Series(fe_values, index=categorias)

# -----------------------------
# Prueba Chi-cuadrado
# -----------------------------
chi2_obs = np.sum((fo - fe)**2 / fe)
gl = len(categorias) - 1
chi2_crit = chi2.ppf(1 - nivel_significancia, df=gl)

# -----------------------------
# Resultados
# -----------------------------
tabla = pd.DataFrame({
    'Huecos': categorias,
    'f_obs (nᵢ)': fo,
    'f_esp (nₑᵢ)': fe.round(4)
})

print("📊 Tabla de frecuencias:")
print(tabla.to_string(index=False))
print("\n🔍 Estadístico Chi²:", round(chi2_obs, 4))
print("📏 Chi² crítico (α = 0.05, gl = {}): {:.4f}".format(gl, chi2_crit))

# -----------------------------
# Conclusión
# -----------------------------
if chi2_obs <= chi2_crit:
    print("\n✅ No se rechaza H₀: los números parecen ser independientes.")
else:
    print("\n❌ Se rechaza H₀: no se puede concluir que los números sean independientes.")
