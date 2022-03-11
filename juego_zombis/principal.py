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


numero = ""
while numero not in ("1", "2", "3", "4"):
    numero = input("  Número de jugadores (1/4): ")

jugadores = []
for i in range(1, int(numero)+1):
    nombre = input("  Nombre del " + str(i) + "º jugador: ").capitalize()
    jugador = Persona(nombre)
    jugadores.append(jugador)


horda = []

for i in range(10):
    z = Zombi()
    horda.append(z)


while True:
    os.system("clear")
 
    print("  NOMBRE    -   CALLE   -   ENERGÍA")
    print("  ---------------------------------")
    for jugador in jugadores:
        nom, cal, ene = jugador.situacion()
        print("  {:8}  -    {:2}     -     {:2}".format(nom, cal, ene))
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

    
    ganadores = []
    for jugador in jugadores:
        if jugador.calle > 40:
            ganadores.append(jugador)
    if len(ganadores) >0:
        for jugador in ganadores:
            print("  {}, has escapado de los zombis.".format(jugador.nombre))
        print("  Has/Han ganado la partida.")
        print()
        break
# ---------------AQUÍ ME QUEDE, MINUTO 3:40 VÍDEO 5
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