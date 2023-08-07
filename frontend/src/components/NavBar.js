import React from 'react';
import { Link } from 'react-router-dom';

const NavBar = () => {
    return (
        <nav>
            <Link to="/">Home</Link>
            <Link to="/products">Products</Link>
            <Link to="/categories">Categories</Link>
            <Link to="/orders">Orders</Link>
            <Link to="/profile">Profile</Link>
        </nav>
    );
};

export default NavBar;
