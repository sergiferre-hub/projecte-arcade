# Arcade Python

Arcade és una petita aplicació de consola desenvolupada en Python que simula una màquina recreativa amb dos jocs: Pedra, Paper, Tisora amb 2 modes de ronda i endevinar el número del 1 al 100.

## Descripció del Projecte

Aquest projecte demostra la modularització i estructuració del codi en Python, dividint la lògica en tres mòduls:

* **main.py**: Conté el bucle principal** i el menú d'interacció amb l'usuari. És el punt d'entrada de l'aplicació.
* **jocs.py**: Conté la lògica de les funcions dels dos jocs.
* **robot.py**: Conté la classe que gestiona la lògica de l'oponent de la màquina.

## Jocs

### Joc 1: Pedra, Paper, Tisora

El joc te un bucle per gestionar les rondes i el comptador de puntuacions. Al començament, l'usuari ha de triar un dels dos modes de joc:

* El primer que arribi a 3 victòries.
* Al millor de 5 rondes.

### Joc 2: Endevinar el Número

L'aplicació genera un número aleatori (entre 1 i 100), i gestiona un bucle per demanar números a l'usuari, donar pistes ("Més alt," "Més baix") i compta els intents.

## Com Executar el Projecte

Per executar el Mini Arcade, necessites tenir Python instal·lat al teu sistema i executar main.py.