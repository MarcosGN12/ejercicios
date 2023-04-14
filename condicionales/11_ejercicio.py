dia = int(input("Ingrese un número: "))
mes = int(input("Ingrese un número: "))
año = int(input("Ingrese un número: "))
resultado = (f"{dia}/{mes}/{año}")

# dia

if dia <= 31 and dia > 0:
    print(f"dia {dia}")
    
else:
    print("no existe ese dia")

# mes

if mes <= 12 and  mes > 0:
    print(f"mes {mes}")

else:
    print("no existe ese mes")

# año

if año <= 2023 and año > 0:
    print(f"año {año}")

else:
    print("no existe ese año")

#resultado

if  dia <= 31 and dia > 0 and mes <= 12 and  mes > 0 and año <= 2023 and año > 0:
    print(f"estamos a {resultado}")

else:
    print("fecha invalida")

