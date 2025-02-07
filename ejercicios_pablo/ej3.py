# lista 
numeros = [4, 7, 12, 15, 8, 21, 6, 33, 10, 5]

# Mostrar la lista original
print("Lista original:", numeros)

# Mostrar solo los números pares
numeros_pares = [num for num in numeros if num % 2 == 0]
print("Números pares:", numeros_pares)

# Calcular y mostrar la suma de todos los números
suma_total = sum(numeros)
print("Suma total:", suma_total)

# Reemplazar impares por 0
numeros_modificados = [num if num % 2 == 0 else 0 for num in numeros]
print("Lista con impares reemplazados por 0:", numeros_modificados)
