numero = int(input("Ingrese un número: "))

if numero % 2 == 0 and numero > 20 and numero >= 100 and numero <= 150:
    print("coincide con todas las condiciones")
    if numero >= 130 and numero <= 140:
        print("coincide con las condiciones avanzadas")

else:
    print("no coincide con las condiciones")