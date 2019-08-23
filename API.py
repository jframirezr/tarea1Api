from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

tipos = {'sensor': 'ds18b20', 'variable': 'temperatura', 'unidades': 'grados'}


temperatura = [
    {'fecha': '21-08-2019', **tipos, 'v': 20},
    {'fecha': '22-08-2019', **tipos, 'v': 25},
    {'fecha': '23-08-2019', **tipos, 'v': 30},

]

@app.route('/t', methods =['GET'])
def getAll():
    return jsonify(temperatura)

@app.route('/t/t', methods = ['GET'])
def getMayores():
    temperatura.sort(key = lambda d: d['v']) 
    body = request.json
    p = float(body['p'])
    l = len(temperatura)
    r = int(round(l*p))
    return jsonify(temperatura[l-r:])


@app.route('/t', methods =['POST'])
def postOne():
    now = datetime.now()
    body = request.json
    body['fecha']= datetime.strftime(now, '%d-%m-%Y')
    body['v']= int(body['v'])
    temperatura.append({**body, **tipos})
    return jsonify(temperatura)


app.run(port=3010, debug=True)