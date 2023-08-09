"""Main application file for WooPy.

This module contains the Flask application setup and routes for the WooPy project,
including endpoints for managing products, authentication, and settings.
"""

from flask import Flask, request, jsonify, abort
from dotenv import load_dotenv
from product_management import ProductManagement
from woocommerce import API
import settings

# Load environment variables from .env file
load_dotenv()

# Create Flask app
app = Flask(__name__)

# WooCommerce API setup
wcapi = API(
    url=settings.WOO_COMMERCE_URL,
    consumer_key=settings.WOO_COMMERCE_API_KEY,
    consumer_secret=settings.WOO_COMMERCE_API_SECRET,
    version="wc/v3"
)

# Product management instance
product_management = ProductManagement(wcapi)


@app.route('/products', methods=['GET'])
def get_products():
    """Fetch all products."""
    products = product_management.get_products()
    return jsonify(products)


@app.route('/products', methods=['POST'])
def add_product():
    """Add a new product."""
    product_data = request.json
    if 'name' not in product_data or 'price' not in product_data:
        abort(400, description="Missing required fields")
    response = product_management.add_product(product_data)
    return jsonify(response)


@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update an existing product."""
    updated_data = request.json
    response = product_management.update_product(product_id, updated_data)
    return jsonify(response)


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product."""
    response = product_management.delete_product(product_id)
    return jsonify(response)

# Additional routes for authentication, settings, etc.


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
