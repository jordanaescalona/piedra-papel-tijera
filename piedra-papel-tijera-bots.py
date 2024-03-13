import time
import random

#Puntajes
puntajePc1 = 0
puntajePc2 = 0

while True:
    computadora1 = random.randint(1,3)
    computadora2 = random.randint(1,3)

    if computadora1 == 1:
        computadora1 = "piedra"
    elif computadora1 == 2:
        computadora1 = "papel"
    else:
        computadora1 = "tijera"

    if computadora2 == 1:
        computadora2 = "piedra"
    elif computadora2 == 2:
        computadora2 = "papel"
    else:
        computadora2 = "tijera"

    #c1 piedra - tijera
    #c1 papel - piedra
    #c1 tijera - papel
    if computadora1 == computadora2:
        print("Empate")
    elif computadora1 == "piedra" and computadora2 == "tijera":
        print("El bot 1 gano!!")
        puntajePc1 = puntajePc1 + 1
    elif  computadora1 == "papel" and computadora2 == "piedra":
        print("El bot 1 gano!!")
        puntajePc1 = puntajePc1 + 1
    elif computadora1 == "tijera" and computadora2 == "papel":
        print("El bot 1 gano!!")
        puntajePc1 = puntajePc1 + 1
    else:
        print("El bot 2 gano!!")
        puntajePc2 = puntajePc2 + 1
    print("Puntaje bot1:",puntajePc1,"\nPuntaje bot2:",puntajePc2)
    
    time.sleep(3)
    
