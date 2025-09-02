# 🎲 Juego: Adivina el Número

Este es un juego sencillo en Python en el que el programa piensa un número secreto al azar entre **1 y 100**, y el jugador tiene **8 intentos** para adivinarlo.

---

## 🚀 Cómo funciona

1. El programa genera un número aleatorio entre 1 y 100.
2. El jugador ingresa su nombre y comienza a adivinar.
3. El programa indica si el número secreto es **mayor** o **menor** al número ingresado.
4. El jugador tiene **8 intentos** como máximo.
5. El juego termina cuando:
   - ✅ El jugador adivina el número, mostrando en cuántos intentos lo logró.
   - ❌ Se acaban los intentos, mostrando cuál era el número secreto.

---

## 📂 Código principal

python
from random import randint

numero = randint(1, 101)
nombre = input("Cual es tu nombre: ")
print(f"{nombre} he pensado un numero del 1 al 100 y tienes 8 intentos para adivinarlo ")
intentos = 0

while intentos <= 7:  # 8 intentos
    numero_a_adiv = int(input("Ingrese un numero a adivinar: "))
    if (numero_a_adiv < 0) or (numero_a_adiv > 100):
        print("No es un numero valido. Por favor ingresar un numero valido")
        continue  # no contar este intento
    intentos += 1
    if numero_a_adiv == numero:
        print(f"Has adivinado el numero, el numero era {numero}, Felicitaciones {nombre}, lo has logrado en {intentos} intentos")
        break
    elif numero_a_adiv > numero:
        print("Incorrecto, el numero es menor")
    elif numero_a_adiv < numero:
        print("Incorrecto, el numero es mayor")

# Si se gastan los 8 intentos sin adivinar
if numero_a_adiv != numero:
    print(f"😢 Te quedaste sin intentos. El número era {numero}.")
    
▶️ Ejecución
Para ejecutar el juego en tu terminal:

bash
Copy code
python adivina_el_numero.py

📌 Notas
Si el jugador ingresa un número fuera del rango 1 a 100, ese intento no se cuenta.

El juego es ideal para practicar estructuras de control, bucles y manejo de condiciones en Python.
