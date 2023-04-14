print("--> pizzeria PF <--")

dinero = int(input("Ingrese el dinero que tiene:"))
print(f"Usted cuenta con {dinero}$")
pizzas = ["jamon", "queso", "barbacoa"]
precios = [10, 8, 7]

print("que pizza quiere elegir")
for i, pizzas in enumerate(pizzas):
    print(f"--> {i} {pizzas} {precios[i]}$ <--")

