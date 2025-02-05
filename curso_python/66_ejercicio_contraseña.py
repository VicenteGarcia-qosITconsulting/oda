print('Creación y Validación de un contraseña ***')

password = input('Ingresa un password (debe tener al menos 6 caracteres: ')

# Validar la contraseña
while len(password) < 6:
    print('La contraseña no cumple con los requisitos. Debe tener al menos 6 caracteres')
    password = input('Ingresa un nuevo valor de contraseña: ')
else:
    print('El valor de contraseña es válido')
