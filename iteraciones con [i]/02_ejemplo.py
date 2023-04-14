frutas = ["manzana", "pera", "manzana", "uva"]
clientes = ["marcos", "axel", "diana", "alex"]
cantidad = [5, 10, 3, 5]

for i in range (len(frutas)):
    fruta = frutas[i]
    if fruta == "manzana":
        can = cantidad[i]
        cli = clientes[i]
        print(cli,can)
    