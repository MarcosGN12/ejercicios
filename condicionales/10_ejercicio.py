numero = int(input("Por favor inserte un numero: "))

if numero >= 18:
    print("eres mayor de edad")
    if numero <= 25 and not numero == 18:
        print("todavia eres joven")
else:
    print("no eres mayor de edad")
