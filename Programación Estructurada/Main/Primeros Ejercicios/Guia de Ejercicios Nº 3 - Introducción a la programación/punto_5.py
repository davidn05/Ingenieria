dni = int(input("Ingrese número de DNI "))
plan = int(input("Ingrese la cantidad de megas de su plan "))

megas_30 = 750
megas_50 = 1100
megas_100 = 1500

if plan == 30:
    print("DNI: ", dni)
    print("Servicio: Internet 30 megas")
    print("Costo final: $", megas_30)
if plan == 50:
    print("DNI: ", dni)
    print("Servicio: Internet 50 megas")
    print("Costo final: $", megas_50)
if plan == 100:
    print("DNI: ", dni)
    print("Servicio: Internet 100 megas")
    megas_descuento = megas_100 * 0.05
    megas_descuento_final = megas_100 - megas_descuento
    print("Costo final: $", megas_descuento_final)