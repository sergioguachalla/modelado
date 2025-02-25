# Modelado, Dinámica de sistemas
## I. Introducción
> - Thomas Naylor => Simulación es una técnica numérica para conducir experimentos en una computadora digital, estos experimentos, comprenden ciertos tipos de relaciones matemáticas y lógicas, las cuales son necesarias para describir el **comportamiento** y la escritura de sistemas complejos del mundo real a traves de largos periodos de tiempo.
> - H. Marsel => Simulación es una técnica numérica para realizar experimentos en una computadora digital. Estos experimentos involucran ciertos tipos de modelos matemáticos lógicos que describen el comportamiento de sistemas de negocios canónicos, sociales, biologicos, fisicos o quimico a través de largos periodos de tiempo.
> - R. Shannon => Simulación es el proceso de diseñar y desarrollar un modelo computarizado de un sistema o proceso y conducir experimentos con este modelo con el propósito de entender el comportamiento del sistema o evaluar varias estrategias con las cuales se puede operar el sistema.

### Etapas de un estudio de simulación

1. Definición de sistema => definir el sistema *(dónde voy a trabajar)*. Para tener una definición exacta del sistema que se desea simular es necesario hacer primeramente un análisis preliminar del mismo con el fin de determinar la interacción del sistema con otros sistemas, las restricciones del sistema, las variables que interactuan dentro del sistema y sus interrelaciones, las medidas de efectividad que se van a utilizar para definir y estudiar el sistema y los resultados que se esperan obtener.
2. Formulación del modelo => Una vez que estan definidos con exactitud los resultados que se esperan obtener del estudio el siguiente paso es definir y construir el modelo con el cual se obtendrán los resultados deseados.
3. Colección de datos 
4. Implementar el modelo en la computadora      

 ---- 
04/02/2025

5.  Validación

    Las formas más comunes de validar un modelo son:
    1. la opinión de expertos sobre los resultados de la simulación
    2. La exactitud con la que se predicen los datos históricos.
    3. la exactitud de la predicción del futuro.
    4. la comprobación de falla del modelo.
    5. la aceptación y confianza en el modelo de la persona que hará uso de los resultado que arroje el experimento de la simulación
6. Interpretación => Existen dos tipos de documentación: técnica y manual de usuario.

### Generación de números aleatorios rectangulares

Deben poseer ciertas características deseables que aseguren o aumenten la confiabilidad. Tales características son:
- Uniformemente distribuido
- Estadísticamente independiente
- Son reproducibles
- Periodo largo (no se trunca en la cantidad de números)
- Generados a través de un método rápido
- Generados a través de un método que no requiera mucha capacidad de almacenamiento.

### Generadores congruenciales lineales
+ Congruencial mixto => $$X_{n+1} = (aX_n + c) \mod m $$
    - Xo : semilla (Xo > 0)
    - a: multiplicador (a > 0)
    - c : constante aditiva (c > 0)
    - m: modulo (m > Xo), m>a, m>c)

> Ejemplo
> Se pide generar números aleatorios cuando $$ a = 5, c = 7,  X_0,  m=8 $$
[Ejemplo](./ejemplos/cgl_example.py)
***Periodo n significa que cada n números la secuencia se va repitiendo.***

Existe la necesidad de establecer algunas reglas que pueden ser utilizadas en la selección de los valores de los parámetros para que el generador resultante tenga periodo completo, algunas de estas reglas se mencionan a continuación:
#### Selección de m 
Existen 2 opciones para seleccionar el valor apropiado de m:
1. Seleccionar *m* de modo que sea el número primo más grande posible y que a su vez sea menor que $$P^d$$ donde p es la base del sistema (binario, decimal, etc.) que se está utilizando y d es el númeo de bits.
2. Seleccionar *m* como $$ P^d$$   
> Ejemplo 
> Se pide generar números aleatorios:
> $$ c = 89; x_0 = 5; m = 10^2; a= 81 $$
[Ejemplo](./ejemplos/cgl_example.py)

-----
06/02
### Selección de a
Debe ser un número impar y no debe ser divisible entre 3 y 5. Además para asegurarnos para que tenga periodo completo seguir:
- $(a-1)mod4$ => 4 no sea factor de $m$.
- $(a-1)mod4 = 0$ => si $b$ factor primo de $m$
- se selecciona a como $2^k+1$ o $10^k +1$ en ambos casos $>=2$

### Selección de c
El valor seleccionado para este parámetro puede ser cualquier constante, si se desean asegurar buenos resultados el valor de $c$ debe ser $cmod8=5$ si se trabaja en sistema binario y $c$ como $cmod200=21$ si se trabaja en sistema decimal. Más específicamente el valor de $c$ debe ser un entero impar y relativamente primo a $m$.
### Método congruencial multiplicativo

$$X_{n+1} = ax_n modm$$
> Ejemplo
> 
>Generar números aleatorios de $X_{n+1} = 3X_n mod 100$
>
> Datos: $X_0 = 17$
> [Ejemplo](/primer%20parcial/ejemplos/cgm_example.py)

>Ejercicio
>
> $X_{n+1} = (8x_n +16) mod 100; x_0 = 15$
> [Ejercicio](/primer%20parcial/ejemplos/cgm_example.py)

