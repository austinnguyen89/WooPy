from woocommerce import API


class ProductManagement:
    def __init__(self, woocommerce_instance):
        self.woocommerce = woocommerce_instance

    def get_products(self):
        try:
            # Fetch products from WooCommerce
            products = self.woocommerce.get("products")
            return products
        except Exception as e:
            print(f"Error fetching products: {e}")
            return None

    def add_product(self, product_data):
        try:
            # Add a new product to WooCommerce
            response = self.woocommerce.post("products", product_data)
            return response
        except Exception as e:
            print(f"Error adding product: {e}")
            return None

    def update_product(self, product_id, updated_data):
        try:
            # Update an existing product in WooCommerce
            response = self.woocommerce.put(
                f"products/{product_id}", updated_data)
            return response
        except Exception as e:
            print(f"Error updating product: {e}")
            return None

    def delete_product(self, product_id):
        try:
            # Delete a product from WooCommerce
            response = self.woocommerce.delete(f"products/{product_id}")
            return response
        except Exception as e:
            print(f"Error deleting product: {e}")
            return None

# Example usage:
# wcapi = API(
#     url="http://example.com",
#     consumer_key="consumer_key",
#     consumer_secret="consumer_secret",
#     version="wc/v3"
# )
# product_management = ProductManagement(wcapi)
# products = product_management.get_products()
