import math

x1 = int(input("Escribeme la cordenada x1: "))
y1 = int(input("Escribeme la cordenada y1: "))

x2 = int(input("Escribeme la cordenada x2: "))
y2 = int(input("Escribeme la cordenada y2: "))

variable1 = x2 - x1
variable2 = y2 - y1

elevacion1 = pow(variable1, 2)
elevacion2 = pow(variable2, 2)

suma = elevacion1 + elevacion2
raiz_cuadrada = math.sqrt(suma)
print(raiz_cuadrada)
