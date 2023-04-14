numeros = [7,8,9,3,10,1,12]
# for i in range(0,6):
#     num = int(input("ingresa el numero "))
#     numeros.append(num)    

# numero1 = numeros[0]
# numero2 = numeros[0]
# print("")
# print(f"primer numero {numero1}")



# for i in range(0,len(numeros)):
#     # print(f"valor de i = {i} ")
#     # print(numeros[i])  

#     actual = numeros[i]
#     siguiente = numeros[i+1]
#     print("")
#     print(f"actual {numeros}")
#     print("")

#     if actual > siguiente:
#         print(f"antes {numeros}")
#         numeros[i] = siguiente
#         numeros[i+1]= actual
#         print(f"despues {numeros}")


for i in range(0,len(numeros)):
    
    print("LA I ES")
    print(numeros[i])
    actual = numeros[i]
    

    print("LAS J SON")
    for j in range(i,len(numeros)):
        siguiente = numeros[j]

        if actual > siguiente:
            print(f"antes {numeros}")
            numeros = siguiente
            numeros[i+1]= actual
            print(f"despues {numeros}")

 
print(numeros)
        