# Inicializar variables para almacenar el mejor tiempo y el número de vehículo
mejor_tiempo = float('inf')  # Inicialmente, el mejor tiempo es infinito para asegurarse de que cualquier tiempo ingresado sea menor
mejor_vehiculo = None  # Variable para almacenar el número del vehículo con el mejor tiempo

# Bucle para procesar los 12 competidores
for i in range(12):
    # Solicitar ingreso de datos para cada competidor
    numero_vehiculo = int(input("Ingrese el número del vehículo: "))
    tiempo = float(input("Ingrese el tiempo (en segundos) del vehículo {}: ".format(numero_vehiculo)))

    # Comparar el tiempo ingresado con el mejor tiempo registrado
    if tiempo < mejor_tiempo:
        mejor_tiempo = tiempo  # Actualizar el mejor tiempo
        mejor_vehiculo = numero_vehiculo  # Actualizar el número del vehículo con el mejor tiempo

# Mostrar el resultado final
print("El vehículo con el mejor tiempo es el número {} con un tiempo de {} segundos.".format(mejor_vehiculo, mejor_tiempo))