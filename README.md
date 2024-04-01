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
    i += 1 #se le suma 1 a i en cada iteracion
```

## 5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.

```python
n = int(input("Ingrese la potencia: "))

p = 1 #valor inicial de 2 elevado a la potencia

for i in range (n): #va a tener n iteraciones
    p *= 2 #se multiplica 2 en cada iteracion
    i += 1 #se suma 1 a i

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
    i += 1 #se va a multiplicar una n-1 cantidad de veces

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
