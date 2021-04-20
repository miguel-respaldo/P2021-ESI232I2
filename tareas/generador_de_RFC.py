nombre = input("Escribe tu nombre: ")
apellido_paterno = input("Escribe tu apellido paterno: ")
apellido_materno = input("Escribe tu apellido materno: ")

dia = int(input("Escribe tu dia de nacimento: "))
mes = int(input("Escribe tu mes de nacimento: "))
anio = input("Escribe tu año de nacimento: ")

# Convierto a mayusculas
nombre = nombre.upper()
apellido_paterno = apellido_paterno.upper()
apellido_materno = apellido_materno.upper()

RFC = ""

# Primera letra de Apellido Paterno
RFC = RFC + apellido_paterno[0]

# Primera vocal de Apellido Paterno
for letra in apellido_paterno[1:]:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        break
RFC = RFC + letra

# Primera letra de Apellido Materno
RFC = RFC + apellido_materno[0]

# Primera letra de Nombre
RFC = RFC + nombre[0]

# Dos digitos del año
if len(anio) == 4:
    anio = anio[2:]

RFC = RFC + anio

# Dos digitos del mes
if mes < 10:
    RFC = RFC + "0"
RFC = RFC + str(mes)

# Dos digitos del dia
if dia < 10:
    RFC = RFC + "0"
RFC = RFC + str(dia)

print(RFC)
