"""
Escriba un programa en python que modifique la configuracion del siguiente archivo escrito en formato JSON,

image.png

El archivo debe ser modificado colocando el key y el value del atributo json y que se guarde directamente:

Ejemplo name, 'Andres Iniesta Perez' y modificarlo internamente, si es un nuevo club colocarlo
"""


import json

with open('details.json', 'r') as f:
    data = json.load(f)


while True:

    print(f"""
Ingresa una propiedad a modificar:
    1. name
    2. position
    3. nationality
    4. date_of_birth
    5. clubs
    6. honors
    7. show json
""")

    action = input("Ingresa una accion: ")
    if action == '1':
        data['name'] = input('Introduce el nuevo nombre: ')
    elif action == '2':
        data['position'] = input('Introduce la nueva posicion: ')
    elif action == '3':
        data['nationality'] = input('Introduce la nueva nacionalidad: ')
    elif action == '4':
        data['date_of_birth'] = input(
            'Introduce la nueva fecha de nacimiento: ')
    elif action == '5':
        data['clubs'][0]['name'] = input('Introduce el nuevo nombre: ')
        data['clubs'][0]['period'] = input('Introduce el nuevo periodo: ')
    elif action == '6':
        data['honors'] = input('Introduce los nuevos honores: ')
    elif action == '7':
        print(json.dumps(data, indent=4))

    # data['clubs'][0]['name'] = input('Introduce el nuevo nombre: ')

    with open('jsonModificado.json', 'w') as f:
        json.dump(data, f, indent=4)

    print(json.dumps(data, indent=4))
