 
from flask import Flask, jsonify, request, render_template

#criando aplicação em flask
app = Flask(__name__)
 

# GET > Buscar algo
@app.route('/helloworld', methods=['GET'])
def helloworld():
    return jsonify({
        "mgs":" Ola mundo como estao voces " 
    })
    
"""
JavaScript (front) = fetch
reactJS (front) = axios
insomnia (aplicativo) = simular um front
postman (aplicativo) = simular um front

back-end -> modelo de API -> FULL REST
Full = arquitetura MVC (model, view, controller)
"""
    
# POST - Criar  uma tarefas
@app.route('/tarefas', methods=['POST'])
def add_tarefas():
    nova_tarefa = request.json #pegar a informação no body
    nova_tarefa['id'] = len(tarefas) + 1 #adicionando novo id
    tarefas.append(nova_tarefa)# adicionanod nova tarefa na lista
    return jsonify(nova_tarefa), 201 #201 -> created -> criado com sucesso
    
#lista de tarefas 
tarefas =[
    {"id":1, "titulo": "Estudar Python", "feito": False},
    {"id":2, "titulo":"Ler a doc", "feito":True}        
]

@app.route('/tarefas', methods =['GET'])
def get_tarefas():
    return jsonify(tarefas)
    
#iniciar o servidor 
if __name__ == '__main__':
    app.run(debug=True)
    
#http://localhost:5000/helloworld 

