def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius"""
    return (fahrenheit - 32) * 5/9

# Mostrar menú de opciones
print("Selecciona la conversión que deseas realizar:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

# Obtener la elección del usuario 
opcion = input("\nIngresa tu opción (1 o 2): ")
if opcion not in ["1", "2"]:
    print("Opción no válida. Debes elegir 1 o 2.")
else:
    temperatura = input("Ingresa la temperatura: ")
    if temperatura.replace('.', '', 1).isdigit() or (temperatura.startswith('-') and temperatura[1:].replace('.', '', 1).isdigit()):
        temperatura = float(temperatura)
        
        # Realizar la conversión según la opción elegida
        if opcion == "1":
            resultado = celsius_a_fahrenheit(temperatura)
            print(f"\n{temperatura}°C = {resultado:.2f}°F")
        else:
            resultado = fahrenheit_a_celsius(temperatura)
            print(f"\n{temperatura}°F = {resultado:.2f}°C")
    else:
        print("Error: Por favor, ingresa valores numéricos válidos.")
