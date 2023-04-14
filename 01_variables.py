#variables

mi_variable = "Mi string variable"
print(mi_variable)

mi_variable_numero = 5
print(mi_variable_numero)

mi_bool_variable = True
print(mi_bool_variable)

#concatenacion de variables 

print(mi_variable_numero, mi_variable, mi_bool_variable)
print("Esto deberia decirme que tienes 5 años", mi_variable_numero)

#algunas funciones del sistema
#len = funcion para contrar numero de caracteres

print(len(mi_variable))

#variables en una sola linea

mi_nombre, mi_apellido, mi_edad = "Marcos", "GN", 17
print("Mi nombre es:",mi_nombre,"Mi apellido es:",mi_apellido,"Y mi edad es",mi_edad, )

#input = formulario de texto a rellenar 

'''''
cual_es_tu_nombre = input("dime tu nombre: ")
cual_es_tu_edad = input("dime tu edad: ")

print("Tu nombre es",cual_es_tu_nombre)
print("Tu edad es",cual_es_tu_edad)
'''''

#¿Forzamos el tipo?
address: str = "Mi direccion"
address = 32
address = 32.5
print(type(address))
