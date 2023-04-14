lista_numeros1 = []
lista_numeros2 = []

for i in range(0,5):
    numero1 = (input(f"ingresa numero {i+1} para la primera lista "))
    lista_numeros1.append(numero1)
    print(lista_numeros1)
    print("")

for i in range(0,5):
    numero2 = (input(f"ingresa numero {i+1} para la segunda lista "))
    lista_numeros2.append(numero2)
    print(lista_numeros2)
    print("")

print(f"primera lista {lista_numeros1}")
print(f"segunda lista {lista_numeros2}")


for i in range(len(lista_numeros1)):
    num1 = lista_numeros1[i]
    num2 = lista_numeros2[i]
    if num1 == num2:
        print(f"El número {num1} está en ambas listas y en la posicion {i}.")



