colores = {
    1 : "rojo",
    2 : "azul",
    3 : "verde",
    4 : "amarillo"
}

for i in colores:
    print(f"{i} - {colores[i].capitalize()}")

colores = {
    1 : "rojo",
    2 : "azul",
    3 : "amarillo",
    4 : "verde"
}

colores[5] = "naranja"
print(colores)