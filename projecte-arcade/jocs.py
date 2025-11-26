import random
import robot 

def determinar_guanyador_ronda (jugador, maquina):

    if jugador == maquina:
        return "empat"
    
    # Regles per guanyar
    if (jugador == "pedra" and maquina == "tisora") or \
       (jugador == "paper" and maquina == "pedra") or \
       (jugador == "tisora" and maquina == "paper"):
        return "jugador"
    
    else:
        return "maquina"

#Joc 1: Pedra, Paper, Tisora
def janken ():

    print ("Pedra, Paper, Tisora")

    maquina_joc = robot.robot () 
    
    # 1. Triar mode de joc
    while True:

        mode = input ("(1: Primer a 3, 2: Millor de 5): ")

        if mode == '1':
            victories_max, rondes_max = 3, float ('inf')
            break

        elif mode == '2':
            victories_max, rondes_max = float ('inf'), 5
            break

        print ("Opció no vàlida.")

    puntuacio_jugador = 0
    puntuacio_maquina = 0
    ronda_actual = 0
    opcions_valides = ["pedra", "paper", "tisora"]

    # Bucle principal del joc
    while puntuacio_jugador < victories_max and puntuacio_maquina < victories_max and ronda_actual < rondes_max:
        ronda_actual += 1

        print (f"Ronda {ronda_actual} ({puntuacio_jugador}-{puntuacio_maquina})")
        
        # 2. Gestió d'entrada de l'usuari
        while True:
            jugada_usuari = input ("La teva jugada (pedra/paper/tisora): ")

            if jugada_usuari in opcions_valides:
                break

            print ("Jugada no vàlida.")
            
        jugada_maquina = maquina_joc.playing () 
        print (f"Robot: {jugada_maquina}")

        # 3. Comparar i actualitzar puntuacions
        guanyador = determinar_guanyador_ronda (jugada_usuari, jugada_maquina)
        
        if guanyador == "jugador":
            puntuacio_jugador += 1
            print ("Has guanyat la ronda!")

        elif guanyador == "maquina":
            puntuacio_maquina += 1
            print ("El robot ha guanyat la ronda.")

        else:
            print ("Empat.")
            
    # Anunciar el guanyador final del partit
    print ("Fi del Partit")
    
    if puntuacio_jugador == puntuacio_maquina:
        missatge = "Partida acabada en empat."

    elif puntuacio_jugador > puntuacio_maquina:
        missatge = f"Has guanyat la partida ({puntuacio_jugador}-{puntuacio_maquina})"

    else:
        missatge = f"El robot guanya la partida ({puntuacio_jugador}-{puntuacio_maquina})"
    
    print (missatge)

# Joc 2: Endevinar el Número del 1 al 100
def nana ():
    print ("Endevina el Número")

    numero_secret = random.randint (1, 100)
    intents = 0

    while True:
        intents += 1

        entrada_usuari = input ("Introdueix un número entre 1 i 100 (s per sortir): ")

        if entrada_usuari == 's':
            print ("Has decidit sortir del joc.")
            break

        try:
            numero_usuari = int(entrada_usuari) 

        except ValueError:
            print ("Entrada no vàlida. Introdueix un número.")
            continue

        if numero_usuari < 1 or numero_usuari > 100:
            print ("Número fora de rang. Torna-ho a intentar.")
            continue
            
        if numero_usuari < numero_secret:
            print ("Més alt.")

        elif numero_usuari > numero_secret:
            print ("Més baix.")

        else:
            print (f"Has endevinat el número {numero_secret} en {intents} intents.")
            break