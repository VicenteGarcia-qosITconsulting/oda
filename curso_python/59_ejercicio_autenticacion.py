print('*** Sistema de Autenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario = input('Ingresa tu usuario: ')
password = input('Ingresa tu contraseña: ')

if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
    print('Bienvenido al Sistema')
elif usuario == USUARIO_VALIDO:
    print('Contraseña incorrecto')
elif password == PASSWORD_VALIDO:
    print('Usuario incorrecto')
else:
    print('Usuario y contraseña incorrectos')
