# Lista de vocales
vocales = ['a', 'e', 'i', 'o', 'u']

# Pedir la palabra
palabra = input("Introduce una palabra: ").lower()  # Convertir a minúsculas

# Inicializar el contador de vocales
contador = 0

# Recorrer cada letra de la palabra
for letra in palabra:
    # Si la letra está en la lista de vocales, incrementar el contador
    if letra in vocales:
        contador += 1

# Mostrar el resultado
print(f"La palabra '{palabra}' tiene {contador} vocales")
