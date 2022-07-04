from flask import Flask, request, jsonify
import uuid
import json

app = Flask(__name__)

@app.route("/valorant", methods=['POST', 'GET'])
def game():
    with open('game.json', 'r') as f:
        data = json.load(f)
        # print(type(data))
        op = []
        for i in data:
            # print(type(i))
            for j in data[i]:
                # print(data[i][j])
                if 'valorant' in data[i][j]:
                    op.append(data[i])
                    break
    return jsonify(op)

@app.route("/krillxox", methods=['POST', 'GET'])
def player():
    with open('game.json', 'r') as f:
        data = json.load(f)
        # print(type(data))
        op = []
        for i in data:
            # print(type(i))
            for j in data[i]:
                # print(data[i][j])
                if 'krillxox' in data[i][j]:
                    op.append(data[i])
                    break
    return jsonify(op)

@app.route("/game", methods=['POST', 'GET'])
def feed():
    data = request.args
    gameList = {}
    keys = ['name', 'game', 'character']
    for i in data:
        # print(i)
        l = data[i].split('-')
        # print(l)
        k = 0
        foo = dict()
        for j in keys:
            foo.update({j: l[k]})
            k += 1
        # print(foo)
        gameList[uuid.uuid4().int] = foo
    # print(gameList)
    with open('game.json', 'w') as file:
        json.dump(gameList, file)
    return jsonify(gameList)

@app.route("/test", methods=['POST', 'GET'])
def test():
    data = request.args
    print(data)
    return jsonify({'value received' : data['tes']}) 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"