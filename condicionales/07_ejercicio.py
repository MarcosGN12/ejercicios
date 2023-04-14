nombre = str(input("Por favor ingrese su nombre: "))
edad = int(input("Por favor ingrese su edad: "))


print(f"Hola {nombre}")

if edad < 18:
    print("Eres menor de edad")

if edad > 18:
    print("Eres mayor de edad")

if edad == 18:
    print("Tienes 18 años")