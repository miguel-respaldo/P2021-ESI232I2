# Pedir los terminos
num1 = int(input("Escribe el primer número: "))
num2 = int(input("Escribe el segundo número: "))
num3 = int(input("Escribe el tercer número: "))

# Hago la comparación de cada uno

if num1 > num2:
    if num1 > num3:
        print("El mayor es: ", num1)
    else:
        print("El mayor es: ", num3)
else:
    if num2 > num3:
        print("El mayor es: ", num2)
    else:
        print("El mayor es: ", num3)
