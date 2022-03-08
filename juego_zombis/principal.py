from subprocess import CalledProcessError
from persona import Persona
from zombi import Zombi
import os


os.system("clear")


print()
print("  La ciudad se ha llenado de zombis.")
print("  Estás en la calle 1 y has de llegar")
print("  a la calle 40 para poder salvarte.")
print()
print("  Los zombis avanzan 1, 2 ó 3 calles.")
print("  Tú puedes avanzar 1, 2 ó 3 calles.")
print()
nombre = input("  ¿Estás preparado? Cual es tu nombre: ").capitalize()


jugador = Persona(nombre)


horda = []

for i in range(10):
    z = Zombi()
    horda.append(z)


while True:
    os.system("clear")

    print()
    print(jugador.situacion())
    print()

    calles = []
    for zombi in horda:
        calles.append(zombi.calle)
    calles.sort()
    print("Hay zombies en las calles: ")
    print()
    print("  ", end = "")
    for elemento in calles:
        print(elemento, end = " ")
    print()
    print()

    if jugador.calle > 40:
        print("  No te ha visto ningún zombi.")
        print("  Te has librado de ser comido.")
        print()
        break

    comido = False
    for zombi in horda:
        if zombi.calle == jugador.calle:
            comido = True
    if comido:
        print("  Un zombi te acaba de ver.")
        print("  Te va a comer. Se acabó el juego")
        print()
        break

    velocidad = ""
    while velocidad not in ("1", "2", "3"):
        velocidad = input("  Cuánto quieres correr (1/2/3): ")
    jugador.moverse(velocidad)
    
    for z in list(horda):
        z.moverse()
        if z.no_visible():
            horda.remove(z)