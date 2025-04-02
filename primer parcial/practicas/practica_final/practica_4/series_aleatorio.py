import numpy as np
from scipy.stats import chi2

# Función para realizar la prueba de series
def prueba_series(n, N, alpha=0.05):
    # Generamos N datos aleatorios de una distribución uniforme U(0,1)
    datos = np.random.uniform(0, 1, N)
    
    # Dividimos los datos en n intervalos (por ejemplo, n=5)
    intervalos = np.linspace(0, 1, n+1)  # Limites de los intervalos
    
    # Inicializamos la matriz de cuentas (n-1 x n-1)
    a = np.zeros((n, n))
    
    # Contamos cuántos valores caen en cada combinación de intervalos
    for i in range(N-1):
        for j in range(i+1, N):
            # Verificamos en qué intervalos caen los valores i y j
            intervalo_i = np.digitize(datos[i], intervalos) - 1
            intervalo_j = np.digitize(datos[j], intervalos) - 1
            a[intervalo_i, intervalo_j] += 1
    
    # Frecuencia esperada bajo la hipótesis nula
    esperado = (N-1) / n**2
    
    # Calculamos el estadístico chi-cuadrado
    chi_cuadrado = (n**2 / (N - 1)) * np.sum((a - esperado)**2)
    
    # Grados de libertad
    df = (n - 1)  # Para n intervalos
    
    # Valor crítico de la chi-cuadrado para el nivel de significancia y los grados de libertad
    chi_critico = chi2.ppf(1 - alpha, df)
    
    # Mostramos los resultados
    print(f"Matriz de frecuencias observadas (a_ij):\n{a}")
    print(f"Frecuencia esperada por intervalo: {esperado:.2f}")
    print(f"Estadístico chi-cuadrado calculado: {chi_cuadrado:.2f}")
    print(f"Valor crítico chi-cuadrado para {df} grados de libertad y alpha={alpha}: {chi_critico:.2f}")
    
    # Decisión sobre la hipótesis
    if chi_cuadrado > chi_critico:
        print("Se rechaza la hipótesis nula: La distribución no es uniforme U(0,1).")
    else:
        print("No se rechaza la hipótesis nula: Los datos siguen una distribución uniforme U(0,1).")

# Parámetros
n = int(input("Ingrese el número de intervalos (n): "))  # Número de intervalos
N = int(input("Ingrese el número de datos (N): "))  # Número de datos aleatorios a generar
alpha = 0.05  # Nivel de significancia

# Llamada a la función para realizar la prueba de series
prueba_series(n, N, alpha)
