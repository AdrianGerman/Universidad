print("-----Suma de un número consigo mismo 100 veces-----")
num = float(input("Ingrese un número positivo(o el -1 para salir): "))
suma = 0.0
i = 0
while num != -1:
    suma += num
    i += 1
    if i == 100:
        print("Suma de un número consigo mismo 100 veces:",suma)
        num = float(input("Ingrese un número positivo(o el -1 para salir): "))
        i = 0
        suma = 0