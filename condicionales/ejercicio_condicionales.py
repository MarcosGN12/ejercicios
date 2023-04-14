print("calculadora")

numero1 = int(input("numero 1: "))
numero2 = int(input("numero 2: "))

print("1 suma")
print("2 resta")
print("3 multiplicacion")
print("4 division")
print("5 modulo")
print("6 exponente")

operacion = int(input("operacion: "))

suma = 1
resta = 2
multiplicacion = 3
division = 4
modulo = 5
exponente = 6

if operacion == suma:
    print("funcion suma seleccionada")
    resultado = round(numero1 + numero2)

elif operacion == resta:
    print("funcion resta seleccionada")
    resultado = round(numero1 - numero2)

elif operacion == multiplicacion:
    print("funcion multiplicacion seleccionada")
    resultado = round(numero1 * numero2)
elif operacion == division:
    print("funcion division seleccionada")

    if numero2 == 0:
        print("error:no se puede dividir por cero")
        resultado = None

    else:
        resultado = round(numero1 / numero2)

elif operacion == modulo:
    print("funcion modulo seleccionada")
    if numero2 == 0:
        print("error:no se puede calcular el módulo por cero")
        resultado = None

    else:
        resultado = round(numero1 % numero2)
        
elif operacion == exponente:
    print("funcion exponente seleccionada")
    resultado = round(numero1 ** numero2)

else:
    print("no existe esta operacion")

if resultado is not None:
    print(f"el resultado es {resultado}")