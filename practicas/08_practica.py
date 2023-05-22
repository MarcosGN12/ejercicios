numeros1 = [1,2,3,4,5]
numeros2 = [5,7,8,9,6]
condiciones = [True,False,True,True,False]
multiplicado = []

for i in range (0,len(numeros1)):
    if condiciones[i] == True:
        
        num1 = numeros1[i]
        num2 = numeros2[i]
        multiplicacion = num1 * num2
        resultado = (multiplicacion,i)
        multiplicado.append(resultado)

print(multiplicado)