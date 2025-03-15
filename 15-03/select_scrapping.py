import requests  # responsável por enviar a requisição
from bs4 import BeautifulSoup  # responsável por tratar a requisição

# URL ajustada para buscar por SSDs de 1TB
url = "https://www.kabum.com.br/cgi-local/site/listagem/listagem.cgi?string=ssd+1tb&btnG="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    resposta = requests.get(url, headers=headers)
    resposta.raise_for_status()  # Verifica se houve algum erro na requisição
except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar o site: {e}")
else:
    if resposta.status_code == 200:
        print("Kabuum, aqui você encontra as melhores ofertas de SSDs de 1TB")
        soup = BeautifulSoup(resposta.text, "html.parser")
        promocoes = soup.find_all("div", class_="productCard")
        print(promocoes)

        if promocoes:
            print("Produtos encontrados:")
            for index, promocao in enumerate(promocoes):
                titulo = promocao.find("span", class_="nameCard").text.strip()
                link = promocao.find('a', href=True)['href']
                preco_texto = promocao.find("span", class_="priceCard").text.strip()
                preco = float(preco_texto.replace('R$', '').replace('.', '').replace(',', '.'))

                if preco < 500:
                    print(f"{index + 1}. {titulo} - R$ {preco:.2f} - https://www.kabum.com.br{link}")
        else:
            print("Nenhuma promoção encontrada.")
    else:
        print(f"Falha ao acessar a página. Status code: {resposta.status_code}")
    
    