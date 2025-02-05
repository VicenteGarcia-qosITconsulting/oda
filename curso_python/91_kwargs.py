print('*** Imprimir detalles de una persona usando kwargs ***')

# Funcion que acepta argumentos variables en forma de llave-valor dict
def imprimir_detalle_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

# Llamamos a la funcion
imprimir_detalle_persona(nombre='Vicen', edad=19, ciudad='Cadiz')
imprimir_detalle_persona(nombre='Carlos', edad=28, ciudad='Valencia', puesto='Gerente')