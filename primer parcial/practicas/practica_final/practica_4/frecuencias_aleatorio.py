import numpy as np
from scipy.stats import chi2

# Función para realizar la prueba de frecuencias
def prueba_frecuencias(n, alpha=0.05):
    # Generamos n datos aleatorios de una distribución uniforme U(0,1)
    datos = np.random.uniform(0, 1, n)  # Generamos n datos aleatorios
    print(f"Datos generados aleatoriamente: {datos}")
    
    # Dividimos los datos en n segmentos (por ejemplo, n=5)
    segmentos = np.linspace(0, 1, n + 1)  # Limites de los segmentos
    
    # Contamos cuántos datos caen en cada segmento
    observados = np.histogram(datos, bins=segmentos)[0]
    
    # Frecuencia esperada para cada segmento (suponiendo distribución uniforme)
    esperado = len(datos) / n
    
    # Calculamos el estadístico chi-cuadrado
    chi_cuadrado = np.sum((observados - esperado)**2 / esperado)
    
    # Grados de libertad
    df = n - 1
    
    # Valor crítico de la chi-cuadrado para el nivel de significancia y los grados de libertad
    chi_critico = chi2.ppf(1 - alpha, df)
    
    # Mostramos los resultados
    print(f"Frecuencias observadas: {observados}")
    print(f"Frecuencias esperadas: {esperado:.2f} para cada segmento")
    print(f"Estadístico chi-cuadrado calculado: {chi_cuadrado:.2f}")
    print(f"Valor crítico chi-cuadrado para {df} grados de libertad y alpha={alpha}: {chi_critico:.2f}")
    
    # Decisión sobre la hipótesis
    if chi_cuadrado > chi_critico:
        print("Se rechaza la hipótesis nula: La distribución no es uniforme U(0,1).")
    else:
        print("No se rechaza la hipótesis nula: Los datos siguen una distribución uniforme U(0,1).")

# Parámetros
n = int(input("Ingrese el número de datos (n): "))  # Número de datos aleatorios a generar
alpha = 0.05  # Nivel de significancia

# Llamada a la función para realizar la prueba de frecuencias
prueba_frecuencias(n, alpha)
