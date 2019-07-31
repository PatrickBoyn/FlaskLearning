from flask import Flask

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


@app.route('/store', methods=['POST'])
def create_store():
    pass


@app.route('/store/<string:name>')
def get_store(name):
    pass


@app.route('/store')
def get_stores():
    pass


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    pass


@app.route('/store/<string:name>/item')
def get_item(name):
    pass


app.run(port=5000)
