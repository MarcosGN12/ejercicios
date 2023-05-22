#6# 
def ordenar_alfabeticamente (lista_palabras):
    resultado_final = []

    for i in lista_palabras:
          resultado_final.append(i)
    resultado_final.sort()
    print(f"Los numeros no repetidos son: {resultado_final} ")
    return resultado_final