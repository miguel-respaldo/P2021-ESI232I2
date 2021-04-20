# CSV -> Comma Separated Values
import csv

def promedio_por_alumno(lector):
    for fila in lector:
        promedio = 0.0
        if fila[0] == "nombre":
            continue
        for i in range(1,5):
            promedio = promedio + float(fila[i])
        promedio = promedio / 4.0
        print("El promedio de", fila[0], "es", promedio)

# Pregutamos por el nombre del archivo
nombre_archivo = input("Escribe el nombre del archivo: ")
archivo = open(nombre_archivo,"r")
lector = csv.reader(archivo)

promedio_por_alumno(lector)

