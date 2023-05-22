ancho = -1
alto = -1

while ancho <= 0:
    print("El ancho debe ser un numero entero")
    ancho = int(input("Dame un ancho del rectangulo: "))
    
while alto <= 0:
    print("El alto debe ser un numero entero")
    alto= int(input("Dame un alto del rectangulo: "))
    
print(f"el ancho es {ancho} y el alto es {alto}")

for i in range(0,alto):
        linea = ""
        for j in range(0,ancho):
            linea = linea + "*"
        print(linea)