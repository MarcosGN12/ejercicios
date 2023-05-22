#2#
def palindroma (palabra):
    primera_letra = 0
    ultima_letra = len(palabra) -1

    while palabra[primera_letra] == palabra[ultima_letra]:
          if primera_letra >= ultima_letra:
                return True
          primera_letra += 1
          ultima_letra -= 1
    return False