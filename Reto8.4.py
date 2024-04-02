#4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial

n = int(input("Introduzca el número: ")) #se le pide al usuario el dato

p = 1 #se declara una variable que va a ser la base para sacar el factorial en cada iteracion

for i in range (1, n+1): #lista de 1 hasta n
    p = p*i #la variable declarada p, se multiplica por i para sacar el factorial
    print(f"el numero es {i} y su factorial: {p}")