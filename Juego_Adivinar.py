print("Bienvenido, YO, Luty te invito al juego de adivinar el numero de porotos que quiero")

import random

numero_a_adivinar = random.randint(1, 10)

contador_numero_intentos = 1

adivina = int(input("ingresa un número entre 1 y 10: "))

while numero_a_adivinar != adivina:
    print("número incorrecto")
    if contador_numero_intentos == 2:
        break
    elif adivina < numero_a_adivinar:
        print("tú numero de porotos fue menor que mi numero")
    else:
        print("tú numero de porotos fue mayor que mi numero")

    adivina = int(input("prueba de nuevo: "))
    contador_numero_intentos += 1

if numero_a_adivinar == adivina:
    print("Felicitaciones, has adivinado. Dame mis porotos y un chocolate")

else:
    print("Que huea¡¡¡, has perdido. Entrega la bolsa de porotos")


print("Adios")






