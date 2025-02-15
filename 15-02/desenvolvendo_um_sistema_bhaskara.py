#desenvolvendo um sistema
#valor A, Valor B e Valor C
#calcular bhaskara
#delta = b² - 4 * a * c
#Bhaskara

print(" seja bem vindo a formula de bhaskara")
print("digite o valor de A")
A = int(input())
print("digite o valor de B")
B = int(input())
print("digite o valor de C")
C = int(input())

delta = B ** 2 - 4 * A * C
print("delta = ", delta)

if delta < 0:
    print("não existe raiz real")
else:
    x1 = (-B + delta ** 0.5) / (2 * A)
    x2 = (-B - delta ** 0.5) / (2 * A)
    print("x1 = ", x1)
    print("x2 = ", x2)



