lista_numero = [10,45,55,76]

print(lista_numero)

print(lista_numero[3])

print(f"Utiliza la lista del ejercicio 1 para mostrar el {lista_numero[0]} y {lista_numero[3]} ")

lista_colores = ["rojo","azul","verde","amarillo"]
print(lista_colores[-0])
print(lista_colores[-2])

print(lista_colores[1][1])

paises = ["namibia","españa","zimbawe","portugal","alemania","irlanda","polonia"]
print(paises[5])

lista_colores.append("rosa")
lista_colores.insert(0,"gris")
lista_colores.insert(3,"naranja")
lista_colores.pop(1)
lista_colores.pop(3)
lista_colores.pop(3)
print(lista_colores)

paises_nuevos = paises.copy()
print(paises_nuevos)

lista_numeros = [1,1,2,65,24,82,32,63,62,645,3]
print(lista_numeros.count(1))

print(paises.index("españa"))

lista_numeros1 = [1,5,25,2,62,732]
lista_numeros1.sort(reverse=True)

print(lista_numeros1)

paises1 = ["españa","portugal","andorra","francia"]
print(len(paises1))