import numpy as np
import pandas as pd
from scipy.stats import chi2

# -----------------------------------
# PARÁMETROS INICIALES
# -----------------------------------
n_datos = 100  # ← Puedes cambiar este número a lo que necesites
alpha = 0.5
beta = 0.6
h = beta - alpha
nivel_significancia = 0.05

# -----------------------------------
# GENERACIÓN DE DATOS ALEATORIOS
# -----------------------------------
datos = np.random.uniform(0, 1, n_datos)

# -----------------------------------
# CLASIFICACIÓN: DENTRO O FUERA DE [α, β]
# -----------------------------------
marcado = [1 if alpha <= x <= beta else 0 for x in datos]

# -----------------------------------
# DETECCIÓN DE HUECOS
# -----------------------------------
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

# -----------------------------------
# CATEGORIZAR HUECOS (0 a 4, luego 5+)
# -----------------------------------
huecos_categ = ["5+" if h >= 5 else str(h) for h in huecos]
categorias = ["0", "1", "2", "3", "4", "5+"]

# FRECUENCIAS OBSERVADAS
fo = pd.value_counts(huecos_categ, sort=False).reindex(categorias, fill_value=0)

# -----------------------------------
# FRECUENCIAS ESPERADAS
# -----------------------------------
n_huecos = len(huecos)
fe_values = [n_huecos * h * (1 - h)**i for i in range(5)]
fe_values.append(n_huecos * (1 - h)**5)  # para 5+
fe = pd.Series(fe_values, index=categorias)

# -----------------------------------
# PRUEBA CHI-CUADRADO
# -----------------------------------
chi2_obs = np.sum((fo - fe)**2 / fe)
gl = len(categorias) - 1
chi2_crit = chi2.ppf(1 - nivel_significancia, df=gl)

# -----------------------------------
# MOSTRAR RESULTADOS
# -----------------------------------
tabla = pd.DataFrame({
    'Huecos': categorias,
    'f_obs (nᵢ)': fo,
    'f_esp (nₑᵢ)': fe.round(4)
})

print("📊 TABLA DE FRECUENCIAS:\n")
print(tabla.to_string(index=False))

print("\n🔍 Estadístico Chi² calculado:", round(chi2_obs, 4))
print("📏 Chi² crítico (α = 0.05, gl = {}): {:.4f}".format(gl, chi2_crit))

# -----------------------------------
# CONCLUSIÓN FINAL
# -----------------------------------
if chi2_obs <= chi2_crit:
    print("\n✅ No se rechaza H₀: los números parecen independientes.")
else:
    print("\n❌ Se rechaza H₀: no se puede concluir que los números sean independientes.")
