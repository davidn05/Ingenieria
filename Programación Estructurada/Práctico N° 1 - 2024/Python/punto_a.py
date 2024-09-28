print("Opción 1: perímetro y área de un círculo dado su radio")
print("Opción 2: perímetro y área de un pentágono")
print("Opción 3: perímetro y área de un rectángulo")
print("")

op = int(input("Elija la opción de lo que desea calcular: "))

if op == 1:
    radio = float(input("Ingrese el radio del círculo: "))
    area = (radio**2) * 3.1415
    perimetro = radio * 6.2831
    print("El perímetro del círculo es: ", perimetro)
    print("El área del círculo es: ", area)

elif op == 2:
    longi = float(input("Ingrese la longitud de un lado del pentágono: "))
    perimetro = longi * 5
    area = (5*longi**2)/(4*0.010966)
    print("El perímetro del pentágono es de: ", perimetro)
    print("El área del pentágono es de: ", area)

elif op == 3:
    longi1 = float(input("Ingrese la longitud del lado más grande del rectángulo: "))
    longi = float(input("Ingrese la longitud del lado más pequeño del rectángulo: "))
    perimetro = 2 * (longi1 + longi)
    area = longi * longi1
    print("El perímetro del rectángulo es de: ", perimetro)
    print("El área del rectángulo es de: ", area)
