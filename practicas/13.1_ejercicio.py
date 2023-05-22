altura = -1

while altura <= 0:
    print("Las lineas deben ser un numero entero")
    altura = int(input("Dame unas lineas: "))
    

print(f"las lineas son {altura}")

ancho = 1 + 2 * (altura -1)
print(f"El ancho es {ancho}")

medio = (ancho -1) / 2

for i in range(0,altura):
        linea = ""
        for j in range(0,ancho):
            if j == medio +i or j == medio -i or i == altura -1:
                linea = linea + "*"
            else:
                linea = linea + " "
        print(linea)