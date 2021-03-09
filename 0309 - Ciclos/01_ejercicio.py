import random

#  Investigar  las  siguientes  funciones:
#  ord(), chr(), randint()
#  para resolver  el siguiente  problema:
#  1. Generar  una cadena aleatoria  de cierta
#  longitud. La longitud de la cadena es un
#  dato de entrada.
#   Ejemplo:
#     Entrada
#       Longitud de la cadena: 10
#     Salida
#       hjqoapmsje

# The ord() function returns the number representing
#   the unicode code of a specified character.
# The chr() function returns the character that
#   represents the specified unicode.
# The randint() method returns an integer number
#   selected element from the specified range.

longitud = int(input("Longitud de la cadena: "))

cadena = ""

for i in range(longitud):
    num_aleatorio = random.randint(ord("a"), ord("z"))
    letra = chr(num_aleatorio)
    cadena = cadena + letra
    print(i, "la caden vale = ",cadena)

print(cadena)





