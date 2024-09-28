dni = int(input("Ingrese DNI "))
categoria = int(input("Seleccione su categoría "))

maestranza = 23600
administracion = 35800
gerencia = 60420

if categoria == 0:
    maestranza_jubilacion = maestranza * 0.11
    maestranza_obra_social = maestranza * 0.03
    maestranza_neto = maestranza - maestranza_jubilacion - maestranza_obra_social
    print("DNI: ",dni)
    print("Categoría: ", categoria)
    print("Sueldo Neto: $", maestranza_neto)
if categoria == 1:
    administracion_jubilacion = administracion * 0.11
    administracion_obra_social = administracion * 0.03
    administracion_neto = administracion - administracion_jubilacion - administracion_obra_social
    print("DNI: ",dni)
    print("Categoría: ", categoria)
    print("Sueldo Neto: $", administracion_neto)
if categoria == 2:
    gerengia_jubilacion = gerencia * 0.11
    gerenacia_obra_social = gerencia * 0.03
    gerencia_neto = gerencia - gerengia_jubilacion - gerenacia_obra_social
    print("DNI: ",dni)
    print("Categoría: ", categoria)
    print("Sueldo Neto: $", gerencia_neto)