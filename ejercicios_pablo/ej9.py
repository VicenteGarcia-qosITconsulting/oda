# Solicitamos el texto 
texto = input("Por favor, introduce un texto: ")

# Contamos las palabras usando split()
# split() sin argumentos divide el texto por espacios en blanco
palabras = texto.split()
num_palabras = len(palabras)

# (usamos lower() para contar independientemente de mayúsculas/minúsculas)

# Convertimos el texto a mayúsculas y minúsculas
texto_mayusculas = texto.upper()
texto_minusculas = texto.lower()

# Mostramos los resultados
print("\nResultados del análisis:")
print(f"Número de palabras: {num_palabras}")
print(f"\nTexto en mayúsculas:\n{texto_mayusculas}")
print(f"\nTexto en minúsculas:\n{texto_minusculas}")
