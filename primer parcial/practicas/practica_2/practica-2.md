# Práctica 2
> Sergio Guachalla
## Método congruencial linear
### Ejercicio 1: Se pide generar números aleatorios
Datos:
$$ c = 89; x_0 = 5; m = 10^2; a= 81 $$

*La formula para el método congruencial linear es:*
$$ x_{i+1} = (ax_i + c) \mod m $$

Para n números aleatorios:
|n|$X_n$|
|--|----|
|0|5|
|1|$(81×5+89)mod100=94$|
|2|$(81×94+89)mod100=3$|
|3|$(81×3+89)mod100=32$|
|4|$(81×32+89)mod100=81$|
|5|$(81×81+89)mod100=50$|

## Método congruencial multiplicativo

### Ejercicio 1: 
Datos:
$$ c = 16; x_0 = 13; m = 10^8; a= 211 $$

$X_{n+1} = (8x_n +16) mod 10^8; x_0 = 13$
|1n|$X_n$|
|--|-----|
|0|13|
|1|$(211×13×16)mod10^8=0,13$|
|2|$(211×13×16)mod10^8=0,438$|
|3|$(211×43×16)mod10^8=0,48$|
|4|$(211×48×16)mod10^8=0,80$|
|5|$(211×80×16)mod10^8=0.35$|


## Algoritmo de cuadrados medios
Datos iniciales:
- Semilla: $X_0 = 9803$
- Constante: $a = 6965$
- Dígitos a considerar: $D = 4$
- Cantidad de números a generar: 5

## Cálculo de los números:

### Paso 1:
$$
Y_0 = a \times X_0 = 6965 \times 9803 = 68261895
$$
Tomamos los 4 dígitos centrales: **6189**  
Por lo tanto, $X_1 = 6189$ y $R_1 = 0.6189$

### Paso 2:
$$
Y_1 = a \times X_1 = 6965 \times 6189 = 43138785
$$
Tomamos los 4 dígitos centrales: **1387**  
Por lo tanto, $X_2 = 1387$ y $R_2 = 0.1387$

### Paso 3:
$$
Y_2 = a \times X_2 = 6965 \times 1387 = 9662355
$$
Tomamos los 4 dígitos centrales: **6235**  
Por lo tanto, $X_3 = 6235$ y $R_3 = 0.6235$

### Paso 4:
$$
Y_3 = a \times X_3 = 6965 \times 6235 = 43432175
$$
Tomamos los 4 dígitos centrales: **4321**  
Por lo tanto, $X_4 = 4321$ y $R_4 = 0.4321$

### Paso 5:
$$
Y_4 = a \times X_4 = 6965 \times 4321 = 30094765
$$
Tomamos los 4 dígitos centrales: **0947**  
Por lo tanto, $X_5 = 0947$ y $R_5 = 0.0947$

## Resultado Final:
Los 5 números generados son:
$$
R_1 = 0.6189, \quad R_2 = 0.1387, \quad R_3 = 0.6235, \quad R_4 = 0.4321, \quad R_5 = 0.0947
$$

