from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    {
        'id':'1',
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        'id':'2',
        "done": True,
        "label": "Sample Todo 2"
    }
]

@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    json = jsonify(todos)
    return json

@app.route('/', methods=['POST'])
def add_todo_list():
    request_body = request.data
    print(json.loads(request_body))
    todos.append(json.loads(request_body))
    print(todos)
    return 'ok'

@app.route('/delete/<string:id>', methods=['DELETE'])
def delete_list_by_id(id):
    for item in todos:
        if item.get('id') == id:
            todos.remove(item)
        else:
            print('no existe el elemento')
            return 'no existe el elemento'

    print(todos)
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
