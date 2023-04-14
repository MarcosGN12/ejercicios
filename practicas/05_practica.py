estudiantes = [("Ana", 7, 8, 9), ("Carlos", 6, 7, 8), ("Laura", 9, 9, 9), ("Pedro", 5, 6, 7), ("María", 8, 8, 7)]

promedio = []

for estudiante in estudiantes:

        nota1 = estudiante[1]
        nota2 = estudiante[2]
        nota3 = estudiante[3]

        media = (nota1 + nota2 + nota3) / 3
        
        promedio.append(media)
        
        # print(f"la media de {estudiante[0]} es {media}")


for i in range(0,len(promedio)):
        print(f"El promedio de {estudiantes[i][0]} es {promedio[i]}")

