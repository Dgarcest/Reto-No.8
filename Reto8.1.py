#1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

for i in range(101): #el ciclo va hasta el numero 100
    cuadrado = i*i #variable cuadrado de cada iteracion
    print(f"El numero es {i}, y su cuadrado {cuadrado}")