import React, { useEffect, useState } from 'react';

const ProductsPage = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        // Fetch products from the backend
        fetch('/api/products')
            .then((res) => res.json())
            .then((data) => setProducts(data));
    }, []);

    return (
        <div>
            <h1>Products</h1>
            {products.map((product) => (
                <div key={product.id}>{product.name}</div>
            ))}
        </div>
    );
};

export default ProductsPage;
