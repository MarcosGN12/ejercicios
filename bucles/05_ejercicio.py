lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]

for numero in lista_numeros:
     if numero == 10:
        continue
     
     if numero ==  356:
         break
     print(f"El valor del elemento es {numero}")
     