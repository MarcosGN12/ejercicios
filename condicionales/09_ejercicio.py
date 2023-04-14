numero = input("Ingrese una contraseña: ")

if len(numero) <= 8:
    print("La contraseña debe tener al menos 8 caracteres")

elif any(char.isdigit() for char in numero):
    print("La contraseña debe incluir al menos una letra")

elif any(char.isalpha() for char in numero):
    print("La contraseña debe incluir al menos un numero")

else:
    print("Contraseña válida")