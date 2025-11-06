numeroDecimal = float(input("Ingrese un número decimal: "))
numeroEntero = int(numeroDecimal)
print("El número entero es:", numeroEntero)

numero = input("Escribe un numero: ")
try:
    total = int(numero) + 10
    print("El total es:", total)
except Exception:
    print("No has introducido un número válido.")
