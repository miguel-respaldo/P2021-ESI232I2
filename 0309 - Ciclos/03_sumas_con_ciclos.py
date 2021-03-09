# Sacar el promedio de una cantidad de numeros
# especificda por el usuario

cantidad = int(input("¿Cuantos números son en total?: "))

promedio = 0

for i in range(cantidad):
    numero = int(input("Ingresa un número: "))
    promedio = promedio + numero

promedio = promedio / cantidad
print("El promedio es: ", promedio)