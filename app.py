from flask.signals import message_flashed
from products import products
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!!!"})


@app.route('/produtcs')
def getProducts():
    return jsonify({"Productos": products})


@app.route('/produtcs/<string:product_name>')
def getProduct(product_name):
    productFounts = [
        product for product in products if product['name'] == product_name]
    if (len(productFounts) > 0):
        return jsonify({"Productos": productFounts[0]})
    return jsonify({"Productos": products})


@app.route('/produtcs', methods=['POST'])
def addProduct():
    return 'Recibido'


if __name__ == '__main__':
    app.run(debug=True, port=4000)
