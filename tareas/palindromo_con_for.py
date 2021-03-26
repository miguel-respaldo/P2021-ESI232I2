# Pedimos la cadena al usuario
cadena = input("Escribe una cadena: ")

# Obtengo el tamaño de la cadena
tamano = len(cadena)
cadena_inversa = ""

#for i in range(tamano):
#    cadena_inversa = cadena[i] + cadena_inversa

for i in range(tamano):
    cadena_inversa = cadena_inversa + cadena[tamano-i-1]


print("original = ",cadena)
print("inversa  = ", cadena_inversa)

# Veo si es palindromo
if cadena == cadena_inversa:
    print("Es un palindromo")
else:
    print("NO es un palindromo")