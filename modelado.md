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
> Se pide generar números aleatorios cuando $$ a = 5, c = 7,  X_0,  m=8$$
[Ejemplo](./test.py)
***Periodo n significa que cada n números la secuencia se va repitiendo.***

Existe la necesidad de establecer algunas reglas que pueden ser utilizadas en la selección de los valores de los parámetros para que el generador resultante tenga periodo completo, algunas de estas reglas se mencionan a continuación:
#### Selección de m 
Existen 2 opciones para seleccionar el valor apropiado de m:
1. Seleccionar *m* de modo que sea el número primo más grande posible y que a su vez sea menor que $$P^d$$ donde p es la base del sistema (binario, decimal, etc.) que se está utilizando y d es el númeo de bits.
2. Seleccionar *m* como $$ P^d$$   
> Ejemplo 
> Se pide generar números aleatorios:
> $$ c = 89; x_0 = 5; m = 10^2; a= 81$$
[Ejemplo](./test.py)


> Tarea: Definir sistemas, cómo se clasifan, qué es un modelo (modelo matemático vs estadístico y qué tipos de modelos existen)

