MAX = 4
print("Este programa calcula la suma de", MAX, "números.")

suma = 0.0
i = 0
while i < MAX:
    i = i + 1
    número = float(input("Proporcione el dato " + str(i) + ": "))
    suma = suma + número
print("La suma es:", suma)
