import random

opciones = ["PIEDRA", "PAPEL", "TIJERAS"]
secreto = random.choice(opciones)
victorias = 0
empates = 0
derrotas = 0

while True:
        usuario = input("Ingrese su elección (Piedra, Papel o Tijeras): ").upper()
        if usuario not in opciones:
            print("Ingrese una opción válida")
            continue
        
        if usuario == secreto:
              print("Empataste")
              empates += 1
              secreto = random.choice(opciones)

        elif (usuario == opciones[0] and secreto == opciones[1]) or \
            (usuario == opciones[1] and secreto == opciones[2]) or \
                (usuario == opciones[2] and secreto == opciones[1]):
            print("Ganaste")
            victorias += 1
            if victorias == 3:
                break

        else:
              print("Perdiste")
              derrotas += 1
              secreto = random.choice(opciones)

print(f"Llevas {victorias} enfrentamientos ganados, {derrotas} perdidos y {empates} empatados")
salir = input("Presiona Enter para salir")