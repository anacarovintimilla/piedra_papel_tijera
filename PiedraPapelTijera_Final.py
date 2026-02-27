#Llamado a la funcion random
import random

opciones = ["piedra", "papel", "tijera"]

# Función para validar jugada del usuario
def obtener_jugada_usuario():
    while True:
        jugada = input("Escoge entre piedra, papel o tijera: ").lower()
        if jugada in opciones:
            return jugada
        else:
            print("Entrada invalida. Escribe solo piedra, papel o tijera")

# Función para comparar jugadas
def comparar_jugadas(usuario, computadora):
    if usuario == computadora:
        return "empate"
    
    if (
        (usuario == "piedra" and computadora == "tijera") or
        (usuario == "papel" and computadora == "piedra") or
        (usuario == "tijera" and computadora == "papel")
    ):
        return "usuario"
    else:
        return "computadora"

# Preguntar cuántas rondas quiere jugar
rondas = int(input("¿Cuántas veces quieres jugar? "))

marcador_usuario = 0
marcador_computadora = 0

# Ciclo del juego
for i in range(rondas):
    print(f"Ronda {i+1}")
    
    usuario = obtener_jugada_usuario()
    computadora = random.choice(opciones)

    print("Computadora:", computadora)

    resultado = comparar_jugadas(usuario, computadora)

    if resultado == "empate":
        print("Es un empate")
    elif resultado == "usuario":
        print("¡Ganaste!")
        marcador_usuario += 1
    else:
        print("Perdiste")
        marcador_computadora += 1

print("Juego terminado")
print("Marcador final:")
print("Usuario:", marcador_usuario)
print("Computadora:", marcador_computadora)
