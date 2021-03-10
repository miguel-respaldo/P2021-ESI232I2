fecha = input("Escribe la fecha en el formato dd/mm/aaaa: ")

diagonal1 = fecha.find("/")
diagonal2 = fecha.rfind("/")

dia = int(fecha[:diagonal1])
mes = int(fecha[diagonal1+1:diagonal2])
anio = fecha[diagonal2+1:]

if mes == 1:
    print(dia, "de Enero de", anio)
elif mes == 2:
    print(dia, "de Febrero de", anio)
elif mes == 3:
    print(dia, "de Marzo de", anio)
elif mes == 4:
    print(dia, "de Abril de", anio)
elif mes == 5:
    print(dia, "de Mayo de", anio)
elif mes == 6:
    print(dia, "de Junio de", anio)
elif mes == 7:
    print(dia, "de Julio de", anio)
elif mes == 8:
    print(dia, "de Agosto de", anio)
elif mes == 9:
    print(dia, "de Septiembre de", anio)
elif mes == 10:
    print(dia, "de Octubre de", anio)
elif mes == 11:
    print(dia, "de Noviembre de", anio)
elif mes == 12:
    print(dia, "de Diciembre de", anio)
