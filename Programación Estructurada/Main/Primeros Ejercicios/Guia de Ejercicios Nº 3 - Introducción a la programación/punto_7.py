# Inicialización de variables
total_tenis = 0
total_futbol = 0
edad_tenis = 0
edad_futbol = 0
total_socios = 0

# Otras variables para almacenar datos de otros deportes
total_rugby = 0
edad_rugby = 0
total_voley = 0
edad_voley = 0
total_hockey = 0
edad_hockey = 0

# Bucle para procesar los datos de los socios
while True:
    # Solicitar ingreso de datos para cada socio
    numero_socio = input("Ingrese el número de socio (o 'fin' para terminar): ")
    if numero_socio.lower() == 'fin':
        break
    
    edad = int(input("Ingrese la edad del socio {}: ".format(numero_socio)))
    deporte = int(input("Ingrese el tipo de deporte que practica (1 tenis, 2 rugby, 3 voley, 4 hockey, 5 futbol): "))

    total_socios += 1  # Incrementar contador de socios

    # Contar y acumular edades según el deporte practicado
    if deporte == 1:
        total_tenis += 1
        edad_tenis += edad
    elif deporte == 2:
        total_rugby += 1
        edad_rugby += edad
    elif deporte == 3:
        total_voley += 1
        edad_voley += edad
    elif deporte == 4:
        total_hockey += 1
        edad_hockey += edad
    elif deporte == 5:
        total_futbol += 1
        edad_futbol += edad

# Calcular promedios de edad para cada deporte
promedio_edad_tenis = edad_tenis / total_tenis if total_tenis > 0 else 0
promedio_edad_futbol = edad_futbol / total_futbol if total_futbol > 0 else 0
promedio_edad_rugby = edad_rugby / total_rugby if total_rugby > 0 else 0
promedio_edad_voley = edad_voley / total_voley if total_voley > 0 else 0
promedio_edad_hockey = edad_hockey / total_hockey if total_hockey > 0 else 0

# Mostrar resultados
print("Cantidad de socios que practican tenis:", total_tenis)
print("Cantidad de socios que practican fútbol:", total_futbol)
print("Promedio de edad de jugadores de tenis:", promedio_edad_tenis)
print("Promedio de edad de jugadores de fútbol:", promedio_edad_futbol)
print("Promedio de edad de jugadores de rugby:", promedio_edad_rugby)
print("Promedio de edad de jugadores de voley:", promedio_edad_voley)
print("Promedio de edad de jugadores de hockey:", promedio_edad_hockey)
