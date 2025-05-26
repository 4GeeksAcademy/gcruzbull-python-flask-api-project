from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "Estudiar backend", "done": False },
    { "label": "Asistir a box", "done": False }
]

@app.route('/todos', methods=['GET'])
def todo_list():
    json_todos = jsonify(todos)
    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(dict(request_body))
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.remove(todos[position])
    return jsonify(todos)

# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)