# Solicitar entrada
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

# Realizar la operación según la entrada
if operacion == '+':
    resultado = num1 + num2
    print(f"El resultado de {num1} + {num2} = {resultado}")
elif operacion == '-':
    resultado = num1 - num2
    print(f"El resultado de {num1} - {num2} = {resultado}")
elif operacion == '*':
    resultado = num1 * num2
    print(f"El resultado de {num1} * {num2} = {resultado}")
elif operacion == '/':
    # Verificar división por cero
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de {num1} / {num2} = {resultado}")
    else:
        print("Error: No es posible dividir entre cero")
else:
    print("Error: Operación no válida. Por favor, usa +, -, * o /")
