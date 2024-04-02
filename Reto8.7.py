# 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

f = 1 #variable de las tablas

for i in range(1, 10): #ciclo de todas las tablas 
    for i in range(1, 11): #ciclo de cada una de las tablas
        n = f*i #f es la tabla en la que va, y i es el numero por el que se multiplica
        print(f"{f} x {i} = {n}")
    f += 1 #cuando sale del ciclo de una tabla se suma 1 a f para que vaya a la siguiente y asi sucesivamente