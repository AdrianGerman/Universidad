print("-----Suma de las primeras N potencias de 2-----")
num = int(input("Ingrese el número 10 (o otro número) (y el -1 para salir): "))
suma = 0.0
i = 0
while num != -1:
    i += 1
    suma += 2**i
    if i == num:
        print("El resultado de la suma de las",num,"potencias de 2 es:",suma)
        num = int(input("Ingrese el número 10 (o otro número) (y el -1 para salir): "))
        i = 0
        suma = 0