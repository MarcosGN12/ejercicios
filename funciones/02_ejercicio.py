import math

#1#
def Area_circulo (radio):
    return math.pi * (radio * radio) 
#2#
def palindroma (palabra):
    primera_letra = 0
    ultima_letra = len(palabra) -1

    while palabra[primera_letra] == palabra[ultima_letra]:
          if primera_letra >= ultima_letra:
                return True
          primera_letra += 1
          ultima_letra -= 1
    return False

#3# 
def promedio (lista_numeros):
        for i in range(0,lista_numeros):
          return lista_numeros / len(lista_total)
        
#4# 
def contar_letras (frase):
          return(frase.count(" ")+1)
         

#5# 
def numeros_duplicados (lista_numeros):

    unico = []

    for i in lista_numeros:
          if i not in unico:
                unico.append(i)
    return unico

#6# 
def ordenar_alfabeticamente (lista_palabras):
    resultado_final = []

    for i in lista_palabras:
          resultado_final.append(i)
    resultado_final.sort()
    print(f"Los numeros no repetidos son: {resultado_final} ")
    return resultado_final

#7# 
def lista_mayor_numero (numero_entero,lista_numeros):
    lista_mayor = []
    for i in range(0,len(lista_numeros)):
          if lista_numeros[i] > numero_entero:
                lista_mayor.append(lista_numeros[i])
    return lista_mayor

#8#    
def numeros_menor_a_mayor (lista_numeros):
    resultado_final = []

    for i in lista_numeros:
          resultado_final.append(i)
          resultado_final.sort()
    return resultado_final

#9# 
def lista_caracteres (caracter,conjunto):
    lista_final = []
    for i in range(0,len(conjunto)):
          if caracter in conjunto[i]:
                lista_final.append(conjunto[i])
    return(lista_final)

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
            resultado = Area_circulo(radio)
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
            