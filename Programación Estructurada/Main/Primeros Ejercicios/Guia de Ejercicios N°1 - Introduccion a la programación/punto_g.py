valores = float(input("Ingrese el valor a calcular: "))
porcentaje = float(input("Ingrese el porcentaje a calcular: "))

por = porcentaje/100
resultado = valores * por

print (f"El {porcentaje}% de {valores} es: ", resultado)