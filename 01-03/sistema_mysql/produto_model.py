import mysql.connector

from config import Config

class ProdutoModel: 

    def __init__(self):
        #iniciando a configuração
        self.config = Config()
    
        self.connection = mysql.connector.connect(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            database=self.config.MYSQL_DB
        )
        
        # Faz o cursor trazer o resultado em dicionarios  
        self.cursor=self.connection.cursor(dicionary=True)