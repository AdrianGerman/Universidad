print("-----Suma de los 20 primeros números enteros-----")
b = int(input("Ingrese 1 para comenzar (o cualquier otro número para salir): "))
i = 0
suma = 0.0
while i<20 and b == 1:
    i += 1
    suma += i
    if i == 20:
        print(suma)
        b = int(input("Ingrese 1 para repetir (o cualquier otro número para salir): "))
        i = 0
        suma = 0