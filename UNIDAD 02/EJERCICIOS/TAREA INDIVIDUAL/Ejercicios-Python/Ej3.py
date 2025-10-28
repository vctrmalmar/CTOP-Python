comprobar = True
cadena = ""
contador = 0

while (comprobar):
    try:
        palabra = input("Introduce una palabra: ")
        if palabra == "Basta" or palabra == "":
            comprobar = False
        cadena += palabra
        contador += 1
    except:
        print("Error, introduce una palabra válida")

print("La cadena formada es: ", cadena)
print(f"Has soportado un total de {contador} preguntas")
