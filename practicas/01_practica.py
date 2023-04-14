numeros = []
suma = 0 

for i in range(0,5):
    num = int(input(f"Dame un numero: "))
    numeros.append(num)
    print(numeros)
    suma += num
    print(f"el total es {suma}")

media = suma / len(numeros)

print(f"La media es {media}")

if media < 10:
    print(f"la media {media} es baja")
    
else:
    print(f"la media {media} es alta")