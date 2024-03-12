import time
import random

#Inicializamos variables para contar puntos
puntosJugador = 0
puntosComputadora = 0

while True:
    jugador = input("Ingrese piedra,papel o tijera:")

    if jugador == "piedra" or jugador == "papel" or jugador == "tijera":
        computadora = random.randint(1,3)

        if computadora == 1:
            computadora = "piedra"
        elif computadora == 2:
            computadora = "papel"
        else:
            computadora = "tijera"

        #papel - piedra
        #piedra - tijera
        #tijera - papel
        print("Piedra ....")
        time.sleep(1)
        print("Papel ...")
        time.sleep(1)
        print("Tijera ...")
        
        if jugador == computadora:
            print("Empate")
        elif jugador == "papel" and computadora == "piedra":
            print("Ganaste!")
            puntosJugador = puntosJugador + 1
        elif jugador == "piedra" and computadora == "tijera":
            print("Ganaste!")
            puntosJugador = puntosJugador + 1
        elif jugador == "tijera" and computadora == "papel":
            print("Ganaste!")
            puntosJugador = puntosJugador + 1
        else:
            print("Perdiste!")
            puntosComputadora = puntosComputadora + 1

        print("Puntos jugador:",puntosJugador,"\nPuntos Pc:",puntosComputadora)
        
    else:
        print("Debes ingresar una opción correcta (piedra,papel o tijera):")

