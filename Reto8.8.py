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
        n -= 1 #se resta 1 termino en cada iteracion