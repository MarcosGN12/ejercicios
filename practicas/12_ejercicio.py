lado = -1


while lado <= 0:
    print("El lado debe ser un numero entero")
    lado = int(input("Dame un ancho del rectangulo: "))
    
    
print(f"el lado es {lado}")

for i in range(0,lado):
    linea = ""
    #linea arriba
    for j in range(0,lado):
        if j == i or j == lado -1 - i:
            linea = linea + "*"
        else:
            linea = linea + " "
    print(linea)


