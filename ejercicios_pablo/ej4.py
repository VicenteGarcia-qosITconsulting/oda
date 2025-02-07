# Definir usuario y contraseña predefinidos
USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "admin"

# Definir el número máximo de intentos
MAX_INTENTOS = 3
intentos = 0

# Bucle mientras no se supere el máximo de intentos
while intentos < MAX_INTENTOS:
    # Pedir datos al usuario
    usuario = input("Introduce tu usuario: ")
    contrasena = input("Introduce tu contraseña: ")
    
    # Verificar si los datos son correctos
    if usuario == USUARIO_CORRECTO and contrasena == CONTRASENA_CORRECTA:
        print("Acceso concedido")
        break  # Salir del bucle si los datos son correctos
    else:
        intentos += 1
        intentos_restantes = MAX_INTENTOS - intentos
        if intentos_restantes > 0:
            print(f"Acceso denegado. Te quedan {intentos_restantes} intentos")
        else:
            print("Acceso denegado. Has superado el número máximo de intentos")
