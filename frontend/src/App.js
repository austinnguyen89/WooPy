import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import NavBar from './components/NavBar';
import ProductsPage from './components/ProductsPage';

const App = () => {
  return (
    <Router>
      <NavBar />
      <Switch>
        <Route path="/products" component={ProductsPage} />
        {/* Add other routes here */}
      </Switch>
    </Router>
  );
};

export default App;
