# Solicitamos el número de niveles 
n = int(input("Introduce el número de niveles para la pirámide: "))

# Generamos la pirámide
for i in range(1, n + 1):
    # En cada línea, imprimimos el número i, i veces
    # end=' ' hace que los números se separen por espacios
    for j in range(i):
        print(i, end=' ')
    # Salto de línea al final de cada nivel
    print()
