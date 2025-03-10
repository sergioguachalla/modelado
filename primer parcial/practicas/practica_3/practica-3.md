# Práctica 3
## Ejercicio 1

Sea $x=$ tiempo que tarda en programar (minutos)

### Datos proporcionados:

| Intervalo $X$ | Frecuencia Observada $n_i$ | Marca de Clase $\left(\frac{L_i+L_{i+1}}{2}\right)$ |
|--------------|-----------------|---------------------------------|
| 10-15       | 30              | 12.5 |
| 15-20       | 25              | 17.5 |
| 20-25       | 22              | 22.5 |
| 25-30       | 18              | 27.5 |
| 30-35       | 19              | 32.5 |
| 35-40       | 12              | 37.5 |
| 40-45       | 8               | 47.5 |
| **Total**   | **134**         | |

### 1. Estimación de $\lambda$
Para la distribución exponencial, el parámetro $\lambda$ se estima como:
$$
\lambda = \frac{1}{\bar{x}}
$$
donde $\bar{x}$ es la media muestral, calculada como:
$$
\bar{x} = \frac{\sum (n_i \cdot \text{Marca de Clase})}{\sum n_i}
$$

Calculamos $\bar{x}$:

$$
\bar{x} = \frac{(30 \cdot 12.5) + (25 \cdot 17.5) + (22 \cdot 22.5) + (18 \cdot 27.5) + (19 \cdot 32.5) + (12 \cdot 37.5) + (8 \cdot 47.5)}{134}
$$

$$
\bar{x} = \frac{(375 + 437.5 + 495 + 495 + 617.5 + 450 + 380)}{134} = \frac{3249}{134} \approx 24.25
$$

Por lo tanto,

$$
\lambda = \frac{1}{24.25} \approx 0.04124
$$

### 2. Cálculo de Probabilidades
La función de distribución acumulada (FDA) de una distribución exponencial es:

$$
P(a \leq X \leq b) = e^{-\lambda a} - e^{-\lambda b}
$$

Para cada intervalo, calculamos:

- **Para $10 \leq x \leq 15$**:
  $$
  P(10 \leq X \leq 15) = e^{-0.04124(10)} - e^{-0.04124(15)}
  $$
  $$
  = e^{-0.4124} - e^{-0.6186}
  $$
  $$
  = 0.662 - 0.538
  $$
  $$
  = 0.124
  $$

  Número esperado:
  $$
  n_{1e} = 134 \times 0.124 = 16.62
  $$

- **Para $15 \leq x \leq 20$**:
  $$
  P(15 \leq X \leq 20) = e^{-0.6186} - e^{-0.8248}
  $$
  $$
  = 0.538 - 0.439
  $$
  $$
  = 0.099
  $$

  Número esperado:
  $$
  n_{2e} = 134 \times 0.099 = 13.27
  $$

- **Para $20 \leq x \leq 25$**:
  $$
  P(20 \leq X \leq 25) = e^{-0.8248} - e^{-1.031}
  $$
  $$
  = 0.439 - 0.356
  $$
  $$
  = 0.083
  $$

  Número esperado:
  $$
  n_{3e} = 134 \times 0.083 = 11.12
  $$

- **Para $25 \leq x \leq 30$**:
  $$
  P(25 \leq X \leq 30) = e^{-1.031} - e^{-1.237}
  $$
  $$
  = 0.356 - 0.290
  $$
  $$
  = 0.066
  $$

  Número esperado:
  $$
  n_{4e} = 134 \times 0.066 = 8.84
  $$

- **Para $30 \leq x \leq 35$**:
  $$
  P(30 \leq X \leq 35) = e^{-1.237} - e^{-1.444}
  $$
  $$
  = 0.290 - 0.236
  $$
  $$
  = 0.054
  $$

  Número esperado:
  $$
  n_{5e} = 134 \times 0.054 = 7.24
  $$

- **Para $35 \leq x \leq 40$**:
  $$
  P(35 \leq X \leq 40) = e^{-1.444} - e^{-1.650}
  $$
  $$
  = 0.236 - 0.192
  $$
  $$
  = 0.044
  $$

  Número esperado:
  $$
  n_{6e} = 134 \times 0.044 = 5.90
  $$

- **Para $40 \leq x \leq 45$**:
  $$
  P(40 \leq X \leq 45) = e^{-1.650} - e^{-1.856}
  $$
  $$
  = 0.192 - 0.157
  $$
  $$
  = 0.035
  $$

  Número esperado:
  $$
  n_{7e} = 134 \times 0.035 = 4.69
  $$

### 3. Cálculo del Estadístico $X^2_c$
$$
X^2_c = \sum \frac{(n_i - n_{ie})^2}{n_{ie}}
$$

Sustituyendo los valores:

$$
X^2_c = \frac{(30 - 16.62)^2}{16.62} + \frac{(25 - 13.27)^2}{13.27} + \frac{(22 - 11.12)^2}{11.12}
$$
$$
+ \frac{(18 - 8.84)^2}{8.84} + \frac{(19 - 7.24)^2}{7.24} + \frac{(12 - 5.90)^2}{5.90} + \frac{(8 - 4.69)^2}{4.69}
$$

$$
X^2_c \approx 10.99 + 8.24 + 10.54 + 9.43 + 13.63 + 6.43 + 2.37
$$

$$
X^2_c \approx 61.63
$$

