#6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**)

#se piden las 2 variables
n = int(input("Ingrese un numero natural: "))
x = float(input("Ingrese un numero real: "))
p = x 

for i in range(1, n): #lista desde 1 hasta n-1 (va a tener n-1 iteraciones)
    p = p*x #en cada iteracion se va a multiplica p(que es x) por si misma

print(f"El valor de {x}^{n} es de {p}") 