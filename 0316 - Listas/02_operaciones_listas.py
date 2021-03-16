l1 = [7,2,11,4,6,21]
l2 = [8,5]

print("len ", len(l1) )  # Imprime el número de elementos de la lista

# imprimir el maximo de l1
print("max ", max(l1) )

# imprimir el minimo de l1
print("min ", min(l1) )

# imprimir la suma de los elementos de l1
print("sum ", sum(l1) )

# El 5 esta en l1?
print("5 in l1 = ", 5 in l1)

# El 11 esta en l1?
print("11 in l1 = ", 11 in l1)

# El 8 no esta en l1?
print("8 not in l1 = ", 8 not in l1)

# Hago una lista grande uniendo l1 + l2
print("l1 + l2: ", l1 + l2)

# Veo el elemento 3 de l1
print("l1[3]", l1[3])

# Veo el elemento del 1 al 3 (sin incluir el 3)
print("l1[1:3]", l1[1:3])

# Repito l2 tres veces
print("3*l2", 3*l2)

# Asigno l1 los elementos de l2
l1 = l2

# veo si son iguals l1 y l2
print("l1 == l2", l1 == l2)
