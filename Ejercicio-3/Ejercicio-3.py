"""

Descripción del Problema:

Se requiere desarrollar un programa en Python que convierta un número entero en su representación en palabras en español. Por ejemplo, si se ingresa el número 10, el programa debe devolver "DIEZ".

 

Requisitos:
El programa debe aceptar un número entero como entrada.
Debe convertir el número a su representación en palabras en español.


Utilizar la biblioteca inflect u otras técnicas para realizar la conversión.

Especificaciones Adicionales:
El programa debe manejar números enteros en el rango admitido por el español.
Debe proporcionar una salida amigable y legible para el usuario.
Ejemplo de Entrada/Salida:


Entrada: 10
Salida: DIEZ

Entrada: 1234
Salida: MIL DOSCIENTOS TREINTA Y CUATRO


Entregables:
Archivo Python que contenga la implementación del programa.
Si se utilizan bibliotecas adicionales, se debe proporcionar información sobre cómo instalarlas y utilizarlas.
"""

"""
Utilice la libreria num2words para realizar la conversion de numeros a palabras
Esta libreria se instala de la siguiente manera: pip install num2words

Link de la documenacion: https://pypi.org/project/num2words/
"""




from num2words import num2words
import re
def converter(numero):
    return num2words(numero, lang='es').upper()


def validator(cadena):
    patron = "^-?[0-9]+$"
    if re.match(patron, cadena):
        return True
    else:
        return False


while True:
    try:
        num = input('Introduce un numero: ')
        if validator(num):
            print("\n")
            print("ENTRADA: ", num)
            print("SALIDA: ", converter(int(num)))
            print("\n")
        else:
            print('[ERROR]: El valor introducido no es un numero entero')
    except ValueError:
        print('[ERROR]: El valor introducido no es un numero')
