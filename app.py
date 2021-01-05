from flask.signals import message_flashed
from products import products
from flask import Flask, jsonify, request

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
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity'],
    }
    products.append(new_product)
    return jsonify({"message": "Producto agregado satifactoriamente", "Productos": products})


@app.route('/produtcs/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFounts = [
        product for product in products if product['name'] == product_name]
    if (len(productFounts) > 0):
        productFounts[0]['name'] = request.json['name']
        productFounts[0]['price'] = request.json['price']
        productFounts[0]['quantity'] = request.json['quantity']
        return jsonify({"message": "Producto editado satifactoriamente", "Producto": productFounts[0]})
    else:
        return jsonify({"message": "Producto no encontrado"})


@app.route('/produtcs/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFounts = [
        product for product in products if product['name'] == product_name]
    if (len(productFounts) > 0):
        products.remove(productFounts[0])
        return jsonify({"message": "Producto eliminado satifactoriamente"})
    else:
        return jsonify({"message": "Producto no encontrado"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
