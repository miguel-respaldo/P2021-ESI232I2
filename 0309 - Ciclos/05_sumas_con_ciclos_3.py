# Sacar el promedio de una cantidad de numeros
# especificda por el usuario


print("Programa que suma numeros y para salir ingresa 0")

promedio = 0
cantidad = 0
numero = 1

while numero != 0:
    numero = int(input("Ingresa un número: "))
    if numero != 0:
       promedio = promedio + numero
       cantidad = cantidad + 1

promedio = promedio / cantidad
print("El promedio es: ", promedio)