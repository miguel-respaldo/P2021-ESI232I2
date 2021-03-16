import random

num_comp = random.randint(1,10)

num = int(input("Adivina que número estoy pensando: "))

# Mientras el numero de la computadora no sea igual al numero del usuario
while num_comp != num:
    num = int(input("No, ese no es, intentalo de nuevo: "))

print("Felicidades, adivinaste!")
