altura = -1

while altura <= 0:
    print("La altura es")
    altura = int(input("Dame la altura "))
    

print(f"la altura es {altura}")

linea_anterior = "*"
for i in range(0,altura): 
          
        print(linea_anterior)
        linea_anterior = "*" + linea_anterior + "*"