# Ejercicio
# Algoritmo para manipular una lista, que incluya 8 opciones:

# 1. Inicializar lista
#lista = list()  # esta tambien esta bien
lista = []
print("paso 1: ", lista)

# 2. Agregar un elemento a la lista
#   el nuevo elemento se debe agregar al final de la lista
lista.append(15) # numero, una palabra
# extra
lista.extend([18, 5, 3, 19, 14,10]) # Lista

print("paso 2: ", lista)

# 3. Elimintar un elemento de la lista
#   Validar si el elemento a elimintar esta en la lista

# Si el elemento 3 esta en la lista entonces remuevelo
if 3 in lista:
    lista.remove(3)
print("paso 3: ", lista)

# 4. Remplazar un elemento en la lista
# 10 -> 20
# Validar si el elemento a remplazar está en la lista
# Insertar el elemento remplazo en la posición donde se
# encontró el elemento a remplazar

if 10 in lista:
    pos = lista.index(10)
    lista.insert(pos,20)
    lista.remove(10)
print("paso 4: ", lista)

# 5. Buscar un elemento en la lista
#  Validar si el elemento a buscar está en la lista
#  Imprimir la posición del elemento encontrado

if 5 in lista:
    pos = lista.index(5)
    print("la posición de 5 es: ", pos)

print("paso 5: ", lista)

# 6. Obtener el número de elementos de la lista
num_elementos = len(lista)
print("Elementos de la lista ", num_elementos)

# 7. Ordenar los elementos de la lista
lista.sort()

# 8. Imprimir lista
print("paso 8: ", lista)
