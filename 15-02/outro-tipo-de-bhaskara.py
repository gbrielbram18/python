# math
# ** 0.5

import  math

print("calculadora de bhaskara")
a = float(input("digite o valor de A" ))
b = float(input("digite o valor de B"))
c = float(input("digite o valor de C"))

delta = b**2 - 4 * a * c
print ("delta: ",  delta )

raiz_delta = math.sqrt(delta) #função de raiz

x1 = (-b + raiz_delta) / (2 * a)
x2 = (-b - raiz_delta) / (2 * a)