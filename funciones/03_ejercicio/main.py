from funcion_01 import area_circulo        
from funcion_02 import palindroma
from funcion_03 import promedio
from funcion_04 import contar_letras
from funcion_05 import numeros_duplicados
from funcion_06 import ordenar_alfabeticamente
from funcion_07 import lista_mayor_numero
from funcion_08 import numeros_menor_a_mayor
from funcion_09 import lista_caracteres


while True:

    print("")
    print("1.area de un circulo")
    print("2.palabra palindroma")
    print("3.promedio")
    print("4.contar palabras")
    print("5.Quitar numeros duplicados")
    print("6.Ordenar palabras alfabeticamente")
    print("7.Numeros mayores al entero")
    print("8.Ordenar numeros de menor a mayor")
    print("9.Cerrar calculadora")
    print("10.Cerrar calculadora")
    print("")

    opcion = float(input("dime una opcion: "))
    if opcion <= 5 and opcion > 0:
        print("")
        print("opcion valida")
        

    else:
        print("")
        print("Seleccione una opcion valida")
        


    if opcion == 1:
            print("Area de un circulo")
            print("")
            radio = int(input("Dime el radio del circulo: ")) 
            resultado = area_circulo(radio)
            print("")
            print(f"El area de un circulo es {resultado}")

    if opcion == 2:
            print("Palindroma")
            print("")
            palabra = (input("dime una palabra: "))
            resultado = palindroma(palabra)
            print("")
            print(f"La palabra {resultado}")

    if opcion == 3:
            print("promedio")
            print("")
            numero1 = int(input("dime un numero: "))
            numero2 = int(input("dime un numero: "))
            lista_numeros = numero1 + numero2
            lista_total = numero1,numero2
            resultado = promedio(lista_numeros)
            print("")
            print(f"el resultado del promedio es {resultado}")

    if opcion == 4:
            print("contador de palabras")
            print("")
            frase = str(input("Dime una palabra o frase: "))
            resultado = contar_letras(frase)
            print("")
            print(f"el numeros de palabras es {resultado}")

    if opcion == 5:
            print("numeros duplicados")
            print("")
            numero1 = int(input("dime un numero: "))
            numero2 = int(input("dime un numero: "))
            numero3 = int(input("dime un numero: "))
            numero4 = int(input("dime un numero: "))
            numero5 = int(input("dime un numero: "))
            lista_numeros = [numero1,numero2,numero3,numero4,numero5]
            print("")
            resultado = numeros_duplicados(lista_numeros)
            print(f"los numeros no duplicados son {resultado}")

    if opcion == 6:
            print("ordenar alfabeticamente")
            print("")
            palabra1 = str(input("dime una palabra: "))
            palabra2 = str(input("dime una palabra: "))
            palabra3 = str(input("dime una palabra: "))
            palabra4 = str(input("dime una palabra: "))
            palabra5 = str(input("dime una palabra: "))
            lista_palabras = [palabra1,palabra2,palabra3,palabra4,palabra5]
            print("")
            resultado = ordenar_alfabeticamente(lista_palabras)

    if opcion == 7:
            print("Nueva lista con un numero entero mayor")
            print("")
            numero_entero = int (input("dame el numero entero: "))
            numero1 = int(input("dime un numero: "))
            numero2 = int(input("dime un numero: "))
            numero3 = int(input("dime un numero: "))
            numero4 = int(input("dime un numero: "))
            numero5 = int(input("dime un numero: "))
            lista_numeros = [numero1,numero2,numero3,numero4,numero5]
            print("")
            resultado = lista_mayor_numero(numero_entero,lista_numeros)
            print(f"Los numeros mayores que el numero entero son {resultado}")

    if opcion == 8:
            print("ordenar numeros de menor a mayor")
            print("")
            numero1 = int(input("dime un numero: "))
            numero2 = int(input("dime un numero: "))
            numero3 = int(input("dime un numero: "))
            numero4 = int(input("dime un numero: "))
            numero5 = int(input("dime un numero: "))
            lista_numeros = [numero1,numero2,numero3,numero4,numero5]
            print("")
            resultado = numeros_menor_a_mayor(lista_numeros)
            print(f"Los numeros ordenados de menor a mayor: {resultado} ")


    if opcion == 9:
            print("añadir un caracter al final")
            print("")
            palabra1 = (input("dime una palabra: "))
            palabra2 = (input("dime una palabra: "))
            palabra3 = (input("dime una palabra: "))
            palabra4 = (input("dime una palabra: "))
            palabra5 = (input("dime una palabra: "))
            conjunto = [palabra1,palabra2,palabra3,palabra4,palabra5]
            caracter = (input("dime el caracter que contiene una palabra: "))
            print("")
            resultado = lista_caracteres(caracter,conjunto)
            print(f"Las palabras que contienen ese caracter son: {resultado} ")

    if opcion == 10:
            print("cerrar calculadora")
            print("")
            print("Se cerro la calculadora con exito")
            break
            