peso_1 = float(input("Ingrese el peso (en Kg) del producto "))
precio_1 = float(input("Ingrese el precio del prodcuto "))
peso_2 = float(input("Ingrese el peso (en Kg) del producto "))
precio_2 = float(input("Ingrese el precio del prodcuto "))
peso_3 = float(input("Ingrese el peso (en Kg) del producto "))
precio_3 = float(input("Ingrese el precio del prodcuto "))

total_1 = peso_1 * precio_1
total_2 = peso_2 * precio_2
total_3 = peso_3 * precio_3

total_compra = total_1 + total_2 + total_3

#Le hice que el descuento se aplique a partir de los $1000 de importe, porque casi siempre se aplica el descuento
if total_compra > 1000:
    descuento = total_compra * 0.10
    total_descuento = total_compra - descuento
    print("Producto 1: $", total_1)
    print("Producto 2: $", total_2)
    print("Producto 3: $", total_3)

    print("Importe final: $", total_compra)

    print("Descuento del 10% aplicado")
    print("Importe final (descuentos aplicados): $", total_descuento)
else:
    print("Producto 1: $", total_1)
    print("Producto 2: $", total_2)
    print("Producto 3: $", total_3)

    print("Importe final: $", total_compra)