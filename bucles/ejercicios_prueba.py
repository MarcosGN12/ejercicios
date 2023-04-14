#for i in range (3,-12,-3):
#    print(f"El valor del bucle es {i}")
#    print("hola")

# hola = ["rosa","verde","amarillo","rojo"]
# for ho in hola:

#     if ho == "amarillo":
#         print("se ha saltado este valor")
#         break

#     print(f"color valido {ho}")

i = 1

while i <= 0:
    print(f"bucle infinito {i}")
    i += 1


while True:
    salida = input("Introduce accion \n").lower()
    if salida == "salir":
        break
                