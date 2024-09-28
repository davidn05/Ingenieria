# Solicitar al usuario ingresar un número entre 1 y 100
numero = int(input("Ingrese un número entre 1 y 100: "))

if 1 <= numero <= 100:
    if numero % 2 == 0:
        print (f"El número {numero} es par")
    else:
        print (f"El número {numero} es impar")
else: print ("El número ingresaro está fuera del rango")