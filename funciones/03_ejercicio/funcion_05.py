#5# 
def numeros_duplicados (lista_numeros):

    unico = []

    for i in lista_numeros:
          if i not in unico:
                unico.append(i)
    return unico