librosCantidad = int (input ('Ingresa la cantidad de libros (2 a 5): '))

if librosCantidad > 2 and librosCantidad <= 5:
    i=0
    b=True
    librosPrecio = []
    while i <librosCantidad:
        i = i+1
        precio = float (input(f'Introduce el precio del libro {i} ($100.00 a $999.00): '))
        if precio >=100 and precio <= 999:
            librosPrecio.append(precio)
        else:
            precio = float (input ('El precio debe ser de $100.00 a $999.00'))
            b = False
            break
    j=0
    precioTotal = 0
    while j < librosCantidad and b==True:
        precioTotal = precioTotal + librosPrecio[j]
        j=j+1
    if b==True:
        precioTotalEnvio = precioTotal + 10 + j-1
        print ('El precio total mas envio es: ',precioTotalEnvio)
else:
    print ('Tiene que ingresar la cantidad de libros del 2 al 5')