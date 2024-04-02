#5. Calcular el valor de 2 elevado a la potencia n usando ciclos for

n = int(input("Ingrese la potencia: "))

p = 1 #valor inicial de 2 elevado a la potencia

for i in range (n): #va a tener n iteraciones
    p *= 2 #se multiplica 2 en cada iteracion

print(f"El valor de 2 elevado a la potencia {n} es: {p}") #se imprime el mensaje