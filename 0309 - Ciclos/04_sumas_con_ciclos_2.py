# Sacar el promedio de una cantidad de numeros
# especificda por el usuario

cantidad = int(input("¿Cuantos números son en total?: "))

promedio = 0

i=1
while i<=cantidad:
    numero = int(input("Ingresa un número: "))
    promedio = promedio + numero
    i = i + 1

promedio = promedio / cantidad
print("El promedio es: ", promedio)