print("")
print("Pokedex")
print("")

bulbasur = (1,"bulbasur","agua",113,250,130,60,"1,40m","50Kg")
pikachu = (2,"pikachu","rayo",130,170,40,120,300,"1,50m","40Kg")
charmander = (3,"charmander","fuego",100,150,200,78,20,"1,50m","50Kg")
squirtel = (4,"squirtel","agua",102,210,120,400,200,"1,10m","30Kg")
pidgey = (5,"pidgey","tierra",120,90,50,210,100,"1,30m","50Kg")
pokemons = [bulbasur,pikachu,charmander,squirtel,pidgey]

for pokemon in pokemons:
    print(pokemon[0])
    print(pokemon[1])
    print("")

while True:

    opcion = float(input("pokemon que quieras ver mas a detalle?: "))
        
    if opcion == 1:  

        print(pokemons[0])
        print("si quieres volver al listado de pokemon introduce 0")
    if opcion == 2:

        print(pokemons[1]) 
        print("si quieres volver al listado de pokemon introduce 0")  
    if opcion == 3:

        print(pokemons[2])
        print("si quieres volver al listado de pokemon introduce 0")
    if opcion == 4:

        print(pokemons[3])
        print("si quieres volver al listado de pokemon introduce 0")
    if opcion == 5:
        print(pokemons[4])
        print("si quieres volver al listado de pokemon introduce 0")
    
    if opcion == 0:
        for pokemon in pokemons:
            print(pokemon[0])
            print(pokemon[1])
            print("")