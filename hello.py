from flask import Flask, request, jsonify, uuid

app = Flask(__name__)

@app.route("/game", methods=['POST', 'GET'])
def feed():
    data = request.args
    gameList = []
    print(data['tes'])
    keys = ['name', 'game', 'character']
    for i in data:
        print(i)
        l = data[i].split('-')
        print(l)
        k = 0
        locals()[uuid.uuid4] = dict()
        for j in keys:
            foo.update({j: l[k]})
            k += 1
        # foo = {keys[0] : data['tes']}
        print(foo)
        gameList.append(foo)
    print(gameList)
    return jsonify(gameList)

@app.route("/test", methods=['POST', 'GET'])
def test():
    data = request.args
    print(data)
    return jsonify({'value received' : data['tes']}) 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"