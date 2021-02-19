# Determinar  si una persona es baja, media o alta
# de estatura,  considerando que menor de 1.50 metros
# es baja y mayor a 1.70 metros es alta.

altura = float(input("Escribe tu altura: "))

if altura <= 1.50:
    print("Eres de altura baja")
else:
    if altura > 1.50 and altura < 1.70:
        print("Eres de altura media")
    else:
        print("Eres de altura alta")
