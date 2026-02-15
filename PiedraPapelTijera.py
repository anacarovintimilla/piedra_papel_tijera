#Creaccion de variable aleatoria para computador
import random
opciones = ["piedra", "papel", "tijera"]
SeleccionComputador = random.choice(opciones)
marcadorUsuario = 0
marcadorCompuatador = 0 


#Ciclo de 3 partidas seguidas 

for i in range(3): 
       
    #Creacion de variable del ingreso de usuario 
    SeleccionUsuario = input("Escoge entre piedra, papel o tijera: ")
    print("Computador: " + SeleccionComputador)

    #Comparacion si la seleccion de usuaurio y computador es igual
    if SeleccionUsuario == SeleccionComputador:
        print("Es un empate")
    
    #Comparacion eleccion usuario es tijera
    if SeleccionUsuario == "tijera" and SeleccionComputador == "piedra":
        print("Perdiste")
        marcadorCompuatador += 1
    elif SeleccionUsuario == "tijera" and SeleccionComputador == "papel" :
        print("Ganaste")
        marcadorUsuario += 1

    #Comparacion eleccion ususario es papel
    if SeleccionUsuario == "papel" and SeleccionComputador == "tijera":
        print("Perdiste")
        marcadorCompuatador += 1
    elif SeleccionUsuario == "papel" and SeleccionComputador == "piedra" :
        print("Ganaste!")
        marcadorUsuario += 1

    #Comparacion eleccion usuario es piedra
    if SeleccionUsuario == "piedra" and SeleccionComputador == "tijera":
        print("Ganaste!")
        marcadorUsuario += 1
    elif SeleccionUsuario == "piedra" and SeleccionComputador == "papel":
        print("Perdiste")
        marcadorCompuatador += 1

print("Juego terminado")
print("Usuario vs Computador: ", marcadorUsuario , marcadorCompuatador) 