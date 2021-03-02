
cadena = input("Escribe una cadena: ")

print("La primera letra es ",cadena[0])
print("Las primeras tres son", cadena[:3])
print("Las últimos tres son", cadena[-3:])
print("De la segunda al final", cadena[2:])
print("del segundo al quinto es", cadena[2:5])
#  abcdefghij  cadena
#  0123456789  indices

#  2/3/2021
#  02/03/2021

diagonal = cadena.find("/")
print("La posición de la diagonal es ", diagonal)
print("Antes de la diagonal hay ",cadena[:diagonal])

dia = int(cadena[:diagonal])
print("El dia es ", dia)

print(dia,"de el mes",dia)
