def es_primo(numero):
    # Verificar si el número es divisible por algún número hasta su raíz cuadrada
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    
    # Si no encontró divisores, es primo
    return True

# Pedir número al usuario
numero = input("Introduce un número: ")

# Convertir la entrada a entero
if numero.isdigit():
    numero = int(numero)
    # Usar la función para verificar si es primo
    if es_primo(numero):
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")
else:
    print("Por favor, introduce un número entero válido")
