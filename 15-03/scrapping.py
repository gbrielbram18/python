import requests #responsavel por enviar a requisição
from bs4 import BeautifulSoup #responsavel por tratar a requisição

#class -> feed-post-link

#URL do site
url = "https://www.kabum.com.br/ofertas/megaday?pagina=1&limite=20"

headers = {
    "User-Agent": "mozilla/5.0 (Windonws NT 10.0; Win64; x64) applewebkit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

#fazendpo a requisição HTTP
resposta = requests.get(url)

#Verifica se dey tudo certo
if resposta.status_code == 200:
    #codigo 200 -> sucesso
    print("Requisição bem sucedida!")
    #print(resposta.text) #retorno 
    #preenchendo nossa sopa
    soup = BeautifulSoup(resposta.text ,"html.parser")
    #encontra as noticias
    noticias = soup.find_all("a", class_="feed-post-link")
    
    print("ultimos produtos em promoção:")
    for index, noticia in enumerate(noticias):
        print(f"{index + 1 }. {noticia.text.strip()} - {noticia['href']}")