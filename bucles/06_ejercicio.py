print("-->Pizzeria PF <--")

while True:
    dinero = int(input("Cuanto dinero tiene: "))
    if dinero >= 7:
        print(f"Usted cuenta con {dinero}$")
        break

    else:
        print("Necesita al menos 7 euros para comprar una pizza")
        continue

pizzas = ["Jamon","Queso","Barbacoa"]
precios = [10,8,7]

print(f"0. pizza de {pizzas[0]}")
print(f"1. pizza de {pizzas[1]}")
print(f"2. pizza de {pizzas[2]}")

while True:
    elegir_pizza = int(input("Que pizza va a elegir: "))
    if pizzas < 3:
        print("2")
    
    else:
        print("error")


    