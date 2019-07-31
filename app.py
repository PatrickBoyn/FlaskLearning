from flask import Flask, jsonify, request

app = Flask(__name__)

# A faux database.
stores = [
    {
        'name': 'Food store',
        'items': [
            {
                'name': 'apple',
                'price': 1.99
            }
        ]
    }
]

# TODO keep track of what method you're putting things in.
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()

    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)

    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    pass


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    pass


@app.route('/store/<string:name>/item')
def get_item(name):
    pass


app.run(port=5000)
