# numeros pares em um intervalo

"""
solicite dois numeros inteiros ao usuario 
representando o inicio e o fim de um intervalo 
mostre todos os numeros pares nesse intervalo
(incluindo limite inicial e final, se forem pares)
"""

# Números pares em um intervalo

print("Digite o número inicial do intervalo:")
inicio = int(input())

print("Digite o número final do intervalo:")
fim = int(input())

print("Números pares no intervalo de", inicio, "a", fim, ":")

for num in range(inicio, fim + 1):
    if num % 2 == 0:
        print(num)
