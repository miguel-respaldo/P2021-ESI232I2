# Ingresar un nombre y desplegarlo de forma vertial
# Ejemplo:
#   Ingresa un nombre: Python
#   P
#   y
#   t
#   h
#   o
#   n

nombre = input("Ingresa un nombre: ")

longitud = len(nombre)

for i in range(longitud):
    print(nombre[i])
