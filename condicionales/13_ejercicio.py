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
elif operacion == resta:
    print("funcion resta seleccionada")
elif operacion == multiplicacion:
    print("funcion multiplicacion seleccionada")
elif operacion == division:
    print("funcion division seleccionada")
elif operacion == modulo:
    print("funcion modulo seleccionada")
elif operacion == exponente:
    print("funcion exponente seleccionada")
else:
    print("no existe esta operacion")

if operacion == suma:
    resultado = round(numero1 + numero2)
elif operacion == resta:
    resultado = round(numero1 - numero2)
elif operacion == multiplicacion:
    resultado = round(numero1 * numero2)
elif operacion == division:
    if numero2 == 0:
        print("Error: no se puede dividir por cero")
        resultado = None
    else:
        resultado = round(numero1 / numero2)
elif operacion == modulo:
    if numero2 == 0:
        print("Error: no se puede calcular el módulo por cero")
        resultado = None
    else:
        resultado = round(numero1 % numero2)
elif operacion == exponente:
    resultado = round(numero1 ** numero2)

if resultado is not None:
    print(f"el resultado es {resultado}")