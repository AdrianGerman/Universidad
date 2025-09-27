ar1 = int(input("Ingrese el precio del articulo 1 "))
ar2 = int(input("Ingrese el precio del articulo 2: "))
ar3 = int(input("Ingrese el precio del articulo 3: "))
ar4 = int(input("Ingrese el precio del articulo  4: "))
ar5 = int(input("Ingrese el precio del articulo 5: "))

totalVenta = ar1 + ar2 + ar3 + ar4 + ar5
impuesto = float (ar1 * .7 + ar2 * .7 + ar3 * .7 + ar4 * .7 + ar5 * .7)
total = totalVenta + impuesto


print ("El subtotal de la venta es:",totalVenta)

print("El impuesto de la venta es:",impuesto)

print("El total de la venta es:",total) 


