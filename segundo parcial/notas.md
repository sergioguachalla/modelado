## Generacion de números aleatorios no uniformes
### Método de la transformada inversa

Ej: Se desea generar números aleatorios que sigan la siguiente función de probabilidad

$F(x) = \lambda e ;\space x>0$ 

$F(x) = P(X \leq x) = \int_{-\inf}^x f(x)dx$

$\Large{
    \lambda(-\frac{e^{-\lambda x}}{\lambda}) = \lambda (-\frac{e^{\lambda x}}{\lambda} - (-\frac{e^0}{\lambda}))
}$

$\large{
     = -e^{-\lambda x} + 1
}$

$R = 1 - e^{-e\lambda}$

$\large{
     \text{ya que R y 1 - R van de 0 a 1 (en la distribución exponencial):}
}$

$R = e^{-\lambda x}$

$\ln R = -\lambda x$

$\Large{
    x = \frac{\ln{R}}{\lambda}
}$

Para $\lambda = 2$


$\large{
    x = \frac{\ln{R}}{\lambda}
}$

|nro aleatorio|$\large{}x$|
|----|----|
|$r_i$| $x_i$|