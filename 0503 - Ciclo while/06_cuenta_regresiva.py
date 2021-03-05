# importar la biblioteca de time para usar sleep
import time

contador = 10
#for contador in range(10,0,-1):
while contador > 0:
    print(contador)
    contador = contador - 1
    # Nos dormimos (o esperamos) un segundo
    time.sleep(1)
print("Despegue")
