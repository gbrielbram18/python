# sistema de desconto fde veiculos
# solicite o nome do veiculo
# e o preço  do veiculo
# se o preço > 80k -> 60% de desconto 
# se o preço > 50k -> 30% de desconto
# se o preço < 30k -> Nao existe 

nome_veiculo = input("digite o nome do veiculo: ")
preco_veiculo = float(input("digite o preco do veiculo: "))

if preco_veiculo > 80000:
    desconto = 0.60

elif preco_veiculo > 50000:
    desconto = 0.30

else:
    desconto = 0


valor_desconto = preco_veiculo * desconto
valor_final = preco_veiculo - valor_desconto

print("o nome do veiculo e: ", nome_veiculo)
print("o valor do desconto e: ", valor_final)
print("o desconto foi: ", desconto)
