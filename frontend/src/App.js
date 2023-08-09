import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Settings from './components/Settings';
import ProductsPage from './components/ProductsPage';
import NavBar from './components/NavBar';

function App() {
  return (
    <Router>
      <NavBar />
      <Switch>
        <Route path="/login" component={Login} />
        <Route path="/settings" component={Settings} />
        <Route path="/products" component={ProductsPage} />
        {/* Other routes */}
      </Switch>
    </Router>
  );
}

export default App;
