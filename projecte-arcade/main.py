import jocs

def mostrar_menu ():

    print ("Benvingut/da a l'Arcade")
    print ("1. Jugar a Pedra, Paper, Tisora")
    print ("2. Jugar a Endevinar el Número")
    print ("s. Sortir")

def main ():
    
    while True:

        mostrar_menu ()
        
        opcio = input("Introdueix la teva opció: ")
        
        if opcio == 's':
            print ("Gràcies per jugar.")
            break 
            
        elif opcio == '1':
            jocs.janken ()
            
        elif opcio == '2':
            jocs.nana ()
            
        else:
            print ("Opció incorrecta. Selecciona 1, 2 o s.")

if __name__ == "__main__":
    main()