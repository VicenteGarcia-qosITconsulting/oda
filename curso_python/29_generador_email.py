print('*** Sistema Generador de Emails ***')
nombre = input('Cual es tu nombre? ')
apellidos = input('Cuales son tus apellidos? ')
empresa = input('Nombre de tu empresa? ')
extension_dominio = input('Extension del dominio de tu empresa? ')

nombre = nombre.strip().lower().replace(' ','.')
apellidos = apellidos.strip().lower().replace(' ', '.')
empresa = empresa.strip().lower().replace(' ', '')
extension_dominio = extension_dominio.strip().lower().replace(' ', '')

email = f'{nombre}.{apellidos}@{empresa}{extension_dominio}'

print(f'''
Tu nuevo email generado por el sistema es:
    {email}
    Felicidades!''')
