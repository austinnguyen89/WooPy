import React from 'react';
import { Link } from 'react-router-dom';

const NavBar = () => {
    return (
        <nav className="nav-bar">
            <Link to="/">Home</Link>
            <Link to="/settings">Settings</Link>
            <Link to="/products">Product Management</Link>
            <Link to="/logout">Logout</Link>
        </nav>
    );
};

export default NavBar;
