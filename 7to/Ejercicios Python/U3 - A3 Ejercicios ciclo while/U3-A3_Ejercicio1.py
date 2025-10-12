print("-----Tabla de multiplicar del número ingresado-----")
numero = int(input("Ingrese un número(o el -1 para salir): "))
i=0
while numero != -1:
    i+=1
    print(numero,"x",i,"=",numero*i)
    if i==10:
        numero = int(input("Ingrese un número(o el -1 para salir): "))
        i = 0
