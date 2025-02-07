# Crear una lista vacía para almacenar los números
numeros = []

# Pedir 5 números 
for i in range(5):
    num = input(f"Introduce el número {i+1}: ")
    while not num.replace('.', '', 1).isdigit():  # Permite números con decimales
        print("Por favor, introduce un número válido")
        num = input(f"Introduce el número {i+1}: ")
    numeros.append(float(num))

# Mostrar la lista ordenada de menor a mayor
ascendente = sorted(numeros)
print("\nLista ordenada de menor a mayor:", ascendente)

# Mostrar la lista ordenada de mayor a menor
descendente = sorted(numeros, reverse=True)
print("Lista ordenada de mayor a menor:", descendente)

# Mostrar el número más grande y más pequeño
maximo = max(numeros)
minimo = min(numeros)
print(f"\nNúmero más grande: {maximo}")
print(f"Número más pequeño: {minimo}")
