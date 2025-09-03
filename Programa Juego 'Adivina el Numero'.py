#Juego Adivina el numero
from random import *
numero_a_adiv = 0 #Para que no haya algun error por no estar definido
numero = randint(1,101)
nombre = input("Cual es tu nombre: ")
print(f"{nombre} he pensado un numero del 1 al 100 y tienes 8 intentos para adivinarlo ")
intentos = 0

while intentos <= 7: #8 intentos
    numero_a_adiv = int(input("Ingrese un numero a adivinar: "))
    if (numero_a_adiv < 0) or (numero_a_adiv > 100):
        print("No es un numero valido. Por favor ingresar un numero valido")
        continue #no contar este intento
    intentos += 1
    if numero_a_adiv == numero:
            print(f"Has adivinado el numero, el numero era {numero}, Felicitaciones {nombre}, lo has logrado en {intentos} intentos")
            break
    elif numero_a_adiv > numero:
            print(f"Incorrecto, el numero es menor")
    elif numero_a_adiv < numero:
            print(f"Incorrecto, el numero es mayor")
# Si se gastan los 8 intentos sin adivinar
if numero_a_adiv != numero:
    print(f" Te quedaste sin intentos. El número era {numero}.")
