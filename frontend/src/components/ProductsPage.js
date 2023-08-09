import React, { useState, useEffect } from 'react';

const ProductsPage = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        // Fetch products from the backend
    }, []);

    return (
        <div className="products-page">
            <h1>Product Management</h1>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Price</th>
                        <th>Stock</th>
                        {/* Other columns */}
                    </tr>
                </thead>
                <tbody>
                    {products.map((product) => (
                        <tr key={product.id}>
                            <td>{product.name}</td>
                            <td>{product.price}</td>
                            <td>{product.stock}</td>
                            {/* Other columns */}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ProductsPage;
