print("-----Suma de los números pares entre el 1 y 50-----")
b = int(input("Ingrese 1 para comenzar (o cualquier otro número para salir): "))
i = 0
suma = 0.0
while i<50 and b == 1:
    i += 2
    suma += i
    if i == 50:
        print(suma)
        b = int(input("Ingrese 1 para repetir (o cualquier otro número para salir): "))
        i = 0
        suma = 0