### 4. Comparación con $X^2_{crítico}$
Para $\alpha = 0.05$ y $k-1 = 7-1 = 6$ grados de libertad, de la tabla chi-cuadrado:

$$
X^2_{0.05,6} = 12.59
$$

Dado que $X^2_c > X^2_{0.05,6}$, rechazamos $H_0$. Esto significa que los datos **no siguen** una distribución exponencial.
## Ejercicio 2
6 monedas fueron lanzadas 1400 veces:
$x$ : número de caras

|x|0|1|2|3|4|5|6|
|---|---|---|---|---|---|---|---|
|$n_i$|36|146|342|350|320|158|48|
Se quiere probar que $x$ tiene distribución binomial

$$
H_0: x=b(m;p)
H_i: x \neq(m;p)
$$

### **Paso 1: Estimación de \( p \)**
Para una distribución **binomial** \( B(m, p) \), la media se calcula como:  

$$
\bar{x} = m p
$$

La media muestral se obtiene como:

$$
\bar{x} = \frac{\sum x_i n_i}{\sum n_i}
$$

Sustituyendo los valores:

$$
\bar{x} = \frac{(0 \cdot 36) + (1 \cdot 146) + (2 \cdot 342) + (3 \cdot 350) + (4 \cdot 320) + (5 \cdot 158) + (6 \cdot 48)}{1400}
$$

$$
\bar{x} = \frac{0 + 146 + 684 + 1050 + 1280 + 790 + 288}{1400} = \frac{4238}{1400} \approx 3.03
$$

Como \( m = 6 \), estimamos \( p \):

$$
p = \frac{\bar{x}}{m} = \frac{3.03}{6} \approx 0.505
$$

---

### **Paso 2: Cálculo de Probabilidades Teóricas**  

La fórmula de la **distribución binomial** es:

$$
P(x) = \binom{m}{x} p^x (1 - p)^{m - x}
$$

Para cada \( x \):

$$
P(x) = \binom{6}{x} (0.505)^x (1 - 0.505)^{6 - x}
$$

Calculamos los valores:

| \( x \) | \( \binom{6}{x} \) | \( P(x) \) |
|---------|----------------|-----------|
| 0       | 1              | \( (0.495)^6 = 0.0215 \) |
| 1       | 6              | \( 6 (0.505)^1 (0.495)^5 = 0.0779 \) |
| 2       | 15             | \( 15 (0.505)^2 (0.495)^4 = 0.1797 \) |
| 3       | 20             | \( 20 (0.505)^3 (0.495)^3 = 0.2481 \) |
| 4       | 15             | \( 15 (0.505)^4 (0.495)^2 = 0.2248 \) |
| 5       | 6              | \( 6 (0.505)^5 (0.495)^1 = 0.1186 \) |
| 6       | 1              | \( (0.505)^6 = 0.0304 \) |

Los valores esperados \( E_i \) se calculan multiplicando por 1400:

$$
E_i = 1400 \cdot P(x)
$$

| \( x \) | \( n_i \) | \( P(x) \) | \( E_i = 1400 P(x) \) |
|---------|----------|------------|----------------|
| 0       | 36       | 0.0215     | 30.1          |
| 1       | 146      | 0.0779     | 109.1         |
| 2       | 342      | 0.1797     | 251.6         |
| 3       | 350      | 0.2481     | 347.3         |
| 4       | 320      | 0.2248     | 314.7         |
| 5       | 158      | 0.1186     | 166.1         |
| 6       | 48       | 0.0304     | 42.6          |

---

### **Paso 3: Cálculo de \( X^2 \)**
La fórmula del estadístico **chi-cuadrado** es:

$$
X^2 = \sum \frac{(n_i - E_i)^2}{E_i}
$$

Sustituyendo los valores:

$$
X^2 = \frac{(36 - 30.1)^2}{30.1} + \frac{(146 - 109.1)^2}{109.1} + \frac{(342 - 251.6)^2}{251.6}
$$
$$
+ \frac{(350 - 347.3)^2}{347.3} + \frac{(320 - 314.7)^2}{314.7} + \frac{(158 - 166.1)^2}{166.1} + \frac{(48 - 42.6)^2}{42.6}
$$

$$
X^2 \approx \frac{5.9^2}{30.1} + \frac{36.9^2}{109.1} + \frac{90.4^2}{251.6} + \frac{2.7^2}{347.3} + \frac{5.3^2}{314.7} + \frac{8.1^2}{166.1} + \frac{5.4^2}{42.6}
$$

$$
X^2 \approx 1.16 + 12.47 + 32.47 + 0.02 + 0.09 + 0.39 + 0.68
$$

$$
X^2 \approx 47.28
$$

---

### **Paso 4: Comparación con \( X^2 \) Crítico**
Para \( k-1 = 7-1 = 6 \) grados de libertad y \( \alpha = 0.05 \), buscamos en la tabla de chi-cuadrado:

$$
X^2_{0.05,6} = 12.59
$$

Como:

$$
X^2_c = 47.28 > X^2_{0.05,6} = 12.59
$$

**Rechazamos \( H_0 \)** y concluimos que **los datos NO siguen una distribución binomial**.

---

### **📌 Conclusión**
Dado que el valor de \( X^2 \) calculado es significativamente mayor que el valor crítico, podemos decir que **los datos no siguen una distribución binomial con los parámetros estimados**.
