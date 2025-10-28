try :
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
except ValueError:
    print("Error: No has introducido un valor de tipo numérico")
    exit(1)

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print("Ambos numeros son iguales.")