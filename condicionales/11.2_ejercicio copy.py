dia = int(input("Ingrese un número: "))
mes = int(input("Ingrese un número: "))
año = int(input("Ingrese un número: "))

diaValido = dia <= 31 and dia >= 1
mesValido = mes <= 12 and mes >= 1
añoValido = año <= 2023 and año >= 1

if diaValido == True:
    print("dia valido")

else:
    print("dia invalido")

if mesValido == True:
    print("dia valido")

else:
    print("dia invalido")

if añoValido == True:
    print("dia valido")
    
else:
    print("dia invalido")

if diaValido and mesValido and añoValido:
    print(f"estamos a {dia}/{mes}/{año}")

else:
    print("fecha no valida")