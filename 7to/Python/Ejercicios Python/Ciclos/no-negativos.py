print("Este programa suma números no-negativos.")
print("Proporcione el valor -1 cuando no hay más datos.")
suma = 0.0

i = 0
dato = float(input("Proporcione un número, o el -1: "))

while dato >= 0.0:
    suma += dato
    i += 1
    dato = float(input("Proporcione un número, o el -1: "))
    
media = None if i == 0 else (suma / i)
print("La media de los datos es: ", media, ".", sep="")
