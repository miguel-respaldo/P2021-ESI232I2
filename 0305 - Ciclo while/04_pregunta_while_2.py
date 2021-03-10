# Preguntamos al usuario para seguir
respuesta = input("¿Quieres que le siga?: ")

# convierto a minusculas la cadena
respuesta = respuesta.lower()

# Mientras la repespuesta sea si,
while respuesta == "si":
    # seguimos preguntando
    respuesta = input("Seguro, ¿Quieres que le siga?: ")
    # convierto a minusculas la cadena
    respuesta = respuesta.lower()

