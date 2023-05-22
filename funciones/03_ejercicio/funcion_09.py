#9# 
def lista_caracteres (caracter,conjunto):
    lista_final = []
    for i in range(0,len(conjunto)):
          if caracter in conjunto[i]:
                lista_final.append(conjunto[i])
    return(lista_final)