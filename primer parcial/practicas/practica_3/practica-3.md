# Práctica 3
## Ejercicio 1

Sea $x=$ tiempo que tarda en programar (minutos)

| X       | $n_i$ | Marca de clase $\left(\frac{L_i+L_{i+1}}{2}\right)$ |
|---------|-------|---------------------------------|
| 10-15   | 30    | 12.5 |
| 15-20   | 25    | 17.5 |
| 20-25   | 22    | 22.5 |
| 25-30   | 18    | 27.5 |
| 30-35   | 19    | 32.5 |
| 35-40   | 12    | 37.5 |
| 40-45   | 8     | 47.5 |
| **Total** | **134** | |

## Se pide probar:
$$
H_0: X \sim \exp(1/\lambda)
$$
$$
H_1: X \neq \exp(1/\lambda)
$$

## Hallamos el estadístico:
$$
X^2_c = \sum \frac{(n_i - n_{ie})^2}{n_{ie}}
$$

Donde:
$$
n_{ie} = n P(X = x)
$$

Para el primer $n$ esperado:
$$
n_{1e} = 134 P(10 \leq x \leq 15)
$$
