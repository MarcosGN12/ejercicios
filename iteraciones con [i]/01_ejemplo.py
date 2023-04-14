frutas = ["manzana", "pera", "fresa", "uva"]
precio = [0.50, 1.00, 1.55, 1.20]

print("lista de frutas con precio menor que 1.50")
for fruta in frutas:
    pos = frutas.index(fruta)
    pre = precio[pos]
    
    if pre < 1.50:
        print(fruta)