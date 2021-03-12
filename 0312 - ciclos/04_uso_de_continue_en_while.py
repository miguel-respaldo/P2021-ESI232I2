# uso de continue en while

i = 0

while i <= 10:
    print("hola")
    i = i + 1
    if i % 2 != 0:
        continue
    print(i)
