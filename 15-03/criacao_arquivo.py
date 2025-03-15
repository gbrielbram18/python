import csv

#criar e escrever um aquivo txt
with open("dados.txt", "w", encoding = "utf-8") as arquivo:
    arquivo.write("Nome, Idade, cidade\n")
    arquivo.write("Yuri Alberto, 27, São paulo")
    arquivo.write("arthur Morgan,30, Texas")
    arquivo.write("Gabriel , 19, cotia")
    
    
#Ler o conteudo 
# r -> Read -> Ler

with open("dados.txt", "r", encoding= "uft-8") as arquivo:
    print("Conteudo do Arqvuivo txt:")
    print(arquivo.read())
    
    
#criando dados csv
dados = [
    ["Nome", "Idade", "Cidade"]
    ["Carlos", "18" , "curitiba"]
    ["roger Gedes","26","Arabia saldita"]
    ["eren","18","paradis"]
]