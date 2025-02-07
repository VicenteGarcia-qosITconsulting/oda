import random

# Generar un número aleatorio entre 1 y 20
numero_secreto = random.randint(1, 20)

# Definir el número máximo de intentos
MAX_INTENTOS = 5
intentos = 0

print("¡Bienvenido al juego de adivinanza!")
print(f"Tienes {MAX_INTENTOS} intentos para adivinar un número entre 1 y 20")

# Bucle principal del juego
while intentos < MAX_INTENTOS:
    intentos += 1
    numero_usuario = input(f"\nIntento {intentos}. Introduce un número: ")
    
    # Verificar si la entrada es un número entero
    if not numero_usuario.isdigit():
        print("Por favor, introduce un número válido")
        intentos -= 1  # No contar intentos inválidos
        continue
    
    numero_usuario = int(numero_usuario)
    
    # Verificar si el número está en el rango correcto
    if numero_usuario < 1 or numero_usuario > 20:
        print("El número debe estar entre 1 y 20")
        continue
    
    # Comprobar si ha adivinado
    if numero_usuario == numero_secreto:
        print(f"¡Felicitaciones! ¡Has adivinado el número en {intentos} intentos!")
        break
    # Dar pistas
    elif numero_usuario < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")
    
    # Mostrar intentos restantes
    if intentos < MAX_INTENTOS:
        print(f"Te quedan {MAX_INTENTOS - intentos} intentos")

# Si se acabaron los intentos sin adivinar
if intentos == MAX_INTENTOS and numero_usuario != numero_secreto:
    print(f"\n¡Se acabaron los intentos! El número era {numero_secreto}")