> Ejercicio 2
>
>$X_{n+1} = 211 X_n mod 10^8; x_0=13$


-------
10/02
### Algoritmo de cuadrados medios
Pasos:
1. Seleccionar una semilla $(X_0)$ con $D$ dígitos ($D>3$)
2. Sea $y_o =$ resultado de elevar $x_0$ al cuadrado.
3. Sea $y_i =$ resultado de elevar $x_i$ al cuadrado y sera $r_i=0 ,$ D digitos del centro $\forall [=1,2,3...n]$
4. Repetir el paso 3 hasta obtener los n números $r_i$ deseados

> Ejemplo
>
>Generar los primeros 6 números $r_i$, apartir de la semilla $x_0=5735, D=4$
>
>**Solución**
>
> #TODO: add picture 

### Algoritmo de productos medios
1. Seleccionar una semilla $(X_0)$ con $D$ dígitos ($D>3$)
2. Seleccionar una semilla $X_1$ con $D$ digitos ($D>3$)
3. Sea $y_0 = x_0 * x_1$; sea $x_2=$ digitos $D$ del centro y sea $r_i = 0. D$ del centro
4. sea $y_i=x_i*x_{i-1}; x_{i+1}=$ los d digitos del centro y sea $r_{i+1}= 0,$ D digitos del centro
5. repetir el paso 4 hasta obtener los $n$ números $r_i$ deseados

***nota:*** *si no es posible obtener los $D$ digitos del centro del número $y_i$ agregue ceros a la izquierda del mismo*
> Ejemplo
>
>Generar números aleatorios $r_i$ a partir de las semillas $x_o=5015; x_1 = 5734; D = 4$
>
> [Solución](/primer%20parcial/ejemplos/medium_product.py)

### Algoritmo del multiplicador constante
1. Seleccionar una semilla $(X_0)$ con $D$ dígitos ($D>3$)
2. Seleccionar una constante $a$ con $D $ digitos ($D>3$)
3. Sea $y_0 = a * x_0$; sea $x_1=$ los $D$ digitos del centro y $r_i= 0,D$ digitos del centro.
4. sea $y_i= a * x_{i}$; sea $x_{i+1} = $ los $D$ digitos del centro y sea $r_{i+1} = 0, D$ digitos del centro
5. repetir el paso 4 hasta obtener $n$ números $r_i$ deseados.   

>Ejemplo
>
>Generar los números aleatorios a partir de $x_0=9803; a=6965; D = 4$
>
>[Solución](/primer%20parcial/ejemplos/constant_multiplier.py) *este ejemplo no contempla el caso de añadir ceros

----
## pruebas estadísticas
### Prueba de bondad de ajuste
1. Se plantea la hipotesis nula 
$$H_0 = x\sim F(x;\theta)$$

-----
$H_0: X \sim(\mu \sigma^2$)$


$H_1:X\neq N (\mu \sigma^2)$


# add exercise  
### Ejemplo distribución exponencial
Sea $x$=tiempo que tarda en programar (minutos)


|X    |$n_i$|marca de clase ($\frac{L_s+L_i}{2}$)|
|-----|-----|:----------------------------------:|
|10-15|30   |               12,5                 |
|15-20|25   |               17,5                 |
|20-25|22   |               22,5                 |
|25-30|18   |               27,5                 |
|30-35|19   |               32,5                 |
|35-40|12   |               37,5                 |
|40-45|8    |               47,5                 |
|**Total**|**134**|

Se pide probar:

$H_0:X\sim exp(1/\lambda)$

$H_1: X\neq exp(1/\lambda)$

Hallamos el estadístico

$X_c^2=\frac{\sum(n_{i0}-n_{ie})^2}{n_{ie}}$

$n_{ie}=nP(X=x)$

Para el primer $n$ esperado
$n_{1e}=134P(10\leq x\leq 15)$

La función para la distribucion exponencial es:

$f(x)=\frac{1}{\lambda}e^{-\lambda x}$

$\lambda = ? \rArr E(x)=\bar{x} \rArr \lambda=\bar{x}$

|X    |$n_i$|marca de clase ($\frac{L_s+L_i}{2}$)|$X_in_i$|
|-----|-----|:----------------------------------:|----|
|10-15|30   |               12,5                 |375|
|15-20|25   |               17,5                 |...|
|20-25|22   |               22,5                 |...|
|25-30|18   |               27,5                 |...|
|30-35|19   |               32,5                 |...|
|35-40|12   |               37,5                 |...|
|40-45|8    |               47,5                 |340|
|**Total**|**134**|-----|3210|

$\bar{x}=\frac{3210}{134} = 23,96$

$$n_{ie}= 134\int_{10}^{15} \frac{1}{\lambda}e^{-\frac{x}{\lambda}}dx$$

$$n_{ie}= 134[\frac{1}{23,96}(-\frac{1}{\frac{1}{23,96}}e^{\frac{x}{23,96}})]$$

$$134[-e^{\frac{-15}{23,96}}+e^{\frac-{10}{23,96}}]$$

$$=143[0,543+0,6588] \rArr n_{1e}=16,60$$ 


*para los n esperados*

se Halla: $X_{k-r-1}^2, 1 - \alpha$
> Tarea: Definir sistemas, cómo se clasifan, qué es un modelo (modelo matemático vs estadístico y qué tipos de modelos existen)


