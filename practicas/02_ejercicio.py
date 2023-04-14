numeros = []

for i in range(0,7):
    num = int(input("ingresa el numero "))
    numeros.append(num)    

print(f"Lista introducida {numeros}\n")

maximo = numeros[0]
minimo = numeros[0]

print(f"Maximo inicial={maximo}")
print(f"Minimo inicial={minimo}")

print("\n")

for num in numeros:
    print("#######################")
    print(f"Leyendo el valor de la lista {num}")

    if num > maximo:
        print()
        print("Nuevo maximo encontrado")
        print(f"Maximo anterior={maximo}")
        maximo = num
        print(f"Maximo nuevo={maximo}")
  

    if num < minimo:
        print()
        print("Nuevo minimo encontrado")
        print(f"Minimo anterior={minimo}")
        minimo = num
        print(f"Minimo nuevo={minimo}")
       
    print("#######################\n")

print(f"El maximo es {maximo}")
print(f"El minimo es {minimo}")