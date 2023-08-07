from flask import Flask
from product_management import ProductManagement

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to WooPy!'


if __name__ == '__main__':
    app.run(debug=True)
