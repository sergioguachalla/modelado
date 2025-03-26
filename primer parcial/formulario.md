# Formulario Modelado
## Prueba de la Varianza
$$H_0:\sigma^2=\frac{1}{12}$$
$$H_i: \sigma^2 \neq \frac{1}{12}$$


$\Large{LI = \frac{\chi^2_{1-\alpha/2};n-1}{12(n-1)}}$

$\Large{LS= \frac{\chi^2_{\alpha/2};n-1}{12(n-1)}}$

> $N_{io}$ son los que caen dentro del intervalo

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

Donde $n = $ número de segmentos

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
