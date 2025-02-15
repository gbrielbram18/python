#def somar_numeros(num1,num2):
#        return num1 + num2

#resultado= somar_numeros (4,4)
#print("o resultado é: " ,resultado)


def verificaIdade(idade):
    if idade >= 18:
        return "pode ver o filme"
    else:
        return "nao pode ver o filme "
    
print("digite sua idade ")
idade = int(input())

resultado = verificaIdade(idade)

print(resultado)
