import json #lidar com aquivo JSON
from pathlib import Path #lidar com caminhos com WIN


class BancoFake:
    
    def __init__(self, arquivo_db="banco.jshon"):
        self.arquivo_db = arquivo_db
        self.dados ={"clientes":[], "produtos":[]}
        self._carregar()

    def _carregar(self):
            """
            Carrega dados do arquivo JSON, se existir.
            Caso não existir, inicia com dados vazios
            """
            caminho = Path(self.arquivo_db)
            if caminho.is_file():
#abrindo arquivo no modo de leitura em UTF-8(PT-BR)         
                 with open(caminho , 'r', encoding="utf-8") as data:
#salvando dados que ja existem no arquivo
#na variavel dados
                    self.dados = json.load(data)
            else:
                self._salvar()
            
            
    def _salvar (self):
        """
        salvar o conteudo do self.dados no arquivo JSON
        """
        #abrindo arquivo no modo W(escrita)
        with open(self.arquivo_db, 'w', encoding="uft-8") as data:
            #realizando DUMP (python para JSON) para salvar no banco 
            json.dump(self.dados, data, ensure_ascii=False, indent=4)
            
    def adicionar_cliente(self, cliente_dict):
        self.dados["clinte"].append(cliente_dict)
        self._salvar()
        
    def listar_clientes(self):
        return self.dados["clientes"]