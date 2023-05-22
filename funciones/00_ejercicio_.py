colores = ["rojo","verde","azul"]

def añadir_colores(color):
    colores.insert(0,color)

añadir_colores(input("escribe un color: "))

print(colores)