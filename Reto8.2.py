#2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
    
for i in range(1, 1000, 2): #el ciclo va hasta 999 y va de 2 en 2
    print(f"numero impar: {i}")

print("Fin lista numeros impares") #separación 

for i in range(2, 1001, 2): #el ciclo va hasta 1000 y va de 2 en 2
    print(f"número par {i}")

print("Fin lista numeros pares") #separación