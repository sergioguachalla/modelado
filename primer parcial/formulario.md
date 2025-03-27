# Formulario Modelado

## Congruencial mixto
$$X_{n+1} = (aX_n + c) \mod m $$
    
- $X_o$ : semilla $(Xo > 0)$
- $a$: multiplicador $(a > 0)$
- $c$ : constante aditiva $(c > 0)$
- $m$: modulo $(m > Xo), m>a, m>c)$

## Método congruencial multiplicativo

$$X_{n+1} = ax_n \space mod \space m$$

- $X_o$ : semilla $(Xo > 0)$
- $a$: multiplicador $(a > 0)$
- $m$: modulo $(m > Xo), m>a, m>c)$

## Cuadrados medios
Pasos:
1. Seleccionar una semilla $(X_0)$ con $D$ dígitos ($D>3$)
2. Sea $y_o =$ resultado de elevar $x_0$ al cuadrado.
3. Sea $y_i =$ resultado de elevar $x_i$ al cuadrado y sera $r_i=0 ,$ D digitos del centro $\forall [=1,2,3...n]$
4. Repetir el paso 3 hasta obtener los n números $r_i$ deseados
## Productos medios
$x_0 = a; \space x_1 = b; \space D = d$

$y_0 = a \times b; \space x_2 = d \text{digitos del centro}; \space r_1 = 0,\{ d \}$ 


## Prueba de hipotesis (distribucion exponencial)

$$H_0: x = exp(\frac{1}{\lambda})$$
$$H_1: x \neq exp(\frac{1}{\lambda})$$
$\LARGE{
   \chi_c^2 = \frac{(n_{io}-n_{ie})^2}{n_{ie}} 
}$

$\large{
    n_{ie} = nP(X=x)
}$

$\Large{
    f(x) = \frac{1}{\lambda}e^{-\lambda x} 
}$

$\large{
    \lambda = ? \space => E(x) = \bar{x} \space \text{=>} \lambda = \bar{x}
}$

$\Large{
    \bar{x} = \sum \frac{x_i n_i}{n}
}$

$\LARGE{
    n_{ie} = n[-e^{\frac{-L_s}{\bar{x}}} + e^{\frac{-L_i}{\bar{x}}}]
}$

$\large{
    RC: \chi_c^2 > \chi_{k-r-1}^2; RH_o
}$

>k = filas
>r = parámetros de la distribución

## Prueba de hipotesis (distribucion binomial)
$$H_0: x = b(m;p)$$
$$H_1: x \neq b(m;p)$$
$\LARGE{
   \chi_c^2 = \frac{(n_{io}-n_{ie})^2}{n_{ie}} 
}$

$\large{
    n_{ie} = nD(X=x)
}$

$\Large{
    P(x) = \binom{n}{x}\space p^k \space (1-p)^{n-k}
}$

$\large{
    \binom{n}{x} = \frac{n!}{x! (n-x)!}
}$

## Prueba de la Varianza
$$H_0:\sigma^2=\frac{1}{12}$$
$$H_i: \sigma^2 \neq \frac{1}{12}$$



$\Large{LI = \frac{\chi^2_{1-\alpha/2};n-1}{12(n-1)}}$

$\Large{LS= \frac{\chi^2_{\alpha/2};n-1}{12(n-1)}}$

Hallamos la varianza muestral:

$\Large{
    V(r) = \sum\frac{({r_i - \bar{r}})^2}{12(n-1)}
}$

> **Si la varianza muestral está dentro del límite no se rechaza la hipótesis nula**
## Prueba de frecuencias
$$H_0: x = U(0;1) $$
$$H_i: x \neq U(0;1)$$
$\LARGE{
   \chi_c^2 = \frac{(n_{io}-n_{ie})^2}{n_{ie}} 
}$

$\large{
RC: \chi_c^2 > \chi_{n-1}^2;1-\alpha; RH_0
}$

Donde $n =$ número de segmentos

Para n = 5

|$\large{N_{ie}}$|$\large{\frac{N}{n}}$| $\large{\frac{N}{n}}$|$\large{\frac{N}{n}}$|
|---|---|---|---|
|$\large{N_{io}}$| $\large{\frac{1}{n}}$|$\large{\frac{n-1}{n}}$|$\large{\frac{n}{n}}$

## Prueba de Series
$$H_0: x = U(0;1) $$
$$H_i: x \neq U(0;1)$$
$\LARGE{
   \chi_c^2 = \frac{n^2}{N-1} \sum_i \sum_j (n_{io}- \frac{N-1}{n^2})
}$

$\Large{
    x_{n2-1}^2;1-\alpha
}$

$\large{
RC: \chi_c^2 > \chi_{n-1}^2;1-\alpha; RH_0
}$

|$\large{\frac{n-1}{n}}$|$\large{}a_{i_1j_1}$|$\large{}a_{i_1j_2}$|$\large{}a_{i_1j_3}$|
|----|---|---|---|
|$\large{\frac{n-2}{n}}$|
|$\large{\frac{1}{n}}$|
||$\large{\frac{1}{n}}$|$\large{\frac{2}{n}}$|$\large{\frac{n}{n}}$|

Donde $\large{}a_{ij}$ es la cuenta de cuántos valores caen en el intervalo

## Prueba de Kolmogorov
$$H_0: x = U(0;1)$$
$$H_1: x \neq U(0;1)$$
$\Large{
    D_n = max[F_n(x) - x_i]
}$

$\large{
    RC: D_n < d_n; \alpha; N
}$

