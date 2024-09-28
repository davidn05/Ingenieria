
import time

segundos = int(input("Ingrese los segundos para la cuenta regresiva: "))

while segundos > 0:
    tiempo_restante = f'{segundos:02d}' #-string
    print(tiempo_restante, end = "\r")
    time.sleep(1)
    segundos -= 1
print("Felíz Año Nuevo!!!")

