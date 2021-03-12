# uso de continue en while

i = 1

while i <= 10:
    print("hola")
    if i % 2 != 0:
        continue
    print(i)
    i = i + 1