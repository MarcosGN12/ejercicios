cadena = input("escribe cadena ")
print(cadena)

letras = []

for i in range(0,len(cadena)):
    letra = cadena[i]
    
    # print(letra)
    
    if not letra in letras:
        letras.append(letra)
       
print("las letras que no se repiten son: ", len(letras)) 

