# importar la biblioteca de time para usar sleep
import time

for contador in range(10,0,-1):
    print(contador)
    # Nos dormimos (o esperamos) un segundo
    time.sleep(1)
print("Despegue")