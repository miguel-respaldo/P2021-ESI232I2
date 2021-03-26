# Pedimos la fecha en el formato dd/mm/aaaa
fecha = input("Escribe la fecha de tu nacimiento en el formato dd/mm/aaaa: ")

# Separamos la fecha con la /
lista_fecha = fecha.split("/")

dia = int(lista_fecha[0])
mes = int(lista_fecha[1])

# Si el dia es mayor o igual a 22 y el mes es diciembre
#  o  el dia es menor o igual a 20 y el mes es enero
if (dia >= 22 and mes == 12) or (dia <=20 and mes == 1):
    print("Eres Capricornio")
elif (dia >= 21 and mes == 1) or (dia <=19 and mes == 2):
    print("Eres Acuario")
elif (dia >= 20 and mes == 2) or (dia <=20 and mes == 3):
    print("Eres Pisicis")





