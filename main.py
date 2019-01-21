import logging
from dao_impl import Dao
from flask import Flask,redirect,request,jsonify

app = Flask(__name__)
dao = Dao()


@app.route('/hello')
def hello() :
    name = request.args.get('name')
    age = request.args.get("age")
    out_dict = {"name":name, "age":age}
    return jsonify(out_dict), 200


@app.route('/product/create')
def create_product():
    title = request.args.get('title')
    price = request.args.get("price")
    count = request.args.get('inventory_count')
    product_id = request.args.get("product_id")
    data = {"title":title, "price":price, "inventory_count":int(count), "product_id":product_id}
    dao.create_product(product_id, data)
    return "Success", 200


@app.route('/product/fetch')
def fetch_product():
    product_id = request.args.get("product_id")
    result = dao.fetch_product_id(product_id)
    if not result:
        return "Product does not exist", 200
    return jsonify(result), 200


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)