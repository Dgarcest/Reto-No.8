"""
# 9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos 
de la serie de Maclaurin. **Nota:** use *math* para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
"""
import math

def serie(x, n): #funcion para calcular una aproximación de la función seno
    suma_total = 0 #variable de la suma de cada iteracion (de cada i en la serie)

    for i in range(0, n+1): #ciclo en el que cada iteracion es cada i en la serie
        #estas 2 variables son para calcular el factorial de 2*i+1
        k = 2*i + 1
        p = 1
        for j in range(1, k): #ciclo para calcular el factorial de k
            p = p*j
        total = p*k #este es el factorial de 2*i+1
        operacion = ((-1)**i)*(((x)**(2*i+1))/(total))
        suma_total += operacion
    return suma_total

if __name__ == "__main__":
    x = float(input("Ingrese cualquier valor real para la aproximacion de la funcion seno con la serie de Maclaurin (con 10 terminos): "))
    aproximacion = serie(x, 10)
    real = math.sin(x)
    print(f"La aproximacion de la funcion seno con la serie de Maclaurin es {aproximacion} y el valor real es {real}")
    error = math.fabs(((math.fabs(aproximacion - real))/real)*100) #formula de porcentaje de error (con un valor absoluto adicional porque a veces el "real" es negativo)
    print(f"El porcentaje de error es: {error}%")

    n = 10 #n va a ser inicialmente 10 (el n por defecto) y va a aumentar de 1 en 1 hasta el n con el porcentaje adecuado
    while error > 0.1: #si el porcentaje de error es mayor a 0.1 entonces el ciclo se va a repetir hasta que encuentre un n en el que el porcentaje sea menor a 0.1
        aproximacion = serie(x, n) #se llama a la misma funcion pero con el n alterado en cada iteracion
        if (math.fabs((math.fabs(aproximacion - real))/real)*100) < 0.1: #cuando el % es menor a 0.1 se rompe el ciclo
            print(f"El numero de terminos o el valor de n con que el porcentaje de error es menor a 0.1 es {n}")
            break
        n += 1 #se suma 1 termino en cada iteracion

    n = 10 #n va a ser inicialmente 10 (el n por defecto) y va a disminuir de 1 en 1 hasta el n con el porcentaje adecuado
    while error < 0.1: #si el porcentaje de error es mucho menor a 0.1 entonces el ciclo se va a repetir hasta que encuentre un n en el que el porcentaje sea un poco mayor a 0.1
        aproximacion = serie(x, n) #se llama a la misma funcion pero con el n alterado en cada iteracion
        if (math.fabs((math.fabs(aproximacion - real))/real)*100) > 0.1: #cuando el % es un poco mayor a 0.1 se rompe el ciclo
            print(f"El numero de terminos o el valor de n con que el porcentaje de error es menor a 0.1 es {n}")
            break
        n -= 1