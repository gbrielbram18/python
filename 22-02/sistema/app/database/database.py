import json # lidar com arquivo JSON
from pathlib import Path # lidar com caminhos com WIN

class BancoFake:
    
    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": [], "produtos": []}
        self._carregar()

    def _carregar(self):
        """
        Carrega dados do arquivo JSON, se existir.
        Caso não existir, inicia com dados vazios
        """
        caminho = Path(self.arquivo_db)
        if caminho.is_file():
            # abrindo arquivo no modo de leitura em UTF-8 (PT-BR)
            with open(caminho, 'r', encoding="utf-8") as data:
                # salvando dados que já existem no arquivo
                # na variável dados
                self.dados = json.load(data)
        else:
            self._salvar()
            
    def _salvar(self):
        """
        salvar o conteúdo do self.dados no arquivo JSON
        """
        # abrindo arquivo no modo W (escrita)
        with open(self.arquivo_db, 'w', encoding="utf-8") as data:
            # realizando DUMP (python para JSON) para salvar no banco 
            json.dump(self.dados, data, ensure_ascii=False, indent=4)
            
    def adicionar_cliente(self, cliente_dict):
        self.dados["clientes"].append(cliente_dict)
        self._salvar()
        
    def listar_clientes(self):
        return self.dados["clientes"]
    
    
    def adicionar_produto(self, produto_dict):
        self.dados["produtos"].append(produto_dict)
        self._salvar()
        
    def listar_produtos(self):
        return self.dados["produtos"]