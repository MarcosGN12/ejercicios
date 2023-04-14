    #si se pone un numero que no sea del 0 al 2 saltara un bucle con el codigo anterior dentro del else

    
print("--> Pizzeria PF <--")

dinero = int(input("Ingrese el dinero que tiene: "))

if dinero >= 7:
    print(f"Usted cuenta con {dinero}$")
else:
    print("Necesita al menos 7 euros para comprar una pizza")

pizzas = ["jamon", "queso", "barbacoa"]
precios = [10, 8, 7]

for i, pizza in enumerate(pizzas):
    print(f"--> {i} {pizza} {precios[i]}$ <--")

elegir_pizza = int(input("¿Qué pizza desea? "))

if elegir_pizza not in range(len(pizzas)):
    print("La opción elegida no es válida.")
else:
    print(f"Pizza de {pizzas[elegir_pizza]} elegida.")
    precio_pizza = precios[elegir_pizza]
    resultado = dinero - precio_pizza 
    print(f"Le quedan {resultado}$.")

    print("--> 0 Terminar el pedido <--")
    print("--> 1 Añadir extras <--")

    opcion = int(input("¿Qué desea hacer? "))

    if opcion == 0:
        print("Pedido terminado.")

    elif opcion == 1:
        ingredientes = ["queso", "peperoni", "setas"]
        precios_extras = [1.50, 1.20, 1]
        for i, extra in enumerate(ingredientes):
            print(f"--> {i} {extra} {precios_extras[i]}$ <--")

        elegir_extra = int(input("¿Qué extra desea añadir? "))

        if elegir_extra not in range(len(ingredientes)):
            print("La opción elegida no es válida.")
        else:
            print(f"Añadir {ingredientes[elegir_extra]} elegido.")
            precio_extra = precios_extras[elegir_extra]
            resultado -= precio_extra
            print(f"Le quedan {resultado}$.")
