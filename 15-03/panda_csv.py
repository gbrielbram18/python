import pandas as pd
import matplotlib.pyplot as plt

#criar os dados para o nosso dataframe

dados = {
    "nome" : ["Arthur","Maria", "Matheus","Carlos", "Bruna"],
    "Idade" : [28,22,18,35,20],
    "Cidade" : ["Cotia","Carapikuiba","Cotia","Osasco","Cotia"]
}

df = pd.DataFrame(dados)
#Exibir o Dataframe
print(df)

#salvar dataFrame
df.to_csv("panda_dados.csv" , index= False)

#Visualizar em data frame CSV
df_csv = pd.read_csv("panda_dados.csv")

df_fitrar = df[df["Idade"] > 25]
print (df_fitrar) #Todas as pessoas com menos de 25 anos não aparecem

df_ordenado = df.sort_values(by = "Idade", ascending = False)
print (df_ordenado) # Do maior para o menor (Decrescente)

#Exibir estabilidade 
print(df.describe())

#media por cidade, coluna idade
media_cidade = df.groupby("Cidade")["Idade"].mean()
print(media_cidade)

#df.plot(kind="bar", x = "Nome", y = "Idade", color = "blue" )
#plt.title("Idade das pessoas")
#plt.xlabel("Nome")
#plt.ylabel("Idade")
#plt.show()  

df.boxplot(column="idade", by= "Cidade", grid= False)
plt.title("Distribuição de idades por cidade")
plt.xlabel("Cidade")
plt.ylabel("Idade")

plt.show() 