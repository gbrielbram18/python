from flask import Flask
from flask_mysqldb import MySQL
from controllers.produto_controller import produto_bp
import config

app = Flask(__name__) # instaciar o Flask
app.config.from_object(config) #configurar variaveis

mysql = MySQL(app)

#passa a conexão para os controllers
app.mysql = mysql

#registrar o controller
app.register_blueprint(produto_bp )

#Rodar o app
if __name__ == '__main__':
    app.run(debug = True)