1. Generar números aleatorios
2. Ordenar de forma ascendente
3. Calcular:

$$\large{
    F_n(x) = \frac{i}{n}; i 
}$$

$$\large{
    D_n = Max|F_n(x) - x_i| \forall x_i  
}$$

$$\large{
    d_n=\sqrt{\frac{-\ln(\alpha/2)}{2n}}
}
$$

## Prueba de uniformidad
$$H_0: nros = U(0;1)$$
$$H_i: nros \neq U(0;1)$$

$\Large{
    \chi_c^2 = \sum\frac{(n_{io}-n_{ie})^2}{n_{ie}}
}$

$\Large{RC: \chi_c^2 < \chi_{m-1}^2; 1-\alpha} | NRH_0$

$\Large{
    c = \frac{R}{\sqrt{n}} = \frac{max - min }{\sqrt{n}}
}$

|$\large{L_i - L_{i+1}}$|Conteo|$\large{n_{io}}$|$\large{n_{ie} = \frac{n}{m}}$|$\large{\frac{(n_{io} - n_{ie})^2}{n_{ie}}}$|
|---|---|---|---|---|
|$min - L_i + c$|a | a| b| c|
|$\large{L_i - L_{i+1} + c}$|a | a| b| c|

> Hasta tener el número de intervalos $n = datos, m = intervalos$

## Prueba de poker
$$H_0: nros = U(0;1)$$
$$H_i: nros \neq U(0;1)$$

$\Large{
    \chi_c^2 = \sum\frac{(n_{io}-n_{ie})^2}{n_{ie}}
}$

$\Large{RC: \chi_c^2 > \chi_m-1^2; 1-\alpha} | RH_0$

$\large{
    P(diferentes) = 0,30240
}$
$\large{
    P(par) = 0.50400
}$
$\large{
    P(2\space\text{pares}) = 0,10800 
}$
$\large{
    P(\text{tercia}) = 0,07200 
}$
$\large{
    P(\text{full}) = 0,0009
}$
$\large{
    P(\text{poker}) = 0,00450 
}$
$\large{
    P(\text{quintilla}) = 0,0001 
}$

|Categoría|Conteo|$\large{n_{ie}}$|$\large{n_{io}}$|$\large{\frac{(n_{io} - n_{ie})^2}{n_{ie}}}$|
|---|---|---|---|---|
|${\text{todos diferentes}}$|a |$b = P(cat) \times n$| a|$\large{\frac{(a_i - b_i )^2}{b_i}}$|
|${\text{Un par}}$|a | $b = P(cat) \times n$| b|$\large{\frac{(a_i - b_i )^2}{b_i}}$|
|${\text{Dos pares}}$|a | $b = P(cat) \times n$| b|$\large{\frac{(a_i - b_i )^2}{b_i}}$|
|${\text{tercia}}$|a | $b = P(cat) \times n$| $a$|$\large{\frac{(a_i - b_i )^2}{b_i}}$|
|$Poker$|a | $b = P(cat) \times n$| b|$\large{\frac{(a_i - b_i )^2}{b_i}}$|
|$Full$|a | $b = P(cat) \times n$| b|$\large{\frac{(a_i - b_i )^2}{b_i}}$|
|$Quintilla$|a | $b = P(cat) \times n$| b|$\large{\frac{(a_i - b_i )^2}{b_i}}$|

> $m = \text{las columnas que tienen datos}$

## Prueba de la media
$$H_0: \mu = \frac{1}{2}$$
$$H_i: \mu \neq \frac{1}{2}$$

$\Large{
    Z_c = \frac{(\bar{x} - \mu)\sqrt{n}}{\sqrt{\frac{1}{12}}}
}$

$\large{
    \text{Donde } \mu = \frac{1}{2} \text{ y } \bar{x} = \frac{\sum x_i}{n} 
}$

$\Large{
   \text{Si } Z_c \text{ está dentro del intervalo } [-Z_{1-\alpha/2}; Z_{1-\alpha/2}] \text{ no se rechaza la hipótesis nula}
}$

## Pruebas de las corridas arriba y abajo
$$H_0: \text{son indenpendientes}$$
$$H_i: \text{no son indenpendientes}$$

$\Large{
    Z_c = \mid \frac{C_o - \mu_{co}}{\sigma_{co}}\mid
}$

$\large{
    RC: \mid Z_c\mid > Z_{1-\alpha} ; RH_o
}$

$
\Large{
    \mu_{co} = \frac{2n -1 }{3}
}$

$\Large{
    \sigma^2 = \frac{16n - 29}{90}
}$

> $\large{\text{Si } r_{i-1} < r_i => 1}$

> $\large{\text{Si } r_{i-1} > r_i => 0}$

## Prueba de corridas media

$$H_0: \text{son indenpendientes}$$
$$H_i: \text{no son indenpendientes}$$

$\Large{
    Z_c= \frac{C_{o} - \mu_{co}}{\sigma_{co}}
}$

$\Large{
    \mu_{co} = \frac{2n_0 \space n_1}{n} + \frac{1}{2}
}$

$\Large{
    \sigma^2 = \frac{2n_0 \space n_1 \times (2n_0\space n_1 - n) }{n^2(n-1)}
}$

$\large{
    RC: -Z_{1-\frac{\alpha}{2}} < Z_c < +Z_{1-\frac{\alpha}{2}}
}$

>Si está fuera se $RH_o$

>$\large{\text{Si } r_1 > 0,5 => 1; 0}$