pedido = int(input("Ingrese la cantidad de productos "))

if pedido < 5:
    print("No se permiten compras inferiores a 5 productos")
elif 5 <= pedido <= 15:
    print("Costo de envío: $200")
else:
    print("Costo de envío: gratuito")
        