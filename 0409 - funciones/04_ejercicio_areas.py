# funcion menu sin parametros
def menu():
    print("1) Calcular el área de un rectángulo")
    print("2) Calcular el área de un triángulo")
    print("3) Calcular el área de un cuadrado")
    print("4) Calcular el área de un círculo")
    print("5) Salir")

def area_rectangulo(base, altura):
    resultado = base * altura
    return resultado

def calcular_area_rectangulo(figura):
    largo = float(input("¿Cuanto mide de largo?: "))
    ancho = float(input("¿Cuanto mide de ancho?: "))
    area = area_rectangulo(largo, ancho)
    print("El area del",figura," es ", area)

opcion = 0
# Mientras la opcion sea deferente de 5
while opcion != 5:
    menu()
    opcion = int(input("Opción: "))
    if opcion == 1:
        calcular_area_rectangulo("rectangulo")
    elif opcion == 2:
        print("opcion 2")
    elif opcion == 3:
        calcular_area_rectangulo("cuadrado")
    elif opcion == 4:
        print("opcion 4")

