# Inicializamos las cadenas de texo
# s viene de String -> cadena de texto
s1 = str() # Esto es una cadena de texto vacia
s2 = ""    # Esto es una cadena de texto vacia
s3 = "Libreta"  # contiene la palabra Libreta
s4 = str("Libreta") # Lo mismo que s3
# Imprimimos s4
print(s4)

# Libreta
# 0123456  <-- indices

print(s4[3]) # Imprime la letra r
print(s4[6]) # Imprime la letra a
print(s4[0]) # Imprime la letra L

# Concatenación

s1="Algoritmos"
s2="Programación"

s = s1 + " y " + s2
# "áéàû*uÇḉ"
print(s)

s3 = "Algoritmos" + " y " + "Programación"
print(s3)
s4 = "Algoritmos y Programación"
print(s4)

# Repeticiones en cadenas

s3 = 3*s1
print(s3)
# ahora con espacios
s3 = 3*(s1 + " ")
print("con espacios", s3)