"""
10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos 
de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
"""

import math

def arctan_aproximacion(x, n): #funcion para calcular una aproximación de la función arcotangente
    suma_serie = 0 #variable serie Maclaurin
    for i in range(n+1): #ciclo de 0 hasta n terminos
        operacion : float = ((-1)**i)*((x)**(2*i+1)/(2*i+1)) #operacion de la aproximacion
        suma_serie += operacion 
    return suma_serie #devuelve la suma total de los terminos

if __name__ == "__main__": 
    x = float(input("Ingrese cualquier valor en el rango [-1, 1] para la aproximacion de la funcion arcotangente con la serie de Maclaurin (con 10 terminos): "))
    while x>1 or x<-1: #si el valor de x no esta en el rango de [-1, 1] va a seguir pidiendo el dato hasta que este correcto
        print("Escriba un valor que este en el rango de [-1, 1]")
        x = float(input("Ingrese cualquier valor en el rango [-1, 1] para la aproximacion de la funcion arcotangente con la serie de Maclaurin (con 10 terminos): "))
    aproximacion = arctan_aproximacion(x, 10)
    valor_real = math.atan(x)
    print(f"La aproximacion de la funcion arcotangente con la serie de Maclaurin es {aproximacion} y el valor real es {valor_real}")
    error = math.fabs(((math.fabs(aproximacion - valor_real))/valor_real)*100) #formula de porcentaje de error
    print(f"El porcentaje de error es: {error}%")
        
    n = 10 #n va a ser inicialmente 10 (el n por defecto) y va a aumentar de 1 en 1 hasta el n con el porcentaje adecuado
    while error > 0.1: #si el porcentaje de error es mayor a 0.1 entonces el ciclo se va a repetir hasta que encuentre un n en el que el porcentaje sea menor a 0.1
        aproximacion = arctan_aproximacion(x, n) #se llama a la misma funcion pero con el n alterado en cada iteracion
        if (math.fabs((math.fabs(aproximacion - valor_real))/valor_real)*100) < 0.1: #cuando el % es menor a 0.1 se rompe el ciclo
            print(f"El numero de terminos o el valor de n con que el porcentaje de error es menor a 0.1 es {n}")
            break
        n += 1 #se suma 1 termino en cada iteracion

    n = 10 #n va a ser inicialmente 10 (el n por defecto) y va a disminuir de 1 en 1 hasta el n con el porcentaje adecuado
    while error < 0.1: #si el porcentaje de error es mucho menor a 0.1 entonces el ciclo se va a repetir hasta que encuentre un n en el que el porcentaje sea un poco mayor a 0.1
        aproximacion = arctan_aproximacion(x, n) #se llama a la misma funcion pero con el n alterado en cada iteracion
        if (math.fabs((math.fabs(aproximacion - valor_real))/valor_real)*100) > 0.1: #cuando el % es un poco mayor a 0.1 se rompe el ciclo
            print(f"El numero de terminos o el valor de n con que el porcentaje de error es menor a 0.1 es {n}")
            break
        n -= 1