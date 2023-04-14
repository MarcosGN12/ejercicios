numeros = []
for i in range(0,10):
    n = int(input(f"ingresa un numero {i+1} "))
    numeros.append(n)

numeros_pares = []
numeros_impares = []

for numero in numeros:
    if  numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
    
print(f"numeros pares {numeros_pares}")
print(f"numeros impares {numeros_impares}")

        



    