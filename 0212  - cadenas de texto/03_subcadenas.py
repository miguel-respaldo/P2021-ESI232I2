s = 'Bienvenido a Python'
#    0123456789012345678
print(s.endswith("thon"))
print(s.startswith("Buen"))
print(s.find("ido"))
print(s.rfind("venida"))
print(s.count("o"))

# Eliminando espacio en blanco
s = "  Hola Mundo   "
print("--" + s.lstrip()+ "---")
print("--" + s.rstrip()+ "---")
print("--" + s.strip() + "---")