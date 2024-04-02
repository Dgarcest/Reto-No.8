# 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

n=int(input("Escriba su número: ")) #se pide el dato

if n%2 == 0: #cuando n es par
    for i in range(n, 1, -2): #el ciclo comienza en n y va disminuyendo 2 en cada iteracion
        print(i)

else: #cuando n es impar
    for i in range(n-1, 1, -2): #el ciclo comienza en n-1 y va disminuyendo 2 en cada iteracion
        print(i)