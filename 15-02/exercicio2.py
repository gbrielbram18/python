#verificar se uma palavra e um palidromo
# caso seja, exiba "e palidromo"
# caso nao seja, "nao e uma palidromo"
# a verificação deve ser caseb senstivo

#valendo = barra de chocolate

def palindromo(palavra):
    if palavra == palavra[::-1]:
        print("E palindromo")
    else:
        print("Nao e palindromo")

palavra = input("Digite uma palavra: ")
palindromo(palavra)


