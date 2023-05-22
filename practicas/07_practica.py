lista1 = []
lista2 = []
resultado = []

for i in range(0,5):
    numero1 = int(input(f"Dime el numero {i+1}: "))
    lista1.append(numero1)
    print(lista1[i])

print("")

for i in range(0,5):
    numero2 = int(input(f"Dime el numero {i+1}: "))
    lista2.append(numero2)
    print(lista2[i])

print("")

print(f"La lista 1 tiene {lista1}")
print(f"La lista 2 tiene {lista2}")

for i in range(len(lista1)):
    num1 = lista1[i]
    num2 = lista2[i]

    multiplicacion = num1 * num2
    resultado.append(multiplicacion)

print("")

print(f"los resultados son {resultado}")