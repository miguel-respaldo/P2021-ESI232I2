# Pedimos la cadena al usuario
cadena = input("Escribe una cadena: ")

cadena_inversa = cadena[::-1]

#print("original = ",cadena)
#print("inversa  = ", cadena_inversa)

# Veo si es palindromo
if cadena == cadena_inversa:
    print("Es un palindromo")
else:
    print("NO es un palindromo")