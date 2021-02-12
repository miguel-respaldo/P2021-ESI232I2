# Contador de letras.
# Contar las vocales  de una cadena de texto.
# No considerar  vocales  con acento.
# Ejemplo:
# Entrada: Programacion
# Salida: 2 a
#         0 e
#         1 i
#         2 o
#         0 u

cadena = input("Escribe una cadena de texto: ")
print(cadena.count("a"), "a")
print(cadena.count("e"), "e")
print(cadena.count("i"), "i")
print(cadena.count("o"), "o")
print(cadena.count("u"), "u")