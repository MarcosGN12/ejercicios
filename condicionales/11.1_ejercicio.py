dia = int(input("Ingrese un número: "))
mes = int(input("Ingrese un número: "))
año = int(input("Ingrese un número: "))

diaValido = False
mesValido = False
añoValido = False

if dia <= 31 and dia >= 1:
    diaValido = True
    print("dia valido")

else:
    print("dia invalido")

if mes <= 12 and mes >= 1:
    mesValido = True
    print("mes valido")
    
else:
    print("mes invalido")

if año <= 2023 and año >= 1:
    añoValido = True
    print("año valido")
    
else:
    print("año invalido")

if diaValido and mesValido and añoValido:
    print(f"estamos a {dia}/{mes}/{año}")

else:
    print("fecha no valida")