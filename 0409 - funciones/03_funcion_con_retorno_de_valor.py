# Aqui definimos la funcion con parametros y retorno de valor
def suma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

num1 = int(input("Escribe un número: "))
num2 = int(input("Escribe otro número: "))
# Aqui invocamos la función con argumentos y retorno de valor
res = suma(num1, num2)
print("El resultado es: ", res)