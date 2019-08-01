from flask import Flask, jsonify, request, render_template

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


@app.route('/')
def home():
    return render_template('index.html')


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
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({'Error': 'No store by that name.'})


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    request_data = request.get_json()

    for store in stores:

        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }

            store['items'].append(new_item)

            return jsonify(new_item)

    return jsonify({'error': "store wasn't found."})


@app.route('/store/<string:name>/item')
def get_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
        else:
            return jsonify({'Error': 'Item does not exist.'})


app.run(port=5000)
