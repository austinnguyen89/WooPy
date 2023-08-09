"""Main application file for WooPy.

This module contains the Flask application setup and routes for the WooPy project,
including endpoints for managing products, authentication, and settings.
"""

from flask import Flask, request, jsonify
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
    url=settings.WOO_COMMERCE_URL,  # Retrieve from settings
    consumer_key=settings.WOO_COMMERCE_API_KEY,
    consumer_secret=settings.WOO_COMMERCE_API_SECRET,
    version="wc/v3"
)

# Product management instance
product_management = ProductManagement(wcapi)

# Route to get all products


@app.route('/products', methods=['GET'])
def get_products():
    products = product_management.get_products()
    return jsonify(products)

# Route to add a new product


@app.route('/products', methods=['POST'])
def add_product():
    product_data = request.json
    response = product_management.add_product(product_data)
    return jsonify(response)

# Route to update a product


@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    updated_data = request.json
    response = product_management.update_product(product_id, updated_data)
    return jsonify(response)

# Route to delete a product


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    response = product_management.delete_product(product_id)
    return jsonify(response)

# Route to update WooCommerce API settings


@app.route('/settings', methods=['PUT'])
def update_settings():
    new_settings = request.json
    # Logic to update settings (e.g., save to database or file)
    return jsonify({"message": "Settings updated successfully"})

# Route for user authentication (e.g., login)


@app.route('/auth/login', methods=['POST'])
def login():
    credentials = request.json
    # Logic to authenticate user
    return jsonify({"message": "Login successful"})

# Route for user logout


@app.route('/auth/logout', methods=['POST'])
def logout():
    # Logic to log out user
    return jsonify({"message": "Logout successful"})


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
