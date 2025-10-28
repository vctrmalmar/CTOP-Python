numero = int(input("Ingrese un numero entre 5 y 50: "))
if 5 <= numero <= 50:
    while numero > 0:
        print (numero)
        numero -= 1
else:
    print("El numero no esta en el rango solicitado")