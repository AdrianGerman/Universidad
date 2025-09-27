acciones = int (2000)
accionesValor = int (40)
totalPagado = acciones * accionesValor
comision = totalPagado * .3

ventaAcciones = float(42.75)
totalVenta = acciones * ventaAcciones
comisionVenta = totalVenta * .3

total= (totalVenta - totalPagado - comision - comisionVenta)

print ("Joe pago por las acciones:",totalPagado)
print("Cantidad de comisión que Joe le pagó a su corredor cuando compró las acciones",comision)
print ("Cantidad por la que Joe vendió las acciones",totalVenta)
print ("Cantidad de comisión que Joe le pagó a su corredor cuando vendió las acciones",comisionVenta)
print("El dinero que le quedo a Joe es de:",total)
