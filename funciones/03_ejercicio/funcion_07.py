#7# 
def lista_mayor_numero (numero_entero,lista_numeros):
    lista_mayor = []
    for i in range(0,len(lista_numeros)):
          if lista_numeros[i] > numero_entero:
                lista_mayor.append(lista_numeros[i])
    return lista_mayor