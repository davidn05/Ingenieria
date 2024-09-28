# Inicialización de variables
total_personas = 0
total_varones = 0
total_mujeres = 0
varones_entre_16_y_65 = 0
mayor_edad = -1  # Inicializar con un valor imposible para comparar edades
documento_mayor_edad = None
sexo_mayor_edad = None

# Bucle para procesar los datos de cada persona censada
while True:
    numero_documento = int(input("Ingrese el número de documento (0 para terminar): "))
    if numero_documento == 0:
        break
    
    edad = int(input("Ingrese la edad de la persona: "))
    sexo = input("Ingrese el sexo de la persona ('F' o 'M'): ").upper()

    total_personas += 1  # Contar total de personas censadas

    # Contar varones y mujeres
    if sexo == 'M':
        total_varones += 1
        if 16 <= edad <= 65:
            varones_entre_16_y_65 += 1
    elif sexo == 'F':
        total_mujeres += 1

    # Identificar a la persona con mayor edad
    if edad > mayor_edad:
        mayor_edad = edad
        documento_mayor_edad = numero_documento
        sexo_mayor_edad = sexo

# Calcular el porcentaje de varones entre 16 y 65 años respecto del total de varones
if total_varones > 0:
    porcentaje_varones_entre_16_y_65 = (varones_entre_16_y_65 / total_varones) * 100
else:
    porcentaje_varones_entre_16_y_65 = 0

# Mostrar los resultados
print("Cantidad total de personas censadas:", total_personas)
print("Cantidad total de varones censados:", total_varones)
print("Cantidad total de mujeres censadas:", total_mujeres)
print("Porcentaje de varones entre 16 y 65 años:", porcentaje_varones_entre_16_y_65, "%")

if documento_mayor_edad is not None:
    print("La persona con mayor edad tiene {} años, número de documento: {}, sexo: {}".format(mayor_edad, documento_mayor_edad, sexo_mayor_edad))
