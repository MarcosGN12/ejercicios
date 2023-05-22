def suma (numero1,numero2):
    return numero1 + numero2

def resta (numero1,numero2):
    return numero1 - numero2

def multiplicacion (numero1,numero2):
    return numero1 * numero2

def division (numero1,numero2):
    return numero1 / numero2

print("*************")
print("*calculadora*")
print("*************")
print("")
print("1.suma")
print("2.resta")
print("3.multiplicacion")
print("4.division")
print("5.Cerrar calculadora")
print("")

    
while True:

    print("")
    opcion = int(input("dime una opcion: "))
    if opcion <= 5 and opcion > 0:
        print("")
        print("opcion valida")
        

    else:
        print("")
        print("Seleccione una opcion valida")
        


    if opcion == 1:
            print("Suma elegida")
            print("")
            numero1 = int(input("dime un numero: "))
            numero2 = int(input("dime un numero: "))          
            resultado = suma(numero1,numero2)
            print("")
            print(f"el resultado de la suma es {resultado}")

    if opcion == 2:
            print("Resta elegida")
            print("")
            numero1 = int(input("dime un numero: "))
            numero2 = int(input("dime un numero: "))
            resultado = resta(numero1,numero2)
            print("")
            print(f"el resultado de la resta es {resultado}")

    if opcion == 3:
            print("Multiplicacion elegida")
            print("")
            numero1 = int(input("dime un numero: "))
            numero2 = int(input("dime un numero: "))
            resultado = multiplicacion(numero1,numero2)
            print("")
            print(f"el resultado de la multiplicacion es {resultado}")

    if opcion == 4:
            print("Division elegida")
            print("")
            numero1 = int(input("dime un numero: "))
            numero2 = int(input("dime un numero: "))
            resultado = division(numero1,numero2)
            print("")
            print(f"el resultado de la division es {resultado}")

    if opcion == 5:
            print("cerrar calculadora")
            print("")
            print("Se cerro la calculadora con exito")
            break
            