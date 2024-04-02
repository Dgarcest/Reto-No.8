# Reto-No.8

## 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
for i in range(101): #el ciclo va hasta el numero 100
    cuadrado = i*i #variable cuadrado de cada iteracion
    print(f"El numero es {i}, y su cuadrado {cuadrado}")
```

## 2.  Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

```python 
for i in range(1, 1000, 2): #el ciclo va hasta 999 y va de 2 en 2
    print(f"numero impar: {i}")

print("Fin lista numeros impares") #separación 

for i in range(2, 1001, 2): #el ciclo va hasta 1000 y va de 2 en 2
    print(f"número par {i}")

print("Fin lista numeros pares") #separación
```

## 3.  Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

```python
n=int(input("Escriba su número: ")) #se pide el dato

if n%2 == 0: #cuando n es par
    for i in range(n, 1, -2): #el ciclo comienza en n y va disminuyendo 2 en cada iteracion
        print(i)

else: #cuando n es impar
    for i in range(n-1, 1, -2): #el ciclo comienza en n-1 y va disminuyendo 2 en cada iteracion
        print(i)
```

## 4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

```python
n = int(input("Introduzca el número: ")) #se le pide al usuario el dato

p = 1 #se declara una variable que va a ser la base para sacar el factorial en cada iteracion

for i in range (1, n+1): #lista de 1 hasta n
    p = p*i #la variable declarada p, se multiplica por i para sacar el factorial
    print(f"el numero es {i} y su factorial: {p}")
```

## 5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.

```python
n = int(input("Ingrese la potencia: "))

p = 1 #valor inicial de 2 elevado a la potencia

for i in range (n): #va a tener n iteraciones
    p *= 2 #se multiplica 2 en cada iteracion

print(f"El valor de 2 elevado a la potencia {n} es: {p}") #se imprime el mensaje
```

## 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. **Disclaimer:** Trate de no utilizar el operador de potencia (**).

```python
#se piden las 2 variables
n = int(input("Ingrese un numero natural: "))
x = float(input("Ingrese un numero real: "))
p = x 

for i in range(1, n): #lista desde 1 hasta n-1 (va a tener n-1 iteraciones)
    p = p*x #en cada iteracion se va a multiplica p(que es x) por si misma

print(f"El valor de {x}^{n} es de {p}") 
```

## 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

```python
f = 1 #variable de las tablas

for i in range(1, 10): #ciclo de todas las tablas 
    for i in range(1, 11): #ciclo de cada una de las tablas
        n = f*i #f es la tabla en la que va, y i es el numero por el que se multiplica
        print(f"{f} x {i} = {n}")
    f += 1 #cuando sale del ciclo de una tabla se suma 1 a f para que vaya a la siguiente y asi sucesivamente
```

## 8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
$$e^x \approx exp(x,n) \approx \sum_{i=0}^{n}\frac{x^i}{i!}$$

```python
"""
8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie 
de Maclaurin. **Nota:** use *math* para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
"""

import math

def exponencial(x, n): #funcion para obtener el valor aproximado con la serie de Maclaurin
    valor = 0
    p = 1
    aproximacion = 0

    for i in range(n+1): #ciclo que es la serie

        p = p*i #factorial de i

        if p == 0: #if para que no salte error por la division por cero, y que en la aproximacion no falte la suma cuando i=0
            p = 1

        valor = (x**i)/(p)

        aproximacion += valor

    return aproximacion #al final la funcion retorna el resultado del ciclo (la aproximacion)


if __name__ == "__main__":
    #se ingresa x y teniendo en cuenta que n va a ser 10 por defecto
    x = float(input("Ingrese cualquier valor real para la aproximacion de la funcion exponencial con la serie de Maclaurin (con 10 terminos): "))
    #se llama a la funcion para el aproximado y se declara el valor real con el import math, math.exp(x)
    aprox = exponencial(x, 10)
    real = math.exp(x)
    print(f"La aproximacion con la serie de Maclaurin es {aprox} y el valor real es {real}")
    error = ((math.fabs(aprox - real))/real)*100 #formula de porcentaje de error
    print(f"El porcentaje de error es: {error}%")

    n = 10 #n va a ser inicialmente 10 (el n por defecto) y va a aumentar de 1 en 1 hasta el n con el porcentaje adecuado
    while error > 0.1: #si el porcentaje de error es mayor a 0.1 entonces el ciclo se va a repetir hasta que encuentre un n en el que el porcentaje sea menor a 0.1
        aprox = exponencial(x, n) #se llama a la misma funcion pero con el n alterado en cada iteracion
        if ((math.fabs(aprox - real))/real)*100 < 0.1: #cuando el % es menor a 0.1 se rompe el ciclo
            print(f"El numero de terminos o el valor de n con que el porcentaje de error es menor a 0.1 es {n}")
            break
        n += 1 #se suma 1 termino en cada iteracion

    n = 10 #n va a ser inicialmente 10 (el n por defecto) y va a disminuir de 1 en 1 hasta el n con el porcentaje adecuado
    while error < 0.1: #si el porcentaje de error es mucho menor a 0.1 entonces el ciclo se va a repetir hasta que encuentre un n en el que el porcentaje sea un poco mayor a 0.1
        aprox = exponencial(x, n) #se llama a la misma funcion pero con el n alterado en cada iteracion
        if ((math.fabs(aprox - real))/real)*100 > 0.1: #cuando el % es un poco mayor a 0.1 se rompe el ciclo
            print(f"El numero de terminos o el valor de n con que el porcentaje de error es menor a 0.1 es {n}")
            break
        n -= 1
```

## 9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$

```python
```

## 10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
$$arctan(x) \approx arctan(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)}$$

```python
```

## **Disclaimer:** Para las aproximaciones de series determine con que valor n se obtiene menos del 0.1% de error.
