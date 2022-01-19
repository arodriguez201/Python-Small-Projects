from flask import Flask, request, jsonify
import products_dao
from sqlconnection import get_sql_connection

connection = get_sql_connection()

app = Flask(__name__)


@app.route('/getProducts', methods=["GET"])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['Product_id'])
    response = jsonify({
        'Product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flash Server For Grocery Store Management System")
    app.run(port=5000)
