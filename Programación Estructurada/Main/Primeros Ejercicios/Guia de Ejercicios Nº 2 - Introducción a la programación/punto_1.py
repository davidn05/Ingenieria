repositores = float(32235)
cajeros = float(38630.89)
supervisores = float(45560.20)

repositores_jubilacion = repositores * 0.11
repositores_obra_social = repositores * 0.03
repositores_bono = repositores * 0.08

repositores_neto = repositores - repositores_jubilacion - repositores_obra_social

cajeros_jubilacion = cajeros * 0.11
cajeros_obra_social = cajeros * 0.03

cajeros_neto = cajeros - cajeros_jubilacion - cajeros_obra_social

supervisores_jubilacion = supervisores * 0.11
supervisores_obra_social = supervisores * 0.03

supervisores_neto = supervisores - supervisores_jubilacion - supervisores_obra_social

print("Liquidación de Sueldos")

print("Repositores")
print("Sueldo Bruto: $", repositores)
print("Retenciones")
print("Jubilación: $", repositores_jubilacion)
print("Obra Social: $", repositores_obra_social)
print("Sueldo Neto: $", repositores_neto)
print("Adicionales")
print("Bono de Compra: $", repositores_bono)

print("Cajeros")
print("Sueldo Bruto: $", cajeros)
print("Retenciones")
print("Jubilación: $", cajeros_jubilacion)
print("Obra Social: $", cajeros_obra_social)
print("Sueldo Neto: $", cajeros_neto)

print("Supervisores")
print("Sueldo Bruto: $", supervisores)
print("Retenciones")
print("Jubilación: $", supervisores_jubilacion)
print("Obra Social: $", supervisores_obra_social)
print("Sueldo Neto: $", supervisores_neto)