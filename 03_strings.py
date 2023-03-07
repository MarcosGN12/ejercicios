### Strings ###

my_string = "string"
my_other_string = "mi string"

print(len(my_other_string))
print(len(my_string))

salto_de_linea = "mi string tiene un\nsalto de linea"
print(salto_de_linea)

tabulacion = "\t mi string tiene un salto de linea"
print(tabulacion)

mi_nombre, mi_apellido, mi_edad = "Marcos", "GN", 17
print("mi nombre es {} mi apellido es {} y mi edad es {}".format(mi_nombre, mi_apellido, mi_edad))
print("mi nombre es %s mi apellido es %s y mi edad es %d" %(mi_nombre, mi_apellido, mi_edad))
print("mi nombre es" + " " + mi_nombre + " " + "mi apellido es" + " " + mi_apellido + " " + "mi edad es" + " " + str(mi_edad))
print(f"Mi nombre es {mi_nombre} mi apellido es {mi_apellido} y mi edad es {mi_edad}") #la f ajusta {} para que funcionen

#desempaquetar caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

reversed_language = language[::-2]
print(reversed_language)

print(language.capitalize())
print(language.upper())
print(language.lower())
print("1".isnumeric())
print(language.count("t"))
print(language.upper().isupper)
print(language.startswith("hpy"